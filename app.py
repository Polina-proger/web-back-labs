from flask import Flask, url_for, request, redirect
import datetime
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return """<!doctype html>
<html>
<head>
    <title>НГТУ, ФБ, Лабораторные работы</title>
</head>
<body>
    <header>
        <h1>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</h1>
    </header>
    
    <main>
        <ul>
            <li><a href="/lab1">Первая лабораторная</a></li>
        </ul>
    </main>
    
    <footer>
        <hr>
        <p>Селихова Полина Сергеевна, ФБИ-33, 3 курс, 2025</p>
    </footer>
</body>
</html>"""

@app.route("/lab1")
def lab1():
    return """<!doctype html>
<html>
<head>
    <title>Лабораторная 1</title>
</head>
<body>
    <h1>Лабораторная работа 1</h1>
    <ul>
        <li><a href="/lab1/web">web</a></li>
        <li><a href="/lab1/author">author</a></li>
        <li><a href="/lab1/image">image</a></li>
        <li><a href="/lab1/counter">counter</a></li>
        <li><a href="/lab1/info">info</a></li>
        <li><a href="/lab1/created">created</a></li>
    </ul>
    <a href="/">Назад</a>
</body>
</html>"""

@app.route("/lab1/web")
def web():
    return """<!doctype html>
        <html>
          <body>
             <h1>web-сервер на flask</h1>
             <a href="/lab1">Назад</a>
         </body>
        </html>""", 200, {
            'X-Server': 'sample',
            'Content-Type': 'text/plain: charset=utf-8'
        }

@app.route("/lab1/author")
def author():
    name = "Селихова Полина Сергеевна"
    group = "ФБИ-33"
    faculty = "ФБ"

    return """<!doctype html>
        <html>
            <body>
                <p>Студент: """ + name + """</p>
                <p>Группа: """ + group + """</p>
                <p>Факультет: """ + faculty + """</p>
                <a href="/lab1">Назад</a>
            </body>
        </html>"""

@app.route("/lab1/image")
def image():
    css_url = url_for('static', filename='lab1.css')
    img_url = url_for('static', filename='oak.jpg')
    return f'''
<!doctype html>
<html>
    <head>
        <title>Стилизованная картинка</title>
        <link rel="stylesheet" href="{css_url}">
    </head>
    <body>
        <h1>Стилизованный дуб</h1>
        <img src="{img_url}" alt="Дуб" class="styled-image">
        <br>
        <a href="/lab1">Назад</a>
    </body>
</html> 
'''

count = 0

@app.route('/lab1/counter')
def counter():
    global count
    count += 1
    time = datetime.datetime.today()
    url = request.url
    client_ip = request.remote_addr

    return '''
<!doctype html>
<html>
    <body>
        Сколько раз вы сюда заходили: ''' + str(count) + '''
        <hr>
        Дата и время: ''' + str(time) + '''<br>
        Запрошенный адрес: ''' + str(url) + '''<br>
        Ваш IP адрес: ''' + str(client_ip) + '''<br>
        <a href="/lab1/clear_counter">Очистить счётчик</a><br>
        <a href="/lab1">Назад</a>
    </body>
</html> 
'''

@app.route('/lab1/clear_counter')
def clear_counter():
    global count
    count = 0
    return redirect('/lab1/counter')

@app.route("/lab1/info")
def info():
    return redirect("/lab1/author")

@app.route("/lab1/created")
def created():
    return '''
<!doctype html>
<html>
    <body>
        <h1>Создано успешно</h1>
        <div><i>что-то создано...</i></div>
        <a href="/lab1">Назад</a>
    </body>
</html>     
''', 201

@app.errorhandler(404)
def not_found(err):
    return "нет такой страницы", 404
