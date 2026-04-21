import sqlite3


conn = sqlite3.connect("books.db")

cursor = conn.cursor()

# Create the books table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    title TEXT,
    author TEXT,
    year INTEGER
)
""")

# Save (commit) the changes
conn.commit()

# Close the connection
conn.close()