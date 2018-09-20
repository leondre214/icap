from flask import Flask, render_template, request, redirect, flash
from wtforms import StringField, PasswordField, BooleanField, validators
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, Email
from playhouse.postgres_ext import *


# Registration form


#class RegistrationForm(FlaskForm):
    #username = StringField('Username', validators=[InputRequired(), Length(min=4, max=16, message='Please provide a valid username')])
    #email = StringField('Email Address', validators=[Email(message='Please provide a valid email address')])
    #password = PasswordField('Password', validators=[InputRequired(), Length(min=12, max=20, message='Password must have atleast 12 characters')])
    # Accept_rules = BooleanField('I agree to the terms and conditions of this site', [validators.InputRequired()])


# Login form

#class LoginForm(FlaskForm):
    #username = StringField('Username', [validators.length(min=4, max=25)])
    #password = PasswordField('Password', [validators.length(min=12, max=20, message='Password must have 12 char')])


# Create data base for adding and deleting users and comment CRUD.

#ext_db = PostgresqlExtDatabase('web_page', user='postgres')

# This model uses the "web_page.db" database


#class Higher(Model):
    #class Meta:
        #database = ext_db


#class New_usr(Higher):
    #id = PrimaryKeyField(primary_key=True)
    #username = CharField(unique=True)
    #email = CharField(unique=True)
    #password = CharField(unique=True)


# Initialize db


#def initialize_db():
    #ext_db.connect()
    #ext_db.create_tables(New_usr)
    #initialize_db()


# Create web page instance


app = Flask(__name__)
#app.config['SECRET_KEY'] = 'Adrianaleondrejuangrant081517'


# Create homepage/welcome page & Navigation Bar and additional routes


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/neets')
def neets():
    return render_template('Neets.html')


@app.route('/volumes')
def volumes():
    return render_template('volumes.html')


@app.route('/bibs')
def bibs():
    return render_template('bibs.html')


@app.route('/IC3')
def ic3():
    return render_template('ic3.html')


@app.route('/IC2')
def ic2():
    return render_template('ic2.html')


@app.route('/IC1')
def ic1():
    return render_template('ic1.html')


@app.route('/ICC')
def icc():
    return render_template('icc.html')


@app.route('/about')
def about():
    return render_template('about.html')


# Create Forum, registration, and login
@app.route('/forum')
def forum():
    return render_template('forum.html')


#@app.route('/forum/register', methods=['GET', 'POST'])
#def register():
    #form = RegistrationForm()
    #if form.validate_on_submit():
       # new_user = New_usr(username=form.username.data, email=form.email.data, password=form.password.data)
        #new_user.save()
        #return redirect('forum/register/success')

    #return render_template('register.html', form=form)


#@app.route('/forum/register/success')
#def success():
    #return render_template('success.html')


#@app.route('/forum/login', methods=['POST'])
#def login():
    #if request.method == 'POST':
        #redirect('/forum')
    #return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
