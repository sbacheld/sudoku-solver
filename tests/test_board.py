import unittest
from board import Board


class TestBoard(unittest.TestCase):
    def test_filled_out_returns_false_if_not_filled_out(self):
        # Arrange
        initial_values = [[1 for _ in range(9)] for _ in range(9)]
        initial_values[5][3] = Board.EMPTY_SPACE
        board = Board(initial_values)

        # Act
        result = board.is_filled_out()

        # Assert
        self.assertFalse(result)

    def test_filled_out_returns_true_if_filled_out(self):
        # Arrange
        initial_values = [[1 for _ in range(9)] for _ in range(9)]
        board = Board(initial_values)

        # Act
        result = board.is_filled_out()

        # Assert
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
