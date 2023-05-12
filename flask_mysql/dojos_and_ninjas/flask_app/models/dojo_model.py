
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja_model import DB
from flask_app.models import ninja_model

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
# --------------------------------------------SAVE
    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO dojos ( name ) 
            VALUES (%(name)s);
            """
        return connectToMySQL(DB).query_db(query, data)
# -------------------------------------------- GET ALL

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        dojos_from_db = connectToMySQL(DB).query_db(query)
        dojos =[]
        for one_dojo in dojos_from_db:
            dojos.append(cls(one_dojo))
        print(dojos)
        return dojos
# --------------------------------------------GET ONE W/ ALL NINJAS

    @classmethod
    def get_all_ninjas(cls, id):
        query = "SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        dojos_ninjas_db = connectToMySQL(DB).query_db(query, id)
        print(dojos_ninjas_db)
        if dojos_ninjas_db:
            dojo_instance = cls(dojos_ninjas_db[0])
            print('\n\n\n', dojo_instance)
            ninjas_list = []
            for one_row in dojos_ninjas_db:
                ninja_data = {
                    'id': one_row['ninjas.id'],
                    'dojo_id': one_row['dojo_id'],
                    'first_name': one_row['first_name'],
                    'last_name': one_row['last_name'],
                    'age': one_row['age'],
                    'created_at': one_row['ninjas.created_at'],
                    'updated_at': one_row['ninjas.updated_at']
                }
                ninja_instance = ninja_model.Ninja(ninja_data)
                ninjas_list.append(ninja_instance)
            print(ninjas_list)
            dojo_instance.ninjas = ninjas_list

            return dojo_instance

        return dojos_ninjas_db
    

