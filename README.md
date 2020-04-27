# sudoku-solver
A Sudoku solver built using various CSP techniques.

## Environment Setup

Use Conda to create the environment.
```bash
conda env create -f env.yml
```

Activate the environment:
```bash
conda activate sudokusolver
```

Deactivate the environment:
```bash
conda deactivate
```

## Tests

Running all tests:
```bash
python -m unittest
```

## Running

```bash
python runner.py
```

Sample output:
```
~/projects/sudoku-solver $ python runner.py 
Puzzle solved?:   True
Elapsed time (s): 121.2094509601593

Initial board:

 0 9 6 | 0 4 0 | 0 3 0
 0 5 7 | 8 2 0 | 0 0 0
 1 0 0 | 9 0 0 | 5 0 0
-------+-------+-------
 0 0 9 | 0 1 0 | 0 0 8
 5 0 0 | 0 0 0 | 0 0 2
 4 0 0 | 0 9 0 | 6 0 0
-------+-------+-------
 0 0 4 | 0 0 3 | 0 0 1
 0 0 0 | 0 7 9 | 2 6 0
 0 2 0 | 0 5 0 | 9 8 0

Solved board:

 2 9 6 | 1 4 5 | 8 3 7
 3 5 7 | 8 2 6 | 1 4 9
 1 4 8 | 9 3 7 | 5 2 6
-------+-------+-------
 6 3 9 | 5 1 2 | 4 7 8
 5 8 1 | 7 6 4 | 3 9 2
 4 7 2 | 3 9 8 | 6 1 5
-------+-------+-------
 9 6 4 | 2 8 3 | 7 5 1
 8 1 5 | 4 7 9 | 2 6 3
 7 2 3 | 6 5 1 | 9 8 4
```
