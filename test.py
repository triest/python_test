from server.DB import DB

db = DB();
# db.conect();
db.test()
db.insert('deposit', '2018-12-09', 'bob', 12, 'EUR')
