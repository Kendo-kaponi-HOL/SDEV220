import sqlite3

conn = sqlite3.connect("books.db")
cursor = conn.cursor()

cursor.execute("SELECT title FROM books ORDER BY title ASC")
rows = cursor.fetchall()

for row in rows:
    print(row[0])

conn.close()
