from flask import Blueprint, render_template, request, abort, current_app, redirect, url_for, flash
from flask.json import jsonify
from db import db
from db.models import User, Article
from datetime import datetime
from db.models import db
import hashlib
import os
from os import path

lab8 = Blueprint('lab8', __name__)

@lab8.route('/lab8/')
def main():
    return render_template('lab8/lab8.html')

@lab8.route('/lab8/login')
def login():
    return render_template('lab8/login.html')

@lab8.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab8/register.html')
    
    login_form = request.form.get('login')
    password_form = request.form.get('password')

    if not login_form or not login_form.strip():
        return render_template('lab8/register.html', error='Введите логин!')
    if not password_form or not password_form.strip():
        return render_template('lab8/register.html', error='Введите пароль!')

    login_exists = User.query.filter_by(login=login_form).first()
    if login_exists:
        return render_template('lab8/register.html', error='Такой пользователь уже существует')

    password_hash = generate_password_hash(password_form)
    new_user = User(login=login_form, password=password_hash)
    db.session.add(new_user)
    db.session.commit()
    
    login_user(new_user, remember=False)
    
    return redirect('/lab8/')

@lab8.route('/lab8/articles')
def articles():
    return render_template('lab8/articles.html')

@lab8.route('/lab8/create')
def create():
    return render_template('lab8/create.html')

@lab8.route('/lab8/test-db')
def test_db():
    from app import db  
    try:
        result = db.session.execute('SELECT version(), current_user, current_database()')
        db_info = result.fetchone()
        
        return jsonify({
            "success": True,
            "data": {
                "version": db_info[0],
                "user": db_info[1],
                "database": db_info[2],
                "database_uri": current_app.config['SQLALCHEMY_DATABASE_URI']
            }
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500
    