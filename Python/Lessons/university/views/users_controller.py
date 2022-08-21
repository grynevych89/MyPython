from flask import render_template
from config import app


class UsersController(object):

    @staticmethod
    @app.route('/users/admin')
    def admin():
        return render_template('users/admin.html')

    @staticmethod
    @app.route('/users/login')
    def login():
        return render_template('users/login.html')

    @staticmethod
    @app.route('/users/logout')
    def logout():
        return render_template('users/logout.html')

    @staticmethod
    @app.route('/users/profile')
    def profile():
        return render_template('users/profile.html')

    @staticmethod
    @app.route('/users/register')
    def register():
        return render_template('users/register.html')
