from flask import Blueprint, render_template, request, abort, current_app, redirect, url_for, flash
from flask.json import jsonify
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

@lab8.route('/lab8/register')
def register():
    return render_template('lab8/register.html')

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
    