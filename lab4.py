from flask import Blueprint, render_template, url_for, redirect, request, make_response, session
lab4 = Blueprint('lab4', __name__)


@lab4.route('/lab4/')
def lab():
    return render_template('lab4/lab4.html')

@lab4.route('/lab4/div-form')
def div_form():
    return render_template('lab4/div-form.html')

@lab4.route('/lab4/div', methods = ['POST'])
def div():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    
    if x1 == '' or x2 == '':
        return render_template('lab4/div.html', error='Оба поля должны быть заполнены!')
    
    try:
        x1 = float(x1)
        x2 = float(x2)
        
        # Проверка деления на ноль
        if x2 == 0:
            return render_template('lab4/div.html', error='Ошибка: деление на ноль невозможно!')
        
        result = x1 / x2
        return render_template('lab4/div.html', x1=x1, x2=x2, result=result)
    
    except ValueError:
        return render_template('lab4/div.html', error='Ошибка: введите числа!')

@lab4.route('/lab4/sum-form')
def sum_form():
    return render_template('lab4/sum-form.html')

@lab4.route('/lab4/sum', methods=['POST'])
def sum():
    x1 = request.form.get('x1', '0')
    x2 = request.form.get('x2', '0')
    
    x1 = int(x1) if x1 != '' else 0
    x2 = int(x2) if x2 != '' else 0
    
    result = x1 + x2
    return render_template('lab4/sum.html', x1=x1, x2=x2, result=result)

@lab4.route('/lab4/mul-form')
def mul_form():
    return render_template('lab4/mul-form.html')

@lab4.route('/lab4/mul', methods=['POST'])
def mul():
    x1 = request.form.get('x1', '1')
    x2 = request.form.get('x2', '1') 
    
    x1 = int(x1) if x1 != '' else 1
    x2 = int(x2) if x2 != '' else 1
    
    result = x1 * x2
    return render_template('lab4/mul.html', x1=x1, x2=x2, result=result)

@lab4.route('/lab4/sub-form')
def sub_form():
    return render_template('lab4/sub-form.html')

@lab4.route('/lab4/sub', methods=['POST'])
def sub():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    
    if x1 == '' or x2 == '':
        return render_template('lab4/sub.html', x1=x1, x2=x2, error='Оба поля должны быть заполнены!')
    
    x1 = int(x1)
    x2 = int(x2)
    
    result = x1 - x2
    return render_template('lab4/sub.html', x1=x1, x2=x2, result=result)

@lab4.route('/lab4/pow-form')
def pow_form():
    return render_template('lab4/pow-form.html')

@lab4.route('/lab4/pow', methods=['POST'])
def power():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    
    if x1 == '' or x2 == '':
        return render_template('lab4/pow.html', x1=x1, x2=x2, error='Оба поля должны быть заполнены!')
    
    x1 = int(x1)
    x2 = int(x2)
    
    if x1 == 0 and x2 == 0:
        return render_template('lab4/pow.html', x1=x1, x2=x2, error='Ноль в нулевой степени не определен!')
    
    result = x1 ** x2
    return render_template('lab4/pow.html', x1=x1, x2=x2, result=result)

tree_count = 0
max_trees = 10

@lab4.route('/lab4/tree', methods = ['GET', 'POST'])
def tree():
    global tree_count
    if request.method == 'GET':
        return render_template('lab4/tree.html', tree_count=tree_count, max_trees=max_trees)
    operation = request.form.get('operation')

    if operation == 'cut':
        if tree_count > 0:  
            tree_count -= 1
    elif operation == 'plant':
        if tree_count < max_trees:
            tree_count += 1
    
    return redirect('/lab4/tree')

users = [
    {'login': 'alex', 'password': '123', 'name': 'Александр Петров', 'gender': 'М'},
    {'login': 'bob', 'password': '555', 'name': 'Борис Иванов', 'gender': 'М'},
    {'login': 'polly', 'password': '777', 'name': 'Полина Селихова', 'gender': 'Ж'},
    {'login': 'gog', 'password': '333', 'name': 'Георгий Смирнов', 'gender': 'М'},
]

