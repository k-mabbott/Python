from flask_app.config.mysqlconnection import connectToMySQL

class Restaurant:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # list for all burgers within that restaurant
        self.burgers = []

        @classmethod   
        def save(cls, data):
            query = """
                    INSERT INTO restaurants ( name , created_at , updated_at ) 
                    VALUES (%(name)s,NOW(),NOW());
                    """
            return connectToMySQL('burgers').query_db(query, data)