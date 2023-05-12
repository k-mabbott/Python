from flask_app.config.mysqlconnection import connectToMySQL


DB = 'dojos_and_ninjas_schema'

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.dojo_id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
# ------------------------------------------SAVE
    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO ninjas ( dojo_id, first_name, last_name, age ) 
            VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s);
            """
        return connectToMySQL(DB).query_db(query, data)
# ------------------------------------------ GET ONE
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM ninjas WHERE ninjas.id = %(id)s;"
        ninja_from_db = connectToMySQL(DB).query_db(query,data)
        return cls(ninja_from_db[0])
# ------------------------------------------ GET ALL
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        ninjas_from_db =  connectToMySQL(DB).query_db(query)
        ninjas =[]
        for one_ninja in ninjas_from_db:
            ninjas.append(cls(one_ninja))
        return ninjas
    
# # ------------------------------------------ GET ALL FROM A DOJO
#     @classmethod
#     def get_all_from_dojo(cls):
#         query = "SELECT * FROM ninjas WHERE dojo_id = %(id)s;"
#         ninjas_from_db =  connectToMySQL(DB).query_db(query)
#         ninjas =[]
#         for one_ninja in ninjas_from_db:
#             ninjas.append(cls(one_ninja))
#         return ninjas
    
# ------------------------------------------ UPDATE
    @classmethod
    def update(cls,data):
        query = """
                UPDATE ninjas SET dojo_id=%(dojo_id)s, first_name=%(first_name)s, last_name=%(last_name)s, age=%(age)s
                WHERE id = %(id)s;"""
        return connectToMySQL(DB).query_db(query,data)

# ------------------------------------------ DESTROY
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query,data)