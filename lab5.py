from flask import Blueprint, render_template, url_for, redirect, request, make_response, session
lab5 = Blueprint('lab5', __name__)

@lab5.route('/lab5/')
def lab():
    return render_template('lab5/lab5.html')
