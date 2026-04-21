from sqlalchemy import create_engine, text

# connects to our books.db
engine = create_engine("sqlite:///books.db")


with engine.connect() as conn:
    result = conn.execute(text("SELECT title FROM books ORDER BY title ASC"))
    
    for row in result:
        print(row.title)

