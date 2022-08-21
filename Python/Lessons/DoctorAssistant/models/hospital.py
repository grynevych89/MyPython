from mysql.connector import connect, Error
from lib.mysql_provider import MysqlProvider


class Hospital(MysqlProvider):

    def add_hospital(self, name: str, phone: str, address: str) -> None:
        query = """
            insert into hospitals (name, phone, address)
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
                    cursor.execute(query, (name, phone, address))
                    connection.commit()
        except Error as error:
            print(error)
            raise RuntimeError('Ошибка выполнения SQL-запроса')

    def get_all_hospitals(self) -> list:
        query = """ select * from hospitals order by id """
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
