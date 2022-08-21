from flask import render_template
from config import app


class HomeController(object):

    @staticmethod
    @app.route('/abiturient')
    def abiturient():
        return render_template('/home/abiturient.html')

    @staticmethod
    @app.route('/about')
    def about():
        return render_template('/home/about.html')

    @staticmethod
    @app.route('/administrations')
    def administrations():
        return render_template('/home/administrations.html')

    @staticmethod
    @app.route('/cadet')
    def cadet():
        return render_template('/home/cadet.html')

    @staticmethod
    @app.route('/contact')
    def contact():
        return render_template('/home/contact.html')

    @staticmethod
    @app.route('/')
    def index():
        return render_template('/home/index.html')

    @staticmethod
    @app.route('/partners')
    def partners():
        return render_template('/home/partners.html')

    @staticmethod
    @app.route('/teachers')
    def teachers():
        return render_template('/home/teachers.html')



