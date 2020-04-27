from board import Board
from constraint import EqualConstraint, AllDiffConstraint
from constraint_satisfaction_problem import ConstraintSatisfactionProblem
from domain import Domain
from inference import NodeConsistency
from solver import Solver
from variable import Variable


class SudokuSolver:
    _result = None
    _csp = None
    _csp_solver = None

    def __init__(self):
        self._result = None
        self._csp = None

        preprocessors = [NodeConsistency()]
        self._csp_solver = Solver(preprocessors)

    def prepare(self, board):
        variables = self._build_variables(board)
        constraints = self._build_constraints(board, variables)
        self._csp = ConstraintSatisfactionProblem(variables, constraints)

    def run(self):
        self._result = self._csp_solver.solve(self._csp)

    def get_result(self):
        return self._result

    def _build_variables(self, board):
        variables = []
        for unit in board.units():
            variables.append(Variable(unit.name, Domain(list(range(1, 10)))))

        return variables

    def _build_constraints(self, board, variables):
        constraints = []
        variable_lookup = {variable.name: variable for variable in variables}

        # Add equal constraints for board values that are already set
        for unit in board.units():
            if unit.empty():
                continue
            variable = variable_lookup[unit.name]
            constraints.append(EqualConstraint(variable, unit.value))

        # Add all-diff constraints for rows
        for row in board.rows():
            row_variables = [variable_lookup[unit.name] for unit in row]
            constraints.append(AllDiffConstraint(row_variables))

        # Add all-diff constraints for columns
        for col in board.columns():
            col_variables = [variable_lookup[unit.name] for unit in col]
            constraints.append(AllDiffConstraint(col_variables))

        # Add all-diff constraints for boxes
        for box_units in board.boxes_units():
            box_variables = [variable_lookup[unit.name] for unit in box_units]
            constraints.append(AllDiffConstraint(box_variables))

        return constraints
