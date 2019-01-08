from os import getenv
import pymysql
import json
from django.core.serializers import json
import requests


# class DB
#
#

class DB:
    cursor = ""
    limit = 10000;

    def conect(self):
        db = pymysql.connect("localhost", "root", "", "python")
        cur = db.cursor()
        return cur



    # insert data in databese
    def insert(self, method, date, account, amt, ccy):
        connection = pymysql.connect("localhost", "root", "", "python", charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                # insert in databese
                sql = "INSERT INTO `transfers`( `method`, `date`, `account`, `amt`, `ccy`) VALUES (%s,%s,%s,%s,%s)"
                # cursor.execute(sql, ('deposit', '2018-12-09', 'bob', 12, 'EUR',))
                cursor.execute(sql, (method, date, account, amt, ccy))
                result = cursor.fetchone()
                connection.commit()
        except Exception:
            print("Insert Error:")
        finally:
            # Close connection.
            connection.close()

    # parse json for insert in DB
    def parse(self, data):
        # chouse methor for operation
        if data['method'] == 'deposit' or data['method'] == 'withdrawal':  # для метода deposit or withdrawal
            if self.calcSumInEuro(data['account'], data['ccy'], data['amt']) < self.limit:
                self.insert(data['method'], data['date'], data['account'], data['amt'], data['ccy'])
                return True
            else:
                return False
        elif data['method'] == 'transfer':
            to_account = data['to_account']
            from_account = data['from_account']
            sumTo = self.calcSumInEuro(to_account, 'EUR', 5);
            sumFrom = self.calcSumInEuro(from_account, 'EUR', 5);
            if sumFrom < self.limit and sumTo < self.limit:
                self.insert(data['method'], data['date'], to_account, data['amt'], data['ccy'])
                self.insert(data['method'], data['date'], from_account, data['amt'], data['ccy'])
                return True
        elif data['method'] == 'get_balances':
            return True

    # get course from API and convert to EURO, return EURO
    def convert(self, ammount, ccy):  # ссн - валюта для перевода
        try:
            if ammount == None or ammount < 0:  # chect ammount
                return None
            str = 'https://api.exchangeratesapi.io/latest?symbols=' + ccy
            r = requests.get(url=str)
            r = r.json()
            rates = r['rates'][ccy]
            if rates != None and rates > 0:
                euro = ammount / rates
            else:
                return None
            return euro
        except Exception:
            print("error in convert API")
        return None

    # check history operation and summ in euro prom last
    # input: bank account, valute for calculate, number od last days
    #
    def calcSumInEuro(self, account, calcCCy, forDays):

        sum = 0
        try:
            connection = pymysql.connect("localhost", "root", "", "python", charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor)
            with connection.cursor() as cursor:
                # get tracsactions for last 3 days
                sql = "SELECT * FROM `transfers` WHERE account=%s and `create_at` BETWEEN CURRENT_TIMESTAMP - INTERVAL %s DAY AND CURRENT_TIMESTAMP"
                cursor.execute(sql, (account, forDays))
                result = cursor.fetchall()
                count = 0
                for row in result:
                    amt = row['amt']
                    ccy = row['ccy']
                    print(ccy + ' ' + calcCCy)
                    if (ccy == calcCCy):
                        sum += amt
                    else:
                        convert = self.convert(amt, ccy)
                        if (convert != None):
                            sum += convert


        except Exception:
            print("Error in summ")
        return sum
