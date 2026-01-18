from flask import Blueprint, render_template, request, redirect, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from db.models import db, User, Article

lab8 = Blueprint('lab8', __name__)

@lab8.route('/lab8/')
def main():
    return render_template('lab8/lab8.html')

@lab8.route('/lab8/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('lab8/login.html')
    
    login_form = request.form.get('login')
    password_form = request.form.get('password')
    remember_me = request.form.get('remember_me') == 'on'
    
    if not login_form or not login_form.strip():
        return render_template('lab8/login.html', error='Введите логин!')
    if not password_form or not password_form.strip():
        return render_template('lab8/login.html', error='Введите пароль!')
    
    user = User.query.filter_by(login=login_form).first()
    
    if user and check_password_hash(user.password, password_form):
        login_user(user, remember=remember_me)
        return redirect('/lab8/')
    
    return render_template('lab8/login.html', error='Ошибка входа: логин и/или пароль неверны')

@lab8.route('/lab8/register', methods=['GET', 'POST'])
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

    password_hash = generate_password_hash(password_form, method='pbkdf2:sha256', salt_length=16)
    new_user = User(login=login_form, password=password_hash)
    db.session.add(new_user)
    db.session.commit()
    
    login_user(new_user, remember=False)
    
    return redirect('/lab8/')

@lab8.route('/lab8/articles')
@login_required
def articles():
    user_articles = Article.query.filter_by(user_id=current_user.id).all()
    return render_template('lab8/articles.html', articles=user_articles)

@lab8.route('/lab8/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'GET':
        return render_template('lab8/create.html')
    
    title = request.form.get('title')
    article_text = request.form.get('article_text')
    
    if not title or not title.strip():
        flash('Введите заголовок!', 'error')
        return render_template('lab8/create.html')
    if not article_text or not article_text.strip():
        flash('Введите текст статьи!', 'error')
        return render_template('lab8/create.html')
    
    new_article = Article(
        title=title,
        article_text=article_text,
        user_id=current_user.id,
        likes=0
    )
    
    db.session.add(new_article)
    db.session.commit()
    
    return redirect('/lab8/articles')

@lab8.route('/lab8/edit/<int:article_id>', methods=['GET', 'POST'])
@login_required
def edit(article_id):
    article = Article.query.filter_by(id=article_id, user_id=current_user.id).first()
    
    if not article:
        return "Статья не найдена", 404
    
    if request.method == 'GET':
        return render_template('lab8/edit.html', article=article)
    
    title = request.form.get('title')
    article_text = request.form.get('article_text')
    
    if not title or not title.strip():
        flash('Введите заголовок!', 'error')
        return render_template('lab8/edit.html', article=article)
    if not article_text or not article_text.strip():
        flash('Введите текст статьи!', 'error')
        return render_template('lab8/edit.html', article=article)
    
    article.title = title
    article.article_text = article_text
    db.session.commit()
    
    return redirect('/lab8/articles')

@lab8.route('/lab8/delete/<int:article_id>', methods=['POST'])
@login_required
def delete(article_id):
    article = Article.query.filter_by(id=article_id, user_id=current_user.id).first()
    
    if not article:
        return "Статья не найдена", 404
    
    db.session.delete(article)
    db.session.commit()
    
    return redirect('/lab8/articles')

@lab8.route('/lab8/logout')
@login_required
def logout():
    logout_user()
    return redirect('/lab8/')
