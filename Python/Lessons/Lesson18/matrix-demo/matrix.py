class Matrix(object):

    def __init__(self, rows: int, cols: int, m: list):
        self._rows = rows
        self._cols = cols
        self._table = [[0] * cols for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                self._table[i][j] = m[i][j]

    def display(self) -> None:
        for i in range(self._rows):
            for j in range(self._cols):
                print(f'{self._table[i][j]:3d}', end='')
            print()
        print()

    def __add__(self, other):
        new_table = [[0] * self._cols for i in range(self._rows)]
        for i in range(self._rows):
            for j in range(self._cols):
                new_table[i][j] = self._table[i][j] + other._table[i][j]
        return Matrix(self._rows, self._cols, new_table)
