from flask import Blueprint, render_template, url_for, redirect, request, make_response, session, current_app

lab7 = Blueprint('lab7', __name__)

@lab7.route('/lab7/')
def main():
    return render_template('lab7/lab7.html')
