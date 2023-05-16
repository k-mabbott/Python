
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.recipe_model import Recipe
from flask_app.models.user_model import User
import datetime

# ----------------------------------------------------- DASHBOARD

@app.route('/recipes')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    logged_user = User.get_by_id(data)
    all_recipes = Recipe.get_all_with_name()
    print(all_recipes)
    return render_template('dashboard.html', logged_user=logged_user, all_recipes=all_recipes)

# ----------------------------------------------------- EDIT PAGE
@app.route('/recipe/edit/<int:id>')
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': id
    }
    recipe = Recipe.get_one_with_name(data)
    print(recipe)
    return render_template('recipe_edit.html', recipe = recipe)

# ----------------------------------------------------- EDIT PAGE/REDIRECT
@app.route('/recipe/update/<int:id>', methods=['POST'])
def update_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        **request.form,
        'id': id
    }
    Recipe.update(data)
    return redirect('/')

# ----------------------------------------------------- SHOW PAGE
@app.route('/recipe/<int:id>')
def show_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': id
    }
    recipe = Recipe.get_one_with_name(data)
    recipe.date_cooked = recipe.date_cooked.strftime('%B %d,%Y')
    return render_template('recipe_show_one.html', recipe = recipe)

# ----------------------------------------------------- NEW PAGE
@app.route('/recipe/new')
def new_recipe():
    if 'user_id' not in session:
        return redirect('/')

    return render_template('recipe_add.html')

# ----------------------------------------------------- NEW PAGE / REDIRECT
@app.route('/recipe/add', methods=['POST'])
def add_recipe():
    if 'user_id' not in session:
        return redirect('/')
    print('---------------\n\n\n', request.form)
    if not Recipe.validation(request.form):
        print(request.form['name'])
        # data = {
        #     **request.form
        # }
        return redirect('/recipe/new')
    data = {
        **request.form,
        'user_id': session['user_id']
    }
    recipe = Recipe.save(data)
    print(recipe)
    return redirect('/')
    
# ----------------------------------------------------- DELETE
@app.route('/recipe/delete/<int:id>')
def delete_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    Recipe.destroy({'id': id})
    return redirect('/')


