from os import getenv
import pymysql
import json
from django.core.serializers import json


class DB:
    cursor = ""
    server = getenv("MACHINE-VOIV7EH\SQLEXPRESS");
    database = getenv("transfers")
    username = getenv("MACHINE-VOIV7EH\\triest")
    password = getenv("")

    def conect(self):
        db = pymysql.connect("localhost", "root", "", "python")
        cur = db.cursor()

    def test(self):
        print("func")
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
                # Read a single record
                sql = "INSERT INTO `transfers`( `method`, `date`, `account`, `amt`, `ccy`) VALUES (%s,%s,%s,%s,%s)"
                # cursor.execute(sql, ('deposit', '2018-12-09', 'bob', 12, 'EUR',))
                cursor.execute(sql, (method, date, account, amt, ccy))
                result = cursor.fetchone()
                connection.commit()
                print(result)
        except Exception:
            print('Это что ещё такое?')
        finally:
            # Close connection.
            connection.close()

    # parse json for insert in DB
    def parse(self, data):
        print("in parse:")
        self.insert(data['method'], data['date'], data['account'], data['amt'], data['ccy'])
  