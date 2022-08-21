from flask import render_template, session, request
from werkzeug.utils import secure_filename
from os import path
from config import app
from models.article import Article
from time import strftime, localtime


class NewsController(object):

    @staticmethod
    @app.route('/news/create', methods=['GET', 'POST'])
    def create():
        if 'user' in session and session['user'] == 'admin':
            if request.method == 'GET':
                return render_template('news/create.html')
            elif request.method == 'POST':
                title = request.form.get('title')
                about = request.form.get('about')
                content = request.form.get('content')
                status = request.form.get('status')

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
                    save_dir = root_dir + '\\static\\upload'

                    save_path = path.join(save_dir, filename)
                    file.stream.seek(0)
                    file.save(save_path)

                    image = f'upload/{filename}'
                    publish = strftime('%Y-%m-%d %H:%M:%S', localtime())
                    user_id = 2
                    Article.add_article(title, about, content, image, publish, user_id, status)

                    message = 'Новость успешно добавлена!'
                    mess_color = 'green'

                return render_template('news/create_info.html', context={
                    'message': message,
                    'mess_color': mess_color
                })
        else:
            return render_template('access/page403.html')

    @staticmethod
    @app.route('/news/delete')
    def delete():
        return render_template('news/delete.html')

    @staticmethod
    @app.route('/news/details')
    def details():
        return render_template('news/details.html')

    @staticmethod
    @app.route('/news/list')
    def list():
        all_news = Article.get_all_articles()
        return render_template('news/list.html', context={
            'all_news': all_news
        })

    @staticmethod
    @app.route('/news/update')
    def update():
        return render_template('news/update.html')
