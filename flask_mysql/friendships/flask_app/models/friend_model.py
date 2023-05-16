from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask_app.models import user_model
from flask import flash


class Friend:
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.friend_id = data['friend_id']

# ------------------------------------------------ SAVE NEW Friendship
    @classmethod
    def save_friend(cls,data):
        query = """
                INSERT INTO friendships (user_id, friend_id) 
                VALUES (%(user_id)s, %(friend_id)s);
                """
        return connectToMySQL(DB).query_db(query, data)
# ------------------------------------------------ GET ALL FRIENDSHIPS
    
    @classmethod
    def get_all_friendship(cls):
        query = """
                SELECT * FROM friendships f 
                JOIN users u ON u.id = f.user_id 
                JOIN users ON friend_id = users.id;
                """
        results = connectToMySQL(DB).query_db(query)

        all_friends = []
        for row in results:
            friend_instance = cls(row)
            data1 = {
                'id': row['id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            }
            data2 = {
                'id': row['users.id'],
                'first_name': row['users.first_name'],
                'last_name': row['users.last_name'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
            }
            friend1 = user_model.User(data1)
            friend2 = user_model.User(data2)
            friend_instance.friend1 = friend1
            friend_instance.friend2 = friend2
            all_friends.append(friend_instance)

        # @classmethod'
        # def read():


        # print(results, '\n\n**\n\n', all_friends)
        return all_friends
        
# ------------------------------------------------ VALIDATIONS

    @staticmethod
    def validation(data):
        is_valid=True
        if data['user_id'] == data['friend_id']:
            is_valid = False
            flash('*Users can not be friends with themselves', 'friendship')
        all_friendships = Friend.get_all_friendship()
        for friendship in all_friendships:
            # print('\nDATA\n\n', data, '\nFRIENDSHIP\n', friendship)
            # print('DF',data['friend_id'],'FF', friendship.friend_id ,'DU', data['user_id'], 'FU', friendship.user_id)
            # print(data['friend_id'], )
            # print('is friend = friend', (int(data['friend_id']) == friendship.friend_id))
            # print('Friend Type ===', type(friendship.friend_id), '\n\nData Type ==', type(data['user_id']))
            # print('is user = user', (data['user_id'] == friendship.user_id))
            if (int(data['friend_id']) == friendship.friend_id) and (int(data['user_id']) == friendship.user_id):
                print('HIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII')
                is_valid = False
                flash('Friendship Already Exists!', 'friendship')
                break
        
        return is_valid



