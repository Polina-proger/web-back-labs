from flask import Blueprint, render_template, url_for, redirect, request, make_response, session, current_app, abort

lab7 = Blueprint('lab7', __name__)

@lab7.route('/lab7/')
def main():
    return render_template('lab7/index.html')

films = [
    {
        "title": "The Shawshank Redemption",
        "title_ru": "Побег из Шоушенка",
        "year": 1994,
        "description": "Два заключённых на протяжении многих лет находят утешение и в конечном итоге искупление через проявления обычной человеческой порядочности."
    },
    {
        "title": "Inception",
        "title_ru": "Начало",
        "year": 2010,
        "description": "Вор, крадущий корпоративные секреты с помощью технологии доступа к снам, получает обратную задачу — внедрить идею в сознание генерального директора."
    },
    {
        "title": "The Matrix",
        "title_ru": "Матрица",
        "year": 1999,
        "description": "Компьютерный хакер узнаёт от загадочных повстанцев об истинной природе своей реальности и своей роли в войне против её контролёров."
    },
    {
        "title": "The Lord of the Rings: The Return of the King",
        "title_ru": "Властелин колец: Возвращение короля",
        "year": 2003,
        "description": "Гэндальф и Арагорн ведут мир людей против армии Саурона, чтобы отвлечь его внимание от Фродо и Сэма, приближающихся к Роковой Горе с Единым Кольцом."
    },
    {
        "title": "Interstellar",
        "title_ru": "Интерстеллар",
        "year": 2014,
        "description": "Команда исследователей путешествует через червоточину в космосе в попытке обеспечить выживание человечества."
    },
]

@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    return films

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    if id < 0 or id >= len(films):
        abort(404)
    return films[id]

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_film(id):
    if id < 0 or id >= len(films):
        abort(404)
    del films[id]
    return '', 204

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_films(id):  
    film = request.get_json()
    films[id] = film
    return films[id]