@lab4.route('/lab4/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'login' in session:
            authorized = True
            # Получаем имя пользователя для приветствия
            for user in users:
                if user['login'] == session['login']:
                    name = user['name']
                    break
            return render_template('lab4/login.html', authorized=authorized, name=name)
        else:
            return render_template('lab4/login.html', authorized=False)
    
    login = request.form.get('login')
    password = request.form.get('password')

    # Проверка на пустые значения
    errors = []
    if not login:
        errors.append('Не введён логин')
    if not password:
        errors.append('Не введён пароль')
    
    if errors:
        return render_template('lab4/login.html', authorized=False, 
                             errors=errors, login=login)

    for user in users:
        if login == user['login'] and password == user['password']:
            session['login'] = login
            session['name'] = user['name']
            return redirect('/lab4/login')

    error = 'Неверные логин и/или пароль'
    return render_template('lab4/login.html', authorized=False, 
                         login=login, errors=[error])

@lab4.route('/lab4/logout', methods=['POST'])  # Только POST
def logout():
    session.pop('login', None)
    session.pop('name', None)
    return redirect('/lab4/login')

@lab4.route('/lab4/fridge', methods=['GET', 'POST'])
def fridge():
    if request.method == 'GET':
        return render_template('lab4/fridge.html')
    
    temperature = request.form.get('temperature')
    
    if not temperature:
        return render_template('lab4/fridge.html', error='Ошибка: не задана температура')
    
    try:
        temp = int(temperature)
    except ValueError:
        return render_template('lab4/fridge.html', error='Ошибка: температура должна быть числом')
    
    if temp < -12:
        return render_template('lab4/fridge.html', error='Не удалось установить температуру — слишком низкое значение')
    
    if temp > -1:
        return render_template('lab4/fridge.html', error='Не удалось установить температуру — слишком высокое значение')
    
    snowflakes = ''
    if -12 <= temp <= -9:
        snowflakes = '***'
    elif -8 <= temp <= -5:
        snowflakes = '**'
    elif -4 <= temp <= -1:
        snowflakes = '*'
    
    return render_template('lab4/fridge.html', temperature=temp, snowflakes=snowflakes)

@lab4.route('/lab4/grain', methods=['GET', 'POST'])
def grain():
    if request.method == 'GET':
        return render_template('lab4/grain.html')
    
    grain_type = request.form.get('grain_type')
    weight = request.form.get('weight')
    
    if not weight:
        return render_template('lab4/grain.html', error='Ошибка: не указан вес')
    
    try:
        weight_float = float(weight)
    except ValueError:
        return render_template('lab4/grain.html', error='Ошибка: вес должен быть числом')
    
    if weight_float <= 0:
        return render_template('lab4/grain.html', error='Ошибка: вес должен быть положительным числом')
    
    if weight_float > 100:
        return render_template('lab4/grain.html', error='Такого объёма сейчас нет в наличии')
    
    prices = {
        'barley': 12000,
        'oats': 8500,
        'wheat': 9000,
        'rye': 15000
    }
    
    grain_names = {
        'barley': 'ячмень',
        'oats': 'овёс', 
        'wheat': 'пшеница',
        'rye': 'рожь'
    }
    
    price_per_ton = prices.get(grain_type)
    grain_name = grain_names.get(grain_type)
    
    total = weight_float * price_per_ton
    
    discount = 0
    if weight_float > 10:
        discount = total * 0.1
        total -= discount
    
    return render_template('lab4/grain.html', success=True, grain_name=grain_name, 
        weight=weight_float, total=total, discount=discount)

@lab4.route('/lab4/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab4/register.html')
    
    login = request.form.get('login')
    password = request.form.get('password')
    password_confirm = request.form.get('password_confirm')
    name = request.form.get('name')
    
    if not login or not password or not password_confirm or not name:
        return render_template('lab4/register.html', error='Все поля должны быть заполнены')
    
    if password != password_confirm:
        return render_template('lab4/register.html', error='Пароли не совпадают')
    
    for user in users:
        if user['login'] == login:
            return render_template('lab4/register.html', error='Пользователь с таким логином уже существует')
    
    users.append({
        'login': login,
        'password': password,
        'name': name,
        'gender': 'male'
    })
    
    return render_template('lab4/register.html', success='Регистрация успешна')

@lab4.route('/lab4/users')
def users_list():
    if 'login' not in session:
        return redirect('/lab4/login')
    
    current_user_login = session['login']
    return render_template('lab4/users.html', users=users, current_user_login=current_user_login)

@lab4.route('/lab4/delete_user', methods=['POST'])
def delete_user():
    if 'login' not in session:
        return redirect('/lab4/login')
    
    current_user_login = session['login']
    
    for i, user in enumerate(users):
        if user['login'] == current_user_login:
            users.pop(i)
            session.pop('login', None)
            return redirect('/lab4/login')
    
    return redirect('/lab4/users')

@lab4.route('/lab4/edit_user', methods=['GET', 'POST'])
def edit_user():
    if 'login' not in session:
        return redirect('/lab4/login')
    
    current_user_login = session['login']
    current_user = None
    
    for user in users:
        if user['login'] == current_user_login:
            current_user = user
            break
    
    if not current_user:
        return redirect('/lab4/login')
    
    if request.method == 'GET':
        return render_template('lab4/edit_user.html', user=current_user)
    
    new_login = request.form.get('login')
    new_name = request.form.get('name')
    new_password = request.form.get('password')
    password_confirm = request.form.get('password_confirm')
    
    if not new_login or not new_name:
        return render_template('lab4/edit_user.html', user=current_user, error='Логин и имя обязательны')
    
    if new_login != current_user_login:
        for user in users:
            if user['login'] == new_login and user != current_user:
                return render_template('lab4/edit_user.html', user=current_user, error='Пользователь с таким логином уже существует')
    
    if new_password:
        if new_password != password_confirm:
            return render_template('lab4/edit_user.html', user=current_user, error='Пароли не совпадают')
        current_user['password'] = new_password
    
    current_user['login'] = new_login
    current_user['name'] = new_name
    session['login'] = new_login
    
    return render_template('lab4/edit_user.html', user=current_user, success='Данные успешно обновлены')
   