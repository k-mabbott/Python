from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DB
from flask_app.models import user_model
import re

ALPHA = re.compile(r"^[a-zA-Z]+$") 


class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_cooked = data['date_cooked']
        self.under = data['under']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
    
# ------------------------------------------------ SAVE NEW RECIPE
    @classmethod
    def save(cls,data):
        query = """
                INSERT INTO recipes (user_id, name, description, instructions, date_cooked, under ) 
                VALUES (%(user_id)s, %(name)s, %(description)s, %(instructions)s, %(date_cooked)s, %(under)s);
                """
        return connectToMySQL(DB).query_db(query, data)
    
# ------------------------------------------------ GET BY ID
    @classmethod
    def get_by_id(cls, data):
        query = """
                SELECT * FROM recipes WHERE id = %(id)s;
                """
        results = connectToMySQL(DB).query_db(query, data)
        if results:
            return cls(results[0])
        return False
    
# ------------------------------------------------ GET ONE RECIPE W/ USER NAME
    @classmethod
    def get_one_with_name(cls, data):
        query = """
                SELECT r.*, u.first_name FROM recipes r 
                JOIN users u ON r.user_id = u.id
                WHERE r.id = %(id)s;
                """
        # print(query)
        results = connectToMySQL(DB).query_db(query, data)
        recipe = cls(results[0])
        print(results[0])
        recipe.chef = results[0]['first_name']
        return recipe
# ------------------------------------------------ GET ALL RECIPES W/ USER NAME
    @classmethod
    def get_all_with_name(cls):
        query = """
                SELECT * FROM recipes r 
                JOIN users u ON r.user_id = u.id;
                """
        results = connectToMySQL(DB).query_db(query)
        all_recipes = []
        if results:
            for row in results:
                print(row, '--**--\n\n\n')
                this_recipe = cls(row)
                user_data = {
                    **row,
                    'id': row['u.id'],
                    'created_at': row['u.created_at'],
                    'updated_at': row['u.updated_at']
                }
                this_user = user_model.User(user_data)
                this_recipe.chef = this_user
                all_recipes.append(this_recipe)
        return all_recipes
    
# ------------------------------------------------ UPDATE
    @classmethod
    def update(cls,data):
        query = """
                UPDATE recipes SET name=%(name)s, description=%(description)s, 
                instructions=%(instructions)s, date_cooked=%(date_cooked)s,  under=%(under)s
                WHERE id = %(id)s;"""
        return connectToMySQL(DB).query_db(query,data)
    
    # ------------------------------------------ DESTROY
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query,data)

    
# ------------------------------------------------ VALIDATION CHECK
    @staticmethod
    def validation(data):
        is_valid = True
        # ----------------------------------------- Name
        if len(data['name']) < 1 :
            is_valid = False
            flash('Invalid Name!', 'name')
        elif len(data['name']) < 3 :
            is_valid = False
            flash('Invalid Name! * must be 3 characters long', 'name')
        elif len(data['name']) > 45 :
            is_valid = False
            flash('Invalid Name! * must not be more than 45 characters long', 'name')
        # ----------------------------------------- Description
        if len(data['description']) < 1 :
            is_valid = False
            flash('Invalid Description!', 'description')
        elif len(data['description']) < 3 :
            is_valid = False
            flash('Invalid Description! * must be 3 characters long', 'description')
        elif len(data['description']) > 255 :
            is_valid = False
            flash('Invalid Description! * must not be more than 255 characters long', 'description')
        # ----------------------------------------- Instructions
        if len(data['instructions']) < 1 :
            is_valid = False
            flash('Invalid Instructions!', 'instructions')
        elif len(data['instructions']) < 3 :
            is_valid = False
            flash('Invalid Instructions! * must be 3 characters long', 'instructions')
        # ----------------------------------------- Date
        if 'date' not in data:
            is_valid = False
            flash('Date Required!', 'date')
        # ----------------------------------------- Under / Radio buttons
        if 'under' not in data:
            is_valid = False
            flash('Under 30 is Required', 'under')
        # ----------------------------------------- END of Validations
        return is_valid


