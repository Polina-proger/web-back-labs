from flask import Flask, url_for, request, redirect, abort, render_template
import datetime

app = Flask(__name__)

# Глобальный список для хранения логов
access_log = []

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
            <li><a href="/lab2/">Вторая лабораторная</a></li>
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
    <p>Flask — фреймворк для создания веб-приложений на языке
программирования Python, использующий набор инструментов
Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
называемых микрофреймворков — минималистичных каркасов
веб-приложений, сознательно предоставляющих лишь самые ба-
зовые возможности.</p>
    
    <ul>
        <li><a href="/lab1/web">web</a></li>
        <li><a href="/lab1/author">author</a></li>
        <li><a href="/lab1/image">image</a></li>
        <li><a href="/lab1/counter">counter</a></li>
        <li><a href="/lab1/info">info</a></li>
        <li><a href="/lab1/created">created</a></li>
        <li><a href="/lab1/error">error (вызвать ошибку 500)</a></li>
    </ul>

    <h2>Коды ответов HTTP:</h2>
    <ul>
        <li><a href="/lab1/400">400 Bad Request</a></li>
        <li><a href="/lab1/401">401 Unauthorized</a></li>
        <li><a href="/lab1/402">402 Payment Required</a></li>
        <li><a href="/lab1/403">403 Forbidden</a></li>
        <li><a href="/lab1/405">405 Method Not Allowed</a></li>
        <li><a href="/lab1/418">418 I'm a teapot</a></li>
    </ul>

    <h2>Список роутов</h2>
    <ul>
        <li><a href="/">/</a></li>
        <li><a href="/index">/index</a></li>
        <li><a href="/lab1">/lab1</a></li>
        <li><a href="/lab1/web">/lab1/web</a></li>
        <li><a href="/lab1/author">/lab1/author</a></li>
        <li><a href="/lab1/image">/lab1/image</a></li>
        <li><a href="/lab1/counter">/lab1/counter</a></li>
        <li><a href="/lab1/clear_counter">/lab1/clear_counter</a></li>
        <li><a href="/lab1/info">/lab1/info</a></li>
        <li><a href="/lab1/created">/lab1/created</a></li>
        <li><a href="/lab1/error">/lab1/error</a></li>
        <li><a href="/lab1/400">/lab1/400</a></li>
        <li><a href="/lab1/401">/lab1/401</a></li>
        <li><a href="/lab1/402">/lab1/402</a></li>
        <li><a href="/lab1/403">/lab1/403</a></li>
        <li><a href="/lab1/405">/lab1/405</a></li>
        <li><a href="/lab1/418">/lab1/418</a></li>
    </ul>
    
    <a href="/">Назад</a>
</body>
</html>"""

# Обработчик, вызывающий ошибку 500
@app.route("/lab1/error")
def server_error():
    # Вызываем ошибку деления на ноль
    result = 10 / 0
    return "Эта строка никогда не выполнится"

@app.route("/lab1/400")
def bad_request():
    return '''
<!doctype html>
<html>
    <body>
        <h1>400 Bad Request</h1>
        <p>Сервер не может обработать запрос из-за клиентской ошибки (неправильный синтаксис, неверный формат и т.д.)</p>
        <a href="/lab1">Назад</a>
    </body>
</html>
''', 400

@app.route("/lab1/401")
def unauthorized():
    return '''
<!doctype html>
<html>
    <body>
        <h1>401 Unauthorized</h1>
        <p>Требуется аутентификация для доступа к ресурсу</p>
        <a href="/lab1">Назад</a>
    </body>
</html>
''', 401

@app.route("/lab1/402")
def payment_required():
    return '''
<!doctype html>
<html>
    <body>
        <h1>402 Payment Required</h1>
        <p>Требуется оплата для доступа к ресурсу (зарезервировано для будущего использования)</p>
        <a href="/lab1">Назад</a>
    </body>
</html>
''', 402

@app.route("/lab1/403")
def forbidden():
    return '''
<!doctype html>
<html>
    <body>
        <h1>403 Forbidden</h1>
        <p>Доступ к запрошенному ресурсу запрещен</p>
        <a href="/lab1">Назад</a>
    </body>
</html>
''', 403

@app.route("/lab1/405")
def method_not_allowed():
    return '''
<!doctype html>
<html>
    <body>
        <h1>405 Method Not Allowed</h1>
        <p>Метод запроса не поддерживается для данного ресурса</p>
        <a href="/lab1">Назад</a>
    </body>
</html>
''', 405

@app.route("/lab1/418")
def teapot():
    return '''
<!doctype html>
<html>
    <body>
        <h1>418 I'm a teapot</h1>
        <p>Я - чайник (шутливый код из RFC 2324)</p>
        <a href="/lab1">Назад</a>
    </body>
</html>
''', 418

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
            'Content-Type': 'text/plain; charset=utf-8'
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
''', 200, {
    'Content-Language': 'ru',
    'X-Student-Name': 'Selikhova Polina',
    'X-Lab-Number': '1',
    'X-Custom-Header': 'Flask-Image-Processor'
}

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

# Обработчик ошибки 500
@app.errorhandler(500)
def internal_server_error(err):
    css_url = url_for('static', filename='lab1.css')
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
                <p>Мы уже работаем над устранением проблемы. Пожалуйста, попробуйте позже.</p>
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
    
    css_url = url_for('static', filename='lab1.css')
    
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
            
            <img src="/static/404.jpg" alt="Страница не найдена" class="error-image">
            
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

@app.route('/lab2/a')
def a():
    return 'без слэша'

@app.route('/lab2/a/')
def a2():
    return 'со слэшем'

flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']

@app.route('/lab2/add_flower/')
@app.route('/lab2/add_flower/<name>')
def add_flower(name=None):
    if name is None:
        return 'вы не задали имя цветка', 400
    
    flower_list.append(name)
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Добавлен новый цветок</h1>
    <p>Название нового цветка: {name}</p>
    <p>Всего цветов: {len(flower_list)}<p>
    <p>Полный список: {flower_list}</p>
    </body>
 </html>   
'''

@app.route('/lab2/flowers')
def show_flowers():
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Список цветов</h1>
    <p>Всего цветов: {len(flower_list)}</p>
    <ul>
        {"".join(f"<li>{flower}</li>" for flower in flower_list)}
    </ul>
    </body>
</html>
'''

@app.route('/lab2/example')
def example():
    name, n_lab, group, n_course = 'Селихова Полина', '2', 'ФБИ-33', '3 курс'
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}
    ]
    return render_template('example.html', name=name, 
                           n_lab=n_lab, group=group, 
                           n_course=n_course, fruits=fruits)

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/filters')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filter.html', phrase=phrase)

@app.route('/lab2/flowers/<int:flower_id>')
def show_flower(flower_id):
    if flower_id < 0 or flower_id >= len(flower_list):
                return f'''
<!doctype html>
<html>
    <body>
    <h1>Ошибка</h1>
    <p><a>Цветок с ID {flower_id} не найден</a></p>
    <p><a href="/lab2/flowers">Вернуться к списку всех цветов</a></p>
    </body>
</html>
''', 404
    
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Информация о цветке</h1>
    <p>ID: {flower_id}</p>
    <p>: {flower_list[flower_id]}</p>
    <p><a href="/lab2/flowers">Вернуться к списку всех цветов</a></p>
    </body>
</html>
'''

@app.route('/lab2/clear_flowers')
def clear_flowers():
    flower_list.clear()
    return '''
<!doctype html>
<html>
    <body>
    <h1>Список цветов очищен</h1>
    <p>Все цветы были удалены из списка</p>
    <p><a href="/lab2/flowers">Перейти к списку всех цветов</a></p>
    </body>
</html>
'''

@app.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Расчёт с параметрами:</h1>
    <p>
        {a} + {b} = {a + b}<br>
        {a} - {b} = {a - b}<br>
        {a} × {b} = {a * b}<br>
        {a} / {b} = {a / b}<br>
        {a}<sup>{b}</sup> = {a ** b}
    </p>
    </body>
</html>   
'''

@app.route('/lab2/calc/')
def lab2_calc():
    return redirect('/lab2/calc/1/1')

@app.route('/lab2/calc/<int:a>')
def lab2_calc2(a):
    return redirect(f'/lab2/calc/{a}/1')

books = [
    {"author": "Фёдор Достоевский", "title": "Преступление и наказание", "genre": "Роман", "pages": 671},
    {"author": "Лев Толстой", "title": "Война и мир", "genre": "Роман-эпопея", "pages": 1225},
    {"author": "Михаил Булгаков", "title": "Мастер и Маргарита", "genre": "Фантастика", "pages": 480},
    {"author": "Антон Чехов", "title": "Рассказы", "genre": "Рассказы", "pages": 350},
    {"author": "Александр Пушкин", "title": "Евгений Онегин", "genre": "Роман в стихах", "pages": 240},
    {"author": "Николай Гоголь", "title": "Мёртвые души", "genre": "Поэма", "pages": 352},
    {"author": "Иван Тургенев", "title": "Отцы и дети", "genre": "Роман", "pages": 288},
    {"author": "Александр Островский", "title": "Гроза", "genre": "Драма", "pages": 120},
    {"author": "Михаил Лермонтов", "title": "Герой нашего времени", "genre": "Роман", "pages": 224},
    {"author": "Николай Лесков", "title": "Левша", "genre": "Повесть", "pages": 96}
]

@app.route('/lab2/books')
def lab2_books():
    return render_template('books.html', books=books)

berries = [
    {"name": "Клубника", "description": "Сладкая красная ягода", "image": "Клубника.jpg"},
    {"name": "Малина", "description": "Ароматная ягода розового цвета", "image": "Малина.jpg"},
    {"name": "Черника", "description": "Маленькая синяя ягода с антиоксидантами", "image": "Черника.jpg"},
    {"name": "Ежевика", "description": "Тёмная ягода с насыщенным вкусом", "image": "Ежевика.jpg"},
    {"name": "Смородина", "description": "Бывает красная, черная и белая", "image": "Смородина.jpg"},
    {"name": "Клюква", "description": "Кислая ягода, растущая на болотах", "image": "Клюква.jpg"},
    {"name": "Брусника", "description": "Красная ягода с горьковатым вкусом", "image": "Брусника.jpg"},
    {"name": "Земляника", "description": "Лесная ягода с насыщенным ароматом", "image": "Земляника.jpg"},
    {"name": "Голубика", "description": "Крупная синяя ягода", "image": "Голубика.jpg"},
    {"name": "Облепиха", "description": "Оранжевая ягода с высоким содержанием витаминов", "image": "Облепиха.jpg"},
    {"name": "Виноград", "description": "Сочные ягоды, растущие гроздьями", "image": "Виноград.jpg"},
    {"name": "Крыжовник", "description": "Зелёная ягода с кисло-сладким вкусом", "image": "Крыжовник.jpg"},
    {"name": "Шиповник", "description": "Плоды розы, богатые витамином C", "image": "Шиповник.jpg"},
    {"name": "Рябина", "description": "Красные горьковатые ягоды", "image": "Рябина.jpg"},
    {"name": "Калина", "description": "Красные ягоды с косточкой", "image": "Калина.jpg"},
    {"name": "Ирга", "description": "Сладкие синие ягоды", "image": "Ирга.jpg"},
    {"name": "Жимолость", "description": "Синие продолговатые ягоды", "image": "Жимолость.jpg"},
    {"name": "Боярышник", "description": "Красные ягоды с лечебными свойствами", "image": "Боярышник.jpg"},
    {"name": "Арония", "description": "Черноплодная рябина", "image": "Арония.jpg"},
    {"name": "Морошка", "description": "Янтарная ягода севера", "image": "Морошка.jpg"}
]

@app.route('/lab2/berries')
def show_berries():
    berries_html = ""
    for berry in berries:  
        berries_html += f'''
        <div class="berry-item">
            <img src="/static/{berry['image']}" alt="{berry['name']}" style="width: 150px; height: 150px; object-fit: cover;">
            <h3>{berry['name']}</h3>
            <p>{berry['description']}</p>
        </div>
        '''
    
    return f'''
<!doctype html>
<html>
<head>
    <title>Ягоды</title>
    <style>
        .berries-container {{
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
        }}
        .berry-item {{
            width: 200px;
        }}
    </style>
</head>
<body>
    <h1>Разновидности ягод</h1>
    <div class="berries-container">
        {berries_html}
    </div>
</body>
</html>
'''
