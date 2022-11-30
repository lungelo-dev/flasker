from flask import Flask, render_template, flash, request, redirect, url_for
from datetime import datetime 
#from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate
#from werkzeug.security import generate_password_hash, check_password_hash 
from datetime import date
#from webforms import LoginForm, PostForm, UserForm, PasswordForm, NamerForm, SearchForm
#from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
#from webforms import LoginForm, PostForm, UserForm, PasswordForm, NamerForm
#from flask_ckeditor import CKEditor
#from werkzeug.utils import secure_filename
#import uuid as uuid
import os

#create a flask instance
app = Flask(__name__)

@app.route('/')
def index():
    first_name = "Lungelo"
    #return "<h1>chenges</h1>" #This was overwritten by the statement below whic routes to the index file 
    return render_template('index.html', first_name = first_name)

#localhost:5000/user/john
@app.route('/user/<name>')
def user(name):
    #return '<h1>Hello {}</h1>'.format(name)
    return render_template('users.html',user_name=name)

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

# INTERNAL sEVER eRROR
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"),500


app.config['SECRET_KEY'] = "my super secret key"

