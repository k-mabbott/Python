
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.book_model import Book
from flask_app.models.author_model import Author


@app.route('/')
@app.route('/authors')
def home():
    all_authors = Author.get_all_authors()
    print(all_authors)
    return render_template('authors.html', all_authors=all_authors)


@app.route('/author/new', methods=['POST'])
def create_author():

    new_author = Author.save(request.form)
    return redirect('/')

@app.route('/author/<int:id>')
def show_author(id):
    books = Book.get_all_books()
    author = Author.get_all_authors_with_books({'id':id})
    return render_template('author_show.html', author=author, books=books)

