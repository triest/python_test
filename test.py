from server.DB import DB

db = DB();
# db.conect();
# db.test()
# db.insert('deposit', '2018-12-09', 'bob', 12, 'EUR')

# euro=db.convert(77.679,'RUB')
# print(euro)
db.calcSumInEuro()
