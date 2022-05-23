from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Book,User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

views=Blueprint('views',__name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html")

@views.route('/search',methods=['GET','POST'])
@login_required
def  search():
    if request.method=="POST":  
        search=request.form.get('search')

        book=Book.query
        users=User.query
        books=book.filter(Book.bookname.like('%'+search+'%'))
        return render_template("search.html",books=books,users=users)
        


        
    return render_template("search.html")

@views.route('/add',methods=['GET','POST'])
@login_required
def add():
    if request.method=="POST":       
    
        bookname=request.form.get('bookname')
        author=request.form.get('author')
        edition=request.form.get('edition')
        genre=request.form.get('genre')


        new_user=Book(bookname=bookname,author=author,genre=genre,edition=edition,user_id=current_user.id)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('views.home'))
    return render_template("add.html", user=current_user)