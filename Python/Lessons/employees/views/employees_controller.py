from flask import render_template, session, request
from werkzeug.utils import secure_filename
from os import path
from config import app
from models.employees import Employees


class EmployeesController(object):

    @staticmethod
    @app.route('/employees/create', methods=['GET', 'POST'])
    def create():
        if 'user' in session and session['user'] == 'admin':
            if request.method == 'GET':
                return render_template('employees/create.html')
            elif request.method == 'POST':
                name = request.form.get('name')
                phone = request.form.get('phone')
                email = request.form.get('email')
                position = request.form.get('position')

                file = request.files.get('image')
                filename = secure_filename(file.filename)
                extensions = ['png', 'jpg', 'jpeg', 'gif', 'bmp']
                size_limit = 10 * 1024 * 1024  # 10Mb

                if filename.split('.')[-1] not in extensions:
                    message = 'Файл не графического формата!'
                    mess_color = 'red'
                elif len(file.read()) > size_limit:
                    message = 'Файл больше 10 Mb'
                    mess_color = 'red'
                else:
                    local_dir = path.dirname(path.abspath(__file__))
                    root_dir = path.abspath(local_dir + '\\..\\')
                    save_dir = root_dir + '\\media\\upload'

                    save_path = path.join(save_dir, filename)
                    file.stream.seek(0)
                    file.save(save_path)

                    image = f'../media/upload/{filename}'
                    user_id = 1
                    Employees.add_employees(name, phone, email, image, position, user_id)

                    message = 'Сотрудник успешно добавлен!'
                    mess_color = 'green'

                return render_template('employees/create_info.html', context={
                    'message': message,
                    'mess_color': mess_color
                })
        else:
            return render_template('access/page403.html')

    @staticmethod
    @app.route('/employees/delete')
    def delete():
        return render_template('employees/delete.html')

    @staticmethod
    @app.route('/employees/details')
    def details():
        return render_template('employees/details.html')

    @staticmethod
    @app.route('/employees/list')
    def list():
        return render_template('employees/list.html')

    @staticmethod
    @app.route('/employees/update')
    def update():
        return render_template('employees/update.html')
