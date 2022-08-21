from config import mysql
from werkzeug.security import check_password_hash


class User(object):

    @staticmethod
    def register(login, password, email, regdate, status) -> None:
        connection = mysql.get_db()
        cursor = connection.cursor()  # создаем курсор
        sql_query = """
            insert into users (login, password, email, regdate, status)
            values (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql_query, (login, password, email, regdate, status))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def auth(login, password) -> bool:
        connection = mysql.get_db()
        cursor = connection.cursor()
        sql_query = """
            select login, password from users where login=%s
        """
        cursor.execute(sql_query, (login,))
        result = cursor.fetchall()
        k = len(result)

        cursor.close()
        connection.close()

        if k == 0:
            return False
        else:
            return check_password_hash(result[0][1], password)
