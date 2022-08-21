from config import mysql


class Employees(object):

    @staticmethod
    def add_employees(name, phone, email, image, position, user_id):
        connection = mysql.get_db()
        cursor = connection.cursor()  # создаем курсор
        sql_query = """
            insert into employees (name, phone, email, image, position, user_id)
            values (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql_query, (name, phone, email, image, position, user_id))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def get_all_employees(self) -> list:
        pass
