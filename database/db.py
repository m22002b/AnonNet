import sqlite3
import hashlib

class DataBase:
    def __init__(self, path):
        self.connect = sqlite3.connect(path)
        self.cursor = self.connect.cursor()

        with self.connect:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL,
                    password TEXT NOT NULL
                )
            """)

            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS login(
                    email INTEGER NOT NULL,
                    password INTEGER NOT NULL
                )
            """)
    
    def create_user(self, name: str, username: str, email: str, password: str):
        key = hashlib.sha256(password.encode('utf-8')).hexdigest()

        with self.connect:
            self.cursor.execute(
                "INSERT INTO users VALUES (?,?,?,?)",
                [name, username, email, key]
            )

            self.cursor.execute(
                "INSERT INTO login VALUES (?,?)",
                [email, key]
            )
