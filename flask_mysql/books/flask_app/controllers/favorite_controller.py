

from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.author_model import Author
from flask_app.models.book_model import Book
from flask_app.models.favorite_model import Favorite


@app.route('/create_favorite_book/<int:id>', methods=['POST'])
def save_favorite_book(id):
    print(request.form)
    data = {
        **request.form,
        'book_id': id
        
    }
    Favorite.save(data)
    return redirect('/books')

@app.route('/create_favorite_author/<int:id>', methods=['POST'])
def save_favorite_author(id):
    print(request.form)
    data = {
        **request.form,
        'author_id': id
        
    }
    
    if not Favorite.validation(data):
        return redirect('/authors')
    Favorite.save(data)
    return redirect('/authors')


