from flask import Blueprint, render_template, url_for, redirect, request, make_response, session, current_app
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
import os
from os import path

lab6 = Blueprint('lab6', __name__)

@lab6.route('/lab6/')
def lab():
    return render_template('lab6/lab6.html')
