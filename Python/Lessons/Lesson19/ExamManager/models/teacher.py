from lib.provider import Provider


class Teacher(Provider):

    def __init__(self):
        super().__init__()

    def add(self, name: str, birth: str) -> None:
        self.execute_dml("""
            insert into Teachers (name, birth) values (?, ?);
        """, (name, birth))

    def remove(self, name: str,) -> None:
        self.execute_dml("""
            delete from Teachers where name=?;
        """, (name,))

    def update(self, new_name: str, new_birth: str, old_name: str):
        self.execute_dml("""
            update Teachers set name=?, birth=? where name=?
        """, (new_name, new_birth, old_name))

    def get_all(self) -> list:
        return self.execute_select("""
            select * from Teachers;
        """)
