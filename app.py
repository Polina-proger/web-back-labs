from flask import Flask, url_for, request, redirect
import datetime
app = Flask(__name__)

@app.route("/")
@app.route("/lab1/web")
def web():
    return """<!doctype html>
        <html>
          <body>
             <h1>web-сервер на flask</h1>
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
                <a href="/web">web</a>
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
        <a href="/clear_counter">Очистить счётчик</a>
    </body>
</html> 
'''

@app.route('/clear_counter')
def clear_counter():
    global count
    count = 0
    return redirect('/counter')

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
    </body>
</html>     
''', 201

@app.errorhandler(404)
def not_found(err):
    return "нет такой страницы", 404
