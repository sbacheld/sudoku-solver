import string
from collections import namedtuple


class Unit:
    EMPTY_SPACE = 0
    _name = None
    _value = None

    def __init__(self, name, value):
        self._name = name
        self._value = value

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    def empty(self):
        return self._value == self.EMPTY_SPACE

    def filled(self):
        return not self.empty()


class Board:
    SIZE = 9
    _board = []

    def __init__(self, initial_values=None):
        self._board = [[]] * self.SIZE
        for i in range(self.SIZE):
            self._board[i] = [None] * self.SIZE
            for j in range(self.SIZE):
                name = self._grid_to_unit_name(i, j)
                initial_value = Unit.EMPTY_SPACE
                if initial_values:
                    initial_value = initial_values[i][j]
                self._board[i][j] = Unit(name, initial_value)

    def board_valid(self):
        return all([self.unit_valid(i, j) for i in range(self.SIZE) for j in range(self.SIZE)])

    def unit_valid(self, row, col):
        return self._board[row][col].value >= 0 and self._board[row][col].value <= self.SIZE

    def is_filled_out(self):
        return all([self._board[i][j].filled() for i in range(self.SIZE) for j in range(self.SIZE)])

    def boxes_units(self):
        for rows in [[0, 1, 2], [3, 4, 5], [6, 7, 8]]:
            for cols in [[0, 1, 2], [3, 4, 5], [6, 7, 8]]:
                yield [self._board[i][j] for i in rows for j in cols]

    def rows(self):
        for i in range(self.SIZE):
            yield self._board[i][:]

    def columns(self):
        for i in range(self.SIZE):
            yield [self._board[j][i] for j in range(self.SIZE)]

    def units(self):
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                yield self._board[i][j]

    def _grid_to_unit_name(self, i, j):
        return '{}{}'.format(string.ascii_uppercase[i], j)

    def _unit_name_to_grid(self, unit_name):
        return string.ascii_uppercase.find(unit_name[0]), int(unit_name[1])

    def update_units_by_name(self, units):
        for name, value in units.items():
            i, j = self._unit_name_to_grid(name)
            self._board[i][j] = Unit(name, value)

    def __str__(self):
        rows = []
        for i, row in enumerate(self.rows()):
            if i > 0 and i % 3 == 0:
                rows.append('-------+-------+-------')
            row_values = [unit.value for unit in row]
            rows.append(' {} {} {} | {} {} {} | {} {} {}'.format(*row_values))
        return '\n'.join(rows)
