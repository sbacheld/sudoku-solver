import unittest
from board import Board
from sudoku_solver import SudokuSolver


class TestSudokuSolver(unittest.TestCase):
    def test_easy_sudoku_puzzle_success(self):
        # Arrange
        expected_board_values = [
            [2, 9, 6, 1, 4, 5, 8, 3, 7],
            [3, 5, 7, 8, 2, 6, 1, 4, 9],
            [1, 4, 8, 9, 3, 7, 5, 2, 6],
            [6, 3, 9, 5, 1, 2, 4, 7, 8],
            [5, 8, 1, 7, 6, 4, 3, 9, 2],
            [4, 7, 2, 3, 9, 8, 6, 1, 5],
            [9, 6, 4, 2, 8, 3, 7, 5, 1],
            [8, 1, 5, 4, 7, 9, 2, 6, 3],
            [7, 2, 3, 6, 5, 1, 9, 8, 4],
        ]
        initial_board_values = [
            [0, 0, 6, 1, 4, 5, 8, 3, 7],
            [3, 5, 7, 8, 2, 6, 1, 4, 9],
            [1, 4, 8, 9, 3, 0, 0, 2, 6],
            [6, 3, 9, 5, 1, 2, 4, 7, 8],
            [5, 0, 1, 7, 6, 0, 3, 0, 2],
            [4, 7, 2, 3, 0, 8, 6, 1, 5],
            [9, 6, 4, 2, 8, 3, 7, 5, 1],
            [8, 1, 0, 4, 7, 9, 2, 6, 3],
            [7, 2, 0, 6, 5, 1, 9, 8, 0],
        ]
        board = Board(initial_board_values)
        sudoku_solver = SudokuSolver()
        sudoku_solver.prepare(board)

        # Act
        sudoku_solver.run()

        # Assert
        result = sudoku_solver.get_result()
        self.assertTrue(result.success)
        board.update_units_by_name(result.assignment.state)
        for i, row in enumerate(board.rows()):
            row_values = [unit.value for unit in row]
            self.assertEqual(expected_board_values[i], row_values)

    def test_impossible_sudoku_puzzle_failure(self):
        # Arrange
        initial_board_values = [
            [6, 6, 1, 1, 1, 5, 8, 3, 7],
            [3, 5, 7, 8, 2, 6, 1, 4, 9],
            [1, 4, 8, 9, 3, 0, 0, 2, 6],
            [6, 3, 9, 5, 1, 2, 4, 7, 8],
            [5, 0, 1, 7, 6, 0, 3, 0, 2],
            [4, 7, 2, 3, 0, 8, 6, 1, 5],
            [9, 6, 4, 2, 8, 3, 7, 5, 1],
            [8, 1, 0, 4, 7, 9, 2, 6, 3],
            [7, 2, 0, 6, 5, 1, 9, 8, 0],
        ]
        board = Board(initial_board_values)
        sudoku_solver = SudokuSolver()
        sudoku_solver.prepare(board)

        # Act
        sudoku_solver.run()

        # Assert
        result = sudoku_solver.get_result()
        self.assertFalse(result.success)
