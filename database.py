import sqlite3

def connect_db():
    connection = sqlite3.connect("app.db")
    return connection 