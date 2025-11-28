from flask import Blueprint, url_for, redirect, request, render_template, abort

lab2 = Blueprint('lab2', __name__)
import datetime


@lab2.route('/lab2/a')
def a():
    return 'без слэша'


@lab2.route('/lab2/a/')
def a2():
    return 'со слэшем'


flower_list = [
    {"name": "роза", "price": 300},
    {"name": "тюльпан", "price": 200},
    {"name": "незабудка", "price": 200},
    {"name": "ромашка", "price": 100}
]

@lab2.route('/lab2/del_flower/<int:flower_id>')
def del_flower(flower_id):
    if flower_id < 0 or flower_id >= len(flower_list):
        abort(404)
    
    flower_list.pop(flower_id)
    return redirect(url_for('lab2.show_flowers'))  


@lab2.route('/lab2/add_flower/')
@lab2.route('/lab2/add_flower/<name>')
def add_flower(name=None):
    # Если имя передано как параметр URL
    if name is not None:
        base_price = 300
        flower_list.append({"name": name, "price": base_price})  # Исправлено: append вместо lab2end
        return redirect(url_for('lab2.show_flowers'))  # Исправлено
    
    # Если имя передано через параметр запроса (форма)
    name_from_form = request.args.get('name')
    if name_from_form:
        base_price = 300 + (len(flower_list) % 4) * 10
        flower_list.append({"name": name_from_form, "price": base_price})  # Исправлено: append вместо lab2end
        return redirect(url_for('lab2.show_flowers'))  # Исправлено
    
    # Если имя не задано
    return 'вы не задали имя цветка', 400


@lab2.route('/lab2/flowers')
def show_flowers():
    return render_template('lab2/flowers.html', flower_list=flower_list)


@lab2.route('/lab2/example')
def example():
    name, n_lab, group, n_course = 'Селихова Полина', '2', 'ФБИ-33', '3 курс'
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}
    ]
    return render_template('lab2/example.html', name=name, 
                           n_lab=n_lab, group=group, 
                           n_course=n_course, fruits=fruits)


@lab2.route('/lab2/')
def lab2_page():
    return render_template('lab2.html')


@lab2.route('/lab2/filters')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('lab2/filter.html', phrase=phrase)


@lab2.route('/lab2/flowers/<int:flower_id>')
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
    # Добавьте возврат цветка если он найден
    flower = flower_list[flower_id]
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Информация о цветке</h1>
    <p>ID: {flower_id}</p>
    <p>Название: {flower['name']}</p>
    <p>Цена: {flower['price']} руб</p>
    <p><a href="/lab2/flowers">Вернуться к списку всех цветов</a></p>
    </body>
</html>
'''


@lab2.route('/lab2/clear_flowers')
def clear_flowers():
    flower_list.clear()
    return redirect(url_for('lab2.show_flowers')) 


@lab2.route('/lab2/calc/<int:a>/<int:b>')
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


@lab2.route('/lab2/calc/')
def lab2_calc():
    return redirect('/lab2/calc/1/1')


@lab2.route('/lab2/calc/<int:a>')
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

@lab2.route('/lab2/books')
def lab2_books():
    return render_template('lab2/books.html', books=books)

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

@lab2.route('/lab2/berries')
def show_berries():
    berries_html = ""
    for berry in berries:  
        berries_html += f'''
        <div class="berry-item">
            <img src="/static/lab2/{berry['image']}" alt="{berry['name']}" style="width: 150px; height: 150px; object-fit: cover;">
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
