from flask import render_template
from config import app


class HomeController(object):

    @staticmethod
    @app.route('/')
    def index():
        return render_template('/home/index.html')

    @staticmethod
    @app.route('/about')
    def about():
        return render_template('/home/about.html')

    @staticmethod
    @app.route('/contact')
    def contact():
        return render_template('/home/contact.html')
