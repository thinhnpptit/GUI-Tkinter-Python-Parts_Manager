import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS Parts (id INTEGER PRIMARY KEY AUTOINCREMENT, part TEXT, customer TEXT, amount INTEGER, price TEXT, branch TEXT)")

        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM Parts")
        rows = self.cur.fetchall()
        return rows

    def insert(self, part, customer, amount,price, branch):
        self.cur.execute("INSERT INTO Parts VALUES (NULL, ?,?,?,?,?)",(part, customer, amount,price,branch))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM Parts WHERE id=?",(id,))
        self.conn.commit()

    def update(self, id, part, customer, amount,price, branch):
        self.cur.execute("UPDATE Parts SET part=?,customer=?,amount=?,price=?,branch=? WHERE id=?",(part,customer,amount,price,branch,id))
        self.conn.commit()

    def reset(self):
        self.cur.execute("DELETE FROM Parts")
        self.cur.execute("DELETE FROM sqlite_sequence WHERE name = 'Parts'")
        self.cur.execute("UPDATE sqlite_sequence SET id = 1 WHERE name = 'Parts'")
        self.conn.commit()

    def __del__(self):
        self.conn.close()

db = Database('store_parts.db')

# db.insert("8GB DDR4 RAM", "Jimmy", 2,"400")