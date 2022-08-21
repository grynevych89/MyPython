from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config['SECRET_KEY'] = '81dc9bdb52d04dc20036dbd8313ed055'
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'university_db'

mysql = MySQL()
mysql.init_app(app)
