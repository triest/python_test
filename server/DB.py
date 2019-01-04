from os import getenv
import pymysql


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
