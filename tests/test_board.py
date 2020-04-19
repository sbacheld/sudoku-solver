import unittest
from board import Board, Unit


class TestBoard(unittest.TestCase):
    def test_filled_out_returns_false_if_not_filled_out(self):
        # Arrange
        initial_values = [[1 for _ in range(9)] for _ in range(9)]
        initial_values[5][3] = Unit.EMPTY_SPACE
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

    def test_units_yields_all_units(self):
        # Arrange
        board = Board()
        count = 0
        unit_names = set()

        # Act
        for unit in board.units():
            count += 1
            unit_names.add(unit.name)

        # Assert
        self.assertEqual(Board.SIZE * Board.SIZE, count)
        self.assertEqual(count, len(unit_names))

    def test_rows_yields_all_rows(self):
        # Arrange
        board = Board()
        count = 0
        unit_names = set()
        row_names = []
        expected_row_name_sets = [
            ['A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8'],
            ['B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8'],
            ['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8'],
            ['D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8'],
            ['E0', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8'],
            ['F0', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8'],
            ['G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8'],
            ['H0', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8'],
            ['I0', 'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8'],
        ]

        # Act
        for row in board.rows():
            count += 1
            [unit_names.add(unit.name) for unit in row]
            row_names.append([unit.name for unit in row])

        # Assert
        self.assertEqual(Board.SIZE, count)
        self.assertEqual(Board.SIZE * Board.SIZE, len(unit_names))
        for i, expected_row_name_set in enumerate(expected_row_name_sets):
            self.assertEqual(expected_row_name_set, row_names[i])

    def test_columns_yields_all_columns(self):
        # Arrange
        board = Board()
        count = 0
        unit_names = set()
        column_names = []
        expected_column_name_sets = [
            ['A0', 'B0', 'C0', 'D0', 'E0', 'F0', 'G0', 'H0', 'I0'],
            ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1'],
            ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'],
            ['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'I3'],
            ['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'I4'],
            ['A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'I5'],
            ['A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'I6'],
            ['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'I7'],
            ['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'I8'],
        ]

        # Act
        for col in board.columns():
            count += 1
            [unit_names.add(unit.name) for unit in col]
            column_names.append([unit.name for unit in col])

        # Assert
        self.assertEqual(Board.SIZE, count)
        self.assertEqual(Board.SIZE * Board.SIZE, len(unit_names))
        for i, expected_column_name_set in enumerate(expected_column_name_sets):
            self.assertEqual(expected_column_name_set, column_names[i])

    def test_columns_and_rows_yield_different_results(self):
        # Arrange
        board = Board()
        columns = []
        rows = []

        # Act
        for row in board.rows():
            rows.append([unit.name for unit in row])
        for col in board.columns():
            columns.append([unit.name for unit in col])

        # Assert
        for i in range(Board.SIZE):
            self.assertNotEqual(rows[i], columns[i])


if __name__ == '__main__':
    unittest.main()
