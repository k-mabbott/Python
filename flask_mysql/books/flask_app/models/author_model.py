from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask_app.models import book_model


class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # ------------------------------------------------ SAVE NEW AUTHOR
    @classmethod
    def save(cls,data):
        query = """
                INSERT INTO authors (name) 
                VALUES (%(name)s);
                """
        return connectToMySQL(DB).query_db(query, data)
    
    @classmethod
    def get_all_authors(cls):
        query = 'SELECT * FROM authors'
        results = connectToMySQL(DB).query_db(query)
        all_authors = []
        for row in results:
            author_instance = cls(row)
            all_authors.append(author_instance)
        return all_authors
    

    @classmethod
    def get_all_authors_with_books(cls,data):
        query = """
                SELECT * FROM authors a 
                LEFT JOIN favorites f ON a.id = f.author_id
                LEFT JOIN books b ON f.book_id = b.id 
                WHERE a.id = %(id)s;
                """
        results = connectToMySQL(DB).query_db(query,data)
        print(results)
        if results:
            author = cls(results[0])
            books=[]
            for row in results:

                data = {
                    'id': row['b.id'],
                    'title': row['title'],
                    'created_at': row['b.created_at'],
                    'updated_at': row['b.updated_at']
                }
                book = book_model.Book(row)
                books.append(book)
            author.favs = books
            return author
        return False
