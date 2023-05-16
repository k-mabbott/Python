from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DB
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
ALPHA = re.compile(r"^[a-zA-Z]+$") 
ALPHANUMERIC = re.compile(r"^[a-zA-Z0-9]+$") 


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
    
# ------------------------------------------------ SAVE NEW USER
    @classmethod
    def save(cls,data):
        query = """
                INSERT INTO users (first_name, last_name) 
                VALUES (%(first_name)s, %(last_name)s);
                """
        return connectToMySQL(DB).query_db(query, data)
    
# ------------------------------------------------ GET BY ID
    @classmethod
    def get_by_id(cls, data):
        query = """
                SELECT * FROM users WHERE id = %(id)s;
                """
        results = connectToMySQL(DB).query_db(query, data)
        if results:
            return cls(results[0])
        return False
    
# ------------------------------------------------ GET BY ID
    @classmethod
    def get_all(cls):
        query = """
                SELECT * FROM users;
                """
        results = connectToMySQL(DB).query_db(query)
        if results:
            all_users = []
            for row in results:
                one_user = cls(row)
                all_users.append(one_user)
            return all_users
        return False



# ------------------------------------------------ VALIDATION CHECK
    @staticmethod
    def validation(data):
        is_valid = True
        # -----------------------------------------First Name
        if len(data['first_name']) < 1 :
            is_valid = False
            flash('Invalid First Name!', 'first_name')
        elif len(data['first_name']) < 2 :
            is_valid = False
            flash('Invalid First Name! * must be 2 characters long', 'first_name')
        elif not ALPHA.match(data['first_name']):
            is_valid = False
            flash('Invalid First Name! * must be letters only ', 'first_name')
        # -----------------------------------------Last Name
        if len(data['last_name']) < 1 :
            is_valid = False
            flash('Invalid last name!', 'last_name')
        elif len(data['last_name']) < 2 :
            is_valid = False
            flash('Invalid last name! * must be 2 characters long', 'last_name')
        elif not ALPHA.match(data['last_name']):
            is_valid = False
            flash('Invalid Last Name!  * must be letters only', 'last_name')


        return is_valid

