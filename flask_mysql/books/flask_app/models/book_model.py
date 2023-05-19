from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask_app.models import author_model


class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        # ------------------------------------------------ SAVE NEW BOOK
    @classmethod
    def save(cls,data):
        query = """
                INSERT INTO books (title, num_of_pages ) 
                VALUES (%(title)s, %(num_of_pages)s);
                """
        return connectToMySQL(DB).query_db(query, data)
    
        # ------------------------------------------------ GET ALL
    @classmethod
    def get_all_books(cls):
        query = 'SELECT * FROM books'
        results = connectToMySQL(DB).query_db(query)
        all_books = []
        for row in results:
            book_instance = cls(row)
            all_books.append(book_instance)
        return all_books
    

    @classmethod
    def get_all_favs_by_book(cls, data):
        query = """
                SELECT * FROM books b 
                LEFT JOIN favorites f ON b.id = f.book_id
                LEFT JOIN authors a ON f.author_id = a.id 
                WHERE b.id = %(id)s;
                """
        results = connectToMySQL(DB).query_db(query, data)
        print(results)
        book = cls(results[0])
        authors = []
        for row in results:
            
            data = {
                'id': row['a.id'],
                'name': row['name'],
                'created_at': row['a.created_at'],
                'updated_at': row['a.updated_at']
            }
            author = author_model.Author(data)
            authors.append(author)
            book.favs = authors
        print('**\n\n',book,'\n\n**')
        return book
