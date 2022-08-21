from mysql.connector import connect, Error
from lib.mysql_provider import MysqlProvider


class Doctor(MysqlProvider):

    def add_doctor(self, name: str, phone: str, hospital_id: int) -> None:
        query = """
            insert into doctors (name, phone, hospital_id)
            values (%s, %s, %s);
        """
        try:
            with connect(
                    host=self._host,
                    user=self._user,
                    password=self._password,
                    database=self._database
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query, (name, phone, hospital_id))
                    connection.commit()
        except Error as error:
            print(error)
            raise RuntimeError('Ошибка выполнения SQL-запроса')

    def get_all_doctors(self) -> list:
        query = """ select * from doctors order by id """
        try:
            with connect(
                host=self._host,
                user=self._user,
                password=self._password,
                database=self._database
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query)
                    return cursor.fetchall()
        except Error as error:
            print(error)
            raise RuntimeError('Ошибка выполнения SQL-запроса')
