from os import getenv
import pymysql
import json
from django.core.serializers import json
import requests


class DB:
    cursor = ""


    def conect(self):
        db = pymysql.connect("localhost", "root", "", "python")
        cur = db.cursor()
        return cur

    def test(self):
        connection = pymysql.connect("localhost", "root", "", "python", charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        try:

            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT * FROM `transfers`"
                cursor.execute(sql)
                result = cursor.fetchone()
                print(result)
        finally:
            connection.close()

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
        self.insert(data['method'], data['date'], data['account'], data['amt'], data['ccy'])

    # get course from API and convert to EURO, return EURO
    def convert(self, ammount, ccy):  # ссн - валюта для перевода
        r = requests.get(url='https://api.exchangeratesapi.io/latest?symbols=' + ccy)
        r = r.json()
        rates = r['rates'][ccy]
        euro = ammount / rates
        return euro

    # check history operation and summ in euro prom last 3 dats
    def calcSumInEuro(self):
        connection = pymysql.connect("localhost", "root", "", "python", charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                # get tracsactions for last 3 days
                sql = "SELECT * FROM `transfers` WHERE `create_at` BETWEEN CURRENT_TIMESTAMP - INTERVAL '3' DAY AND CURRENT_TIMESTAMP"
                cursor.execute(sql)
                result = cursor.fetchall()
                # для всех строчек перевоим в евро
                conut = 1;
                for row in result:
                    print(row)
                    print(row["id"])
        except Exception:
            print("Error in summ")
        finally:
            # Close connection.
            connection.close()



            # SELECT * FROM `transfers` WHERE create_at
            #      BETWEEN CURRENT_TIMESTAMP - INTERVAL '3' DAY
            #           AND CURRENT_TIMESTAMP
