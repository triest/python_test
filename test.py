from server.DB import DB

db = DB();
# db.conect();
# db.test()
# db.insert('deposit', '2018-12-09', 'bob', 12, 'EUR')

# euro=db.convert(77.679,'RUB')
# print(euro)
sum = db.calcSumInEuro('bob')

print("sum for last 3 days for account ")
print(sum)
