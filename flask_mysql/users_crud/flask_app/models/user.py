from flask_app.config.mysqlconnection import connectToMySQL

DB = 'users_crud'

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
# ------------------------------------------- SAVE 
    @classmethod
    def save(cls, data):
        query = """INSERT INTO users (first_name,last_name,email) 
                VALUES (%(first_name)s,%(last_name)s,%(email)s)"""
        return connectToMySQL(DB).query_db(query , data)
    
# ------------------------------------------- GET ONE
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE users.id = %(id)s;"
        one_user = connectToMySQL(DB).query_db(query,data)
        print(one_user)
        return one_user
# ------------------------------------------- GET ALL
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        users_from_db = connectToMySQL(DB).query_db(query)
        all_users =[]
        for one_user in users_from_db:
            all_users.append(cls(one_user))
        return all_users
    
# ------------------------------------------- UPDATE
    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query,data)
# ------------------------------------------- DELETE
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query,data)
