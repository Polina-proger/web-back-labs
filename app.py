from flask import Flask, url_for, request, redirect, abort, render_template, render_template_string
import datetime
import os
from db.models import db, User
from os import path
from flask_login import LoginManager

from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from lab7 import lab7
from lab8 import lab8

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'secret-key-change-this-in-production')
app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'postgres')

if app.config['DB_TYPE'] == 'postgres':
    db_name = 'polina_selikhova_orm'
    db_user = 'polina_selikhova_orm'
    db_password = '123'
    host_ip = '127.0.0.1'
    host_port = 5432

    app.config['SQLALCHEMY_DATABASE_URI'] = \
        f'postgresql://{db_user}:{db_password}@{host_ip}:{host_port}/{db_name}'
else:
    dir_path = path.dirname(path.realpath(__file__))
    db_path = path.join(dir_path, "polina_selikhova_orm.db")
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'lab8.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# УДАЛИТЬ эту строку - она вызывает проблему с существующими таблицами
# with app.app_context():
#     db.create_all()

app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)
app.register_blueprint(lab8)

@app.route("/")
def start():
    html_content = """
{% extends "base.html" %}

{% block lab %}Главная страница{% endblock %}

{% block main %}
    <header>
        <h1>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</h1>
    </header>
    
    <main>
        <ul>
            <li><a href="/lab1">Первая лабораторная</a></li>
            <li><a href="/lab2/">Вторая лабораторная</a></li>
            <li><a href="/lab3/">Третья лабораторная</a></li>
            <li><a href="/lab4/">Четвертая лабораторная</a></li>
            <li><a href="/lab5/">Пятая лабораторная</a></li>
            <li><a href="/lab6/">Шестая лабораторная</a></li>
            <li><a href="/lab7/">Седьмая лабораторная</a></li>
            <li><a href="/lab8/">Восьмая лабораторная</a></li>
            <li><a href="/lab9/">Девятая лабораторная</a></li>
        </ul>
    </main>
    
    <footer>
        <hr>
        <p>Селихова Полина Сергеевна, ФБИ-33, 3 курс, 2025</p>
    </footer>
{% endblock %}
    """
    return render_template_string(html_content)


@app.errorhandler(500)
def internal_server_error(err):
    css_url = url_for('static', filename='lab1/lab1.css')
    return f'''
<!doctype html>
<html>
    <head>
        <title>Ошибка сервера</title>
        <link rel="stylesheet" href="{css_url}">
    </head>
    <body class="error-500-body">
        <div class="error-container">
            <div class="error-code">500</div>
            <div class="error-message">
                Внутренняя ошибка сервера
            </div>
            <div class="error-description">
                <p><strong>Что случилось?</strong></p>
                <p>На сервере произошла непредвиденная ошибка. Это может быть вызвано:</p>
                <ul>
                    <li>Ошибкой в коде приложения</li>
                    <li>Проблемами с базой данных</li>
                    <li>Недостатком ресурсов сервера</li>
                </ul>
                <p>Мы уже работают над устранением проблемы. Пожалуйста, попробуйте позже.</p>
            </div>
            <a href="/" class="back-link">Вернуться на главную</a>
            <a href="/lab1" class="back-link" style="margin-left: 10px;">К лабораторной работе</a>
        </div>
    </body>
</html>
''', 500


@app.errorhandler(404)
def not_found(err):
    client_ip = request.remote_addr
    access_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    requested_url = request.url
    
    log_entry = {
        'ip': client_ip,
        'time': access_time,
        'url': requested_url
    }
    access_log.append(log_entry)
    
    css_url = url_for('static', filename='lab1/lab1.css')
    image_url = url_for('static', filename='lab1/404.jpg')
    
    log_html = ""
    for entry in access_log:
        log_html += f'<li>[{entry["time"]}, пользователь {entry["ip"]}] зашёл на адрес: <br>{entry["url"]}</li>'
    
    return f'''
<!doctype html>
<html>
    <head>
        <title>Страница не найдена</title>
        <link rel="stylesheet" href="{css_url}">
        <style>
            .access-info {{
                background-color: #e9ecef;
                padding: 15px;
                border-radius: 5px;
                margin: 20px 0;
            }}
            .journal {{
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 5px;
                padding: 20px;
                margin-top: 30px;
            }}
            .journal h3 {{
                color: #495057;
                border-bottom: 2px solid #007bff;
                padding-bottom: 10px;
            }}
            .journal ul {{
                list-style-type: none;
                padding-left: 0;
            }}
            .journal li {{
                padding: 8px 0;
                border-bottom: 1px solid #e9ecef;
            }}
            .journal li:last-child {{
                border-bottom: none;
            }}
        </style>
    </head>
    <body class="error-404-body">
        <div class="error-container">
            <div class="error-code">404</div>
            <div class="error-message">
                Упс! Похоже, эта страница отправилась в космическое путешествие<br>
                и не вернулась обратно
            </div>
            
            <div class="access-info">
                <h3>Информация о вашем запросе:</h3>
                <p><strong>Ваш IP-адрес:</strong> {client_ip}</p>
                <p><strong>Дата и время доступа:</strong> {access_time}</p>
                <p><strong>Запрошенный адрес:</strong> {requested_url}</p>
            </div>
            
            <img src="{image_url}" alt="Страница не найдена" class="error-image">
            
            <div class="suggestions">
                <p>Возможно, вы искали одну из этих страниц:</p>
                <a href="/" class="back-link">Главная страница</a>
                <a href="/lab1" class="back-link" style="margin-left: 10px;">Лабораторная 1</a>
            </div>
            
            <div class="journal">
                <h3>Журнал обращений к несуществующим страницам:</h3>
                <ul>
                    {log_html}
                </ul>
            </div>
        </div>
    </body>
</html>
''', 404

access_log = []

if __name__ == '__main__':
    app.run(debug=True)
    