from flask import Blueprint, url_for, redirect, request, render_template, make_response
lab3 = Blueprint('lab3', __name__)

@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name')
    name_color = request.cookies.get('name_color')
    return render_template('lab3/lab3.html', name=name, name_color=name_color)

@lab3.route('/lab3/cookie')
def cookie():
    resp=make_response(redirect('/lab3/'))
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color', 'magenta')
    return resp

@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp = make_response(redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp

@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'

    age = request.args.get('age')
    sex = request.args.get('sex')
    return render_template('lab3/form1.html', user=user, age=age, sex=sex, errors=errors)

@lab3.route('/lab3/order')
def order():
    return render_template('lab3/order.html')

@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'coffee':
        price = 120
    elif drink =='black-tea':
        price = 80
    else:
        price = 70

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10
    return render_template('lab3/pay.html', price=price)

@lab3.route('/lab3/success')
def success():
    # Берем цену из параметров запроса (передается из формы оплаты)
    price = request.args.get('price', 0)
    return render_template('lab3/success.html', price=price)

@lab3.route('/lab3/settings')
def settings():
    color = request.args.get('color')
    bg_color = request.args.get('bg_color')
    font_size = request.args.get('font_size')
    
    if color or bg_color or font_size:
        resp = make_response(render_template('lab3/settings.html', 
        color=color or request.cookies.get('color'),
        bg_color=bg_color or request.cookies.get('bg_color'),
        font_size=font_size or request.cookies.get('font_size')))
        if color:
            resp.set_cookie('color', color)
        if bg_color:
            resp.set_cookie('bg_color', bg_color)
        if font_size:
            resp.set_cookie('font_size', font_size)
        return resp
    

    color = request.cookies.get('color')
    bg_color = request.cookies.get('bg_color')
    font_size = request.cookies.get('font_size')
    
    return render_template('lab3/settings.html', 
                         color=color, 
                         bg_color=bg_color, 
                         font_size=font_size)

@lab3.route('/lab3/ticket')
def ticket():
    errors = {}
    
    fio = request.args.get('fio')
    shelf = request.args.get('shelf')
    linen = request.args.get('linen') == 'on'
    luggage = request.args.get('luggage') == 'on'
    age_str = request.args.get('age')
    departure = request.args.get('departure')
    destination = request.args.get('destination')
    travel_date = request.args.get('travel_date')
    insurance = request.args.get('insurance') == 'on'
    
    form_submitted = any([fio, shelf, age_str, departure, destination, travel_date])
    
    if form_submitted:
        if not fio:
            errors['fio'] = 'Заполните ФИО пассажира'
        if not shelf:
            errors['shelf'] = 'Выберите полку'
        if not age_str:
            errors['age'] = 'Заполните возраст'
        elif not age_str.isdigit() or not (1 <= int(age_str) <= 120):
            errors['age'] = 'Возраст должен быть от 1 до 120 лет'
        if not departure:
            errors['departure'] = 'Заполните пункт выезда'
        if not destination:
            errors['destination'] = 'Заполните пункт назначения'
        if not travel_date:
            errors['travel_date'] = 'Выберите дату поездки'
        
        if errors:
            return render_template('lab3/ticket.html', 
                                 errors=errors,
                                 fio=fio,
                                 shelf=shelf,
                                 linen=linen,
                                 luggage=luggage,
                                 age=age_str,
                                 departure=departure,
                                 destination=destination,
                                 travel_date=travel_date,
                                 insurance=insurance,
                                 show_result=False)
        
        age = int(age_str)
        if age < 18:
            price = 700
        else:
            price = 1000
        
        if shelf in ['lower', 'side_lower']:
            price += 100
        if linen:
            price += 75
        if luggage:
            price += 250
        if insurance:
            price += 150
        
        return render_template('lab3/ticket.html',
                             fio=fio,
                             shelf=shelf,
                             linen=linen,
                             luggage=luggage,
                             age=age,
                             departure=departure,
                             destination=destination,
                             travel_date=travel_date,
                             insurance=insurance,
                             price=price)
    
    return render_template('lab3/ticket.html')

@lab3.route('/lab3/clear_settings')
def clear_settings():
    resp = make_response(redirect('/lab3/settings'))
    resp.delete_cookie('color')
    resp.delete_cookie('bg_color') 
    resp.delete_cookie('font_size')
    return resp

books = [
    {"title": "Токийский гуль", "price": 1500, "year": 2011, "author": "Сюи Исида"},
    {"title": "Атака титанов", "price": 1800, "year": 2009, "author": "Хадзимэ Исаяма"},
    {"title": "Наруто", "price": 1200, "year": 1999, "author": "Масаси Кисимото"},
    {"title": "Ван Пис", "price": 1400, "year": 1997, "author": "Эйитиро Ода"},
    {"title": "Блич", "price": 1100, "year": 2001, "author": "Тайто Кубо"},
    {"title": "Хантер х Хантер", "price": 950, "year": 1998, "author": "Ёсихиро Тогаси"},
    {"title": "Моб Психо 100", "price": 850, "year": 2012, "author": "ONE"},
    {"title": "Ванпанчмен", "price": 1000, "year": 2009, "author": "ONE"},
    {"title": "Джоджо: Невероятные приключения", "price": 1300, "year": 1987, "author": "Хирохико Араки"},
    {"title": "Евангелион", "price": 900, "year": 1995, "author": "Ёсиюки Садамото"},
    {"title": "Берсерк", "price": 1600, "year": 1989, "author": "Кэнтаро Миура"},
    {"title": "Стальной алхимик", "price": 1250, "year": 2001, "author": "Хирому Аракава"},
    {"title": "Драгонболл", "price": 1150, "year": 1984, "author": "Акира Торияма"},
    {"title": "Сейлор Мун", "price": 1350, "year": 1991, "author": "Наоко Такэути"},
    {"title": "Ковбой Бибоп", "price": 1050, "year": 1997, "author": "Ясухиро Найто"},
    {"title": "Тетрадь смерти", "price": 1450, "year": 2003, "author": "Цугуми Оба"},
    {"title": "Бакуман", "price": 950, "year": 2008, "author": "Цугуми Оба"},
    {"title": "Город, в котором меня нет", "price": 800, "year": 2012, "author": "Кэй Санабэ"},
    {"title": "Паразит", "price": 750, "year": 1988, "author": "Хитоси Ивааки"},
    {"title": "Акира", "price": 1700, "year": 1982, "author": "Кацухиро Отомо"},
    {"title": "Призрак в доспехах", "price": 1550, "year": 1989, "author": "Масамунэ Сиро"},
    {"title": "О моём перерождении в слизь", "price": 1100, "year": 2013, "author": "Фусэ"},
    {"title": "Восхождение героя щита", "price": 1200, "year": 2013, "author": "Анэко Юсаги"}
]

@lab3.route('/lab3/manga')
def manga():
    min_price_cookie = request.cookies.get('min_price', '')
    max_price_cookie = request.cookies.get('max_price', '')
    
    min_price_arg = request.args.get('min_price', min_price_cookie)
    max_price_arg = request.args.get('max_price', max_price_cookie)
    reset = request.args.get('reset')
    
    if reset:
        resp = make_response(redirect('/lab3/manga'))
        resp.delete_cookie('min_price')
        resp.delete_cookie('max_price')
        return resp
    
    min_price_all = min(book['price'] for book in books)
    max_price_all = max(book['price'] for book in books)
    
    filtered_books = books
    message = ""
    
    if min_price_arg or max_price_arg:
        try:
            min_price = int(min_price_arg) if min_price_arg else min_price_all
            max_price = int(max_price_arg) if max_price_arg else max_price_all
            
            if min_price > max_price:
                min_price, max_price = max_price, min_price
            
            filtered_books = [
                book for book in books
                if min_price <= book['price'] <= max_price
            ]
            
            count = len(filtered_books)
            if count == 0:
                message = "Не найдено ни одной манги в заданном диапазоне цен"
            else:
                message = f"Найдено манги: {count}"
                
            if min_price_arg or max_price_arg:
                resp = make_response(render_template('lab3/manga.html',
                    books=filtered_books,
                    min_price=min_price,
                    max_price=max_price,
                    min_price_all=min_price_all,
                    max_price_all=max_price_all,
                    message=message
                ))
                if min_price_arg:
                    resp.set_cookie('min_price', min_price_arg)
                if max_price_arg:
                    resp.set_cookie('max_price', max_price_arg)
                return resp
                
        except ValueError:
            message = "Ошибка: введите корректные числовые значения"
    
    return render_template('lab3/manga.html',
        books=filtered_books,
        min_price=min_price_arg,
        max_price=max_price_arg,
        min_price_all=min_price_all,
        max_price_all=max_price_all,
        message=message or f"Всего манги: {len(filtered_books)}"
    )
