from flask import render_template, request, session, make_response
from werkzeug.security import generate_password_hash
from time import strftime
from config import app
from models.user import User


class UsersController(object):

    @staticmethod
    @app.route('/users/admin')
    def admin():
        return render_template('users/admin.html')

    @staticmethod
    @app.route('/users/logout')
    def logout():
        session.pop('user', None)
        return render_template('users/logout.html')

    @staticmethod
    @app.route('/users/profile')
    def profile():
        return render_template('users/profile.html')

    @staticmethod
    @app.route('/users/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'GET':
            return render_template('users/register.html')
        elif request.method == 'POST':
            message = 'Регистрация провалена'
            mess_color = 'red'

            login = request.form.get('login')
            pass1 = request.form.get('pass1')
            pass2 = request.form.get('pass2')
            email = request.form.get('email')

            password = generate_password_hash(pass1)
            regdate = strftime('%Y-%m-%d %H:%M:%S')
            status = 'new_user'
            User.register(login, password, email, regdate, status)

            message = 'Регистрация прошла успешно'
            mess_color = 'green'
            return render_template('users/register_info.html', context={
                'message': message,
                'mess_color': mess_color
            })

    @staticmethod
    @app.route('/users/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return render_template('users/login.html')
        elif request.method == 'POST':
            message = 'Авторизация провалена'
            mess_color = 'red'

            login = request.form.get('login')
            pass1 = request.form.get('pass1')
            rem = request.form.get('rem')

            if User.auth(login, pass1):
                session['user'] = login  # Регистрация пользователя в сесии
                if rem == 'yes':
                    response = make_response('setting cookie user')
                    response.set_cookie('user', login, max_age=7*24*3600)
                message = 'Вы успешно авторизованы!'
                mess_color = 'green'
            else:
                message = 'Пользователь не найден!'
                mess_color = 'red'

            return render_template('users/login_info.html', context={
                'message': message,
                'mess_color': mess_color
            })
