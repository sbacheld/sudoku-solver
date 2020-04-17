class Board:
    EMPTY_SPACE = 0
    _board = []
    _size = 0

    def __init__(self, initial_values):
        self._board = initial_values
        self._size = len(initial_values)

    def board_valid(self):
        return all([self.unit_valid(i, j) for i in range(self._size) for j in range(self._size)])

    def unit_valid(self, row, col):
        return self._board[row][col] >= 0 and self._board[row][col] <= self._size

    def unit_empty(self, row, col):
        return self._board[row][col] == self.EMPTY_SPACE

    def is_filled_out(self):
        return all([not self.unit_empty(i, j) for i in range(self._size) for j in range(self._size)])
