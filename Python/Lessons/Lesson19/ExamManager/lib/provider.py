import sqlite3


class Provider(object):

    def __init__(self):
        self._db = 'exam_manager.db'
        self._conn = sqlite3.connect(self._db)
        self._cursor = self._conn.cursor()

    def execute_dml(self, sql: str, params=tuple()) -> None:
        if len(params) == 0:
            self._cursor.execute(sql)
        else:
            self._cursor.execute(sql, params)
        self._conn.commit()

    def execute_select(self, sql: str, params=tuple()) -> list:
        if len(params) == 0:
            self._cursor.execute(sql)
        else:
            self._cursor.execute(sql, params)
        return self._cursor.fetchall()
