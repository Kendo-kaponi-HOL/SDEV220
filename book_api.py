# Stephen Garcia Perez
# M4_LAB - Case Study: Python API
# Program allows for creation of Book API with delete, add, and get requests, by importing Flask, request, and SQLAlchemy. Database has been setup as well as functions that allow said actions

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///drinks.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80), unique=False, nullable=False)
    publisher = db.Column(db.String(80), unique=True)
    
    def __repr__(self):
        return f"{self.id} - {self.name} - {self.author} - {self.publisher}"
    
@app.route('/')
def index():
    return  {"Message": "Welcome to the book API",
            "routes": {
                "/books": "List all books"
            }
            }
    
@app.route('/books')
def get_books():
    books = Book.query.all()
    
    output = []
    for book in books:
        book_data = {"id": book.id, "name": book.name, "author": book.author, "publisher": book.publisher}
    
        output.append(book_data)
    return {"books": output}

@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {"id": book.id, "name": book.name, "author": book.author, "publisher": book.publisher}
    
@app.route('/books', methods=['POST'])
def add_book():
    book = Book(name=request.json["name"], author=request.json["author"], publisher=request.json["publisher"])
    db.session.add(book)
    db.session.commit()
    return {"id": book.id}

@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"Error": "Book not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "Book successfully deleted"}
