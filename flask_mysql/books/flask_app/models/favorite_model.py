from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask_app.models import author_model



class Favorite:
    def __init__(self, data):
        self.id = data['id']
        self.book_id = data['book_id']
        self.author_id = data['author_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        # ------------------------------------------------ SAVE NEW BOOK
    @classmethod
    def save(cls,data):
        query = """
                INSERT INTO favorites (book_id, author_id) 
                VALUES (%(book_id)s, %(author_id)s);
                """
        return connectToMySQL(DB).query_db(query, data)
    
    @classmethod
    def save(cls,data):
        query = """
                INSERT INTO favorites (book_id, author_id) 
                VALUES (%(book_id)s, %(author_id)s);
                """
        return connectToMySQL(DB).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = """
                SELECT * FROM favorites;
                """
        
        return connectToMySQL(DB).query_db(query)


    @staticmethod
    def validation(data):
        is_valid = True
        favorites = Favorite.get_all()
        print('**',favorites,'**')
        for row in favorites:
            print('book id--','data',data['book_id'],'row',row['book_id'])
            print('author id--','data',data['author_id'],'row',row['author_id'])
            if int(data['book_id']) == row['book_id'] and int(data['author_id']) == row['author_id'] :
                is_valid = False

        return is_valid
