import sqlite3

conn = sqlite3.connect("books.db")
cursor = conn.cursor()

# adding books to our data base
more_books = [
    ("Fahrenheit 451", "Ray Bradbury", 1953),
    ("Brave New World", "Aldous Huxley", 1932),
    ("To Kill a Mockingbird", "Harper Lee", 1960),
    ("The Catcher in the Rye", "J.D. Salinger", 1951),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925),
    ("Moby-Dick", "Herman Melville", 1851),
    ("The Lord of the Rings", "J.R.R. Tolkien", 1954),
    ("Pride and Prejudice", "Jane Austen", 1813),
    ("The Chronicles of Narnia", "C.S. Lewis", 1950),
    ("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979),
    ("The Alchemist", "Paulo Coelho", 1988)
]

# Formatting to add those books by using the more_books list
cursor.executemany("INSERT INTO books VALUES (?, ?, ?)", more_books)

conn.commit()
conn.close()
