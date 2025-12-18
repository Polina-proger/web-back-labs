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
    