import time
from board import Board
from sudoku_solver import SudokuSolver


def main():
    initial_board_values = [
        [0, 9, 6, 0, 4, 0, 0, 3, 0],
        [0, 5, 7, 8, 2, 0, 0, 0, 0],
        [1, 0, 0, 9, 0, 0, 5, 0, 0],
        [0, 0, 9, 0, 1, 0, 0, 0, 8],
        [5, 0, 0, 0, 0, 0, 0, 0, 2],
        [4, 0, 0, 0, 9, 0, 6, 0, 0],
        [0, 0, 4, 0, 0, 3, 0, 0, 1],
        [0, 0, 0, 0, 7, 9, 2, 6, 0],
        [0, 2, 0, 0, 5, 0, 9, 8, 0],
    ]
    board = Board(initial_board_values)
    sudoku_solver = SudokuSolver()
    sudoku_solver.prepare(board)

    start_time = time.time()

    sudoku_solver.run()

    elapsed_time = time.time() - start_time

    result = sudoku_solver.get_result()

    print('Puzzle solved?:   {}'.format(result.success))
    print('Elapsed time (s): {}'.format(elapsed_time))
    if result.success:
        print('\nInitial board:\n')
        print(board)
        board.update_units_by_name(result.assignment.state)
        print('\nSolved board:\n')
        print(board)


if __name__ == '__main__':
    main()
