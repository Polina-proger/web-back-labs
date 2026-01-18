from flask import Blueprint, render_template, url_for, redirect, request, make_response, session, current_app, abort

from flask.json import jsonify

lab7 = Blueprint('lab7', __name__)

@lab7.route('/lab7/')
def main():
    return render_template('lab7/index.html')

films = [
    {
        "id": 0,
        "title": "The Shawshank Redemption",
        "title_ru": "Побег из Шоушенка",
        "year": 1994,
        "description": "Два заключённых на протяжении многих лет находят утешение и в конечном итоге искупление через проявления обычной человеческой порядочности."
    },
    {
        "id": 1,
        "title": "Inception",
        "title_ru": "Начало",
        "year": 2010,
        "description": "Вор, крадущий корпоративные секреты с помощью технологии доступа к снам, получает обратную задачу — внедрить идею в сознание генерального директора."
    },
    {
        "id": 2,
        "title": "The Matrix",
        "title_ru": "Матрица",
        "year": 1999,
        "description": "Компьютерный хакер узнаёт от загадочных повстанцев об истинной природе своей реальности и своей роли в войне против её контролёров."
    },
    {
        "id": 3,
        "title": "The Lord of the Rings: The Return of the King",
        "title_ru": "Властелин колец: Возвращение короля",
        "year": 2003,
        "description": "Гэндальф и Арагорн ведут мир людей против армии Саурона, чтобы отвлечь его внимание от Фродо и Сэма, приближающихся к Роковой Горе с Единым Кольцом."
    },
    {
        "id": 4,
        "title": "Interstellar",
        "title_ru": "Интерстеллар",
        "year": 2014,
        "description": "Команда исследователей путешествует через червоточину в космосе в попытке обеспечить выживание человечества."
    },
]

@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    return jsonify(films)

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    for film in films:
        if film['id'] == id:
            return jsonify(film)
    abort(404)

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_film(id):
    for i, film in enumerate(films):
        if film['id'] == id:
            del films[i]
            return '', 204
    abort(404)

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_films(id):
    film_data = request.get_json()
    
    # Валидация
    errors = {}
    if not film_data.get('title_ru'):
        errors['title_ru'] = 'Название на русском обязательно'
    if not film_data.get('description'):
        errors['description'] = 'Описание обязательно'
    if not film_data.get('year'):
        errors['year'] = 'Год обязателен'
    elif not isinstance(film_data.get('year'), int) or film_data['year'] < 1888 or film_data['year'] > 2100:
        errors['year'] = 'Год должен быть числом от 1888 до 2100'
    
    if errors:
        return jsonify(errors), 400
    
    for i, film in enumerate(films):
        if film['id'] == id:
            film_data['id'] = id
            films[i] = film_data
            return jsonify(film_data)
    abort(404)

@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_films():
    film_data = request.get_json()
    
    # Валидация
    errors = {}
    if not film_data.get('title_ru'):
        errors['title_ru'] = 'Название на русском обязательно'
    if not film_data.get('description'):
        errors['description'] = 'Описание обязательно'
    if not film_data.get('year'):
        errors['year'] = 'Год обязателен'
    elif not isinstance(film_data.get('year'), int) or film_data['year'] < 1888 or film_data['year'] > 2100:
        errors['year'] = 'Год должен быть числом от 1888 до 2100'
    
    if errors:
        return jsonify(errors), 400
    
    # Находим максимальный id и увеличиваем на 1
    if films:
        new_id = max(film['id'] for film in films) + 1
    else:
        new_id = 0
    
    film_data['id'] = new_id
    films.append(film_data)
    return jsonify({"id": new_id})
