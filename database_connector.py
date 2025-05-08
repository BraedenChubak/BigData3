import sqlite3

connection = sqlite3.connect('chinook.db')
cursor = connection.cursor()
sql_query = """SELECT name FROM sqlite_master WHERE type='table';"""
cursor.execute(sql_query)
print(cursor.fetchall())
