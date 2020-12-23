from flask import render_template, url_for, flash, redirect
from firstflask import app, db, bcrypt
from firstflask.Form import RegistartionForm, LoginForm
from firstflask.models import User, Post
    
posts = [
    {
     'author':'Tanu',
     'title':'Blog Post',
     'content':'Posted checking',
     'date_posted': 'April20,2020'
     },
    {
     'author':'Bineeta',
     'title':'Blog Posting Second',
     'content':'Post checking!',
     'date_posted': 'April20,2022'
     } 
    ]
@app.route('/')
@app.route('/home') 
def homee():
    return render_template('homee.html', posts=posts) 

@app.route('/about') 
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form= RegistartionForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user= User(username= form.username.data, email= form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created You can now Login', 'success')
        return redirect(url_for('homee'))
    return render_template('register.html', title= 'Register', form=form)

@app.route('/login') 
def login():
    form= LoginForm()
    return render_template('login.html', title= 'Login', form=form)