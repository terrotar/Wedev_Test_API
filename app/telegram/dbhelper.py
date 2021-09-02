import sqlite3


class DBHelper:
    def __init__(self, dbname="database/sqlite.db"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname, check_same_thread=False)

    def add_user(self, id_user, first_name, last_name, cel_number):
        stmt = "INSERT INTO usuario (id_user, first_name, last_name, cel_number) VALUES (?, ?, ?, ?)"
        args = (id_user, first_name, last_name, cel_number)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_user(self, id_user):
        stmt = "SELECT * FROM usuario WHERE id_user = (?)"
        args = (id_user)
        self.conn.execute(stmt, args)

    def close(self):
        self.conn = sqlite3.close()
