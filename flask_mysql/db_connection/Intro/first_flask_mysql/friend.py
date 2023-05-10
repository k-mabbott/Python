

# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Friend:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    def __repr__(self):
        rep = f'friend( {self.first_name} {self.last_name} {self.occupation} )'
        return rep

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('first_flask').query_db(query)
        # Create an empty list to append our instances of friends
        friends = []
        # Iterate over the db results and create instances of friends with cls.
        for friend in results:
            friends.append( cls(friend) )
        return friends
            
    # ------------------- CREATE
    @classmethod
    def save(cls, data ):
        query = """INSERT INTO friends ( first_name , last_name , occupation , created_at, updated_at ) 
                    VALUES ( %(fname)s , %(lname)s , %(occ)s , NOW() , NOW() );"""
        # data is a dictionary that will be passed into the save method from server.py
        result = connectToMySQL('first_flask').query_db( query, data )
        return result
    # --------------------- GET ONE
    @classmethod
    def get_one(cls, id):
        query = """SELECT * FROM friends WHERE id = %(id)s"""
        results = connectToMySQL('first_flask').query_db(query, {'id': id} )
        # one_friend = results[0]
        return cls(results[0])
    # --------------------- GET ALL
    @classmethod
    def get_al(cls):
        query = "SELECT * FROM friends;"
        results = connectToMySQL('first_flask').query_db(query)
        all_friends = []

        for row in results:
            # make friend object and add to list
            all_friends.append(cls(row))
        return all_friends