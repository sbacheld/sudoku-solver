import unittest
from constraint import AllDiffConstraint, EqualConstraint
from constraint_satisfaction_problem import ConstraintSatisfactionProblem
from domain import Domain
from solver import Solver
from variable import Variable


class TestSolver(unittest.TestCase):
    def test_solver_success_one_variable_one_constraint(self):
        # Arrange
        expected_value = 3
        variable = Variable('1', Domain([1, 2, 3, 4, 5]))
        constraint = EqualConstraint(variable, expected_value)
        csp = ConstraintSatisfactionProblem([variable], [constraint])
        solver = Solver()

        # Act
        result = solver.solve(csp)

        # Assert
        self.assertTrue(result.success)
        self.assertIsNotNone(result.assignment)
        self.assertEqual(expected_value, result.assignment.get(variable.name))

    def test_solver_failure_one_variable_one_constraint(self):
        # Arrange
        variable = Variable('1', Domain([1, 2, 3, 4, 5]))
        constraint = EqualConstraint(variable, 10)
        csp = ConstraintSatisfactionProblem([variable], [constraint])
        solver = Solver()

        # Act
        result = solver.solve(csp)

        # Assert
        self.assertFalse(result.success)
        self.assertIsNone(result.assignment)

    def test_solver_success_many_variables_many_constraints(self):
        # Arrange
        variables = []
        domain = set([1, 2, 3, 4, 5])
        for i in range(5):
            variable = Variable(str(i), Domain(list(domain)))
            variables.append(variable)
        constraints = [
            EqualConstraint(variables[2], 3),
            AllDiffConstraint(variables)
        ]
        csp = ConstraintSatisfactionProblem(variables, constraints)
        solver = Solver()

        # Act
        result = solver.solve(csp)

        # Assert
        self.assertTrue(result.success)
        assignment = result.assignment
        self.assertIsNotNone(assignment)
        self.assertEqual(3, assignment.get(variables[2].name))
        encountered_values = set()
        for variable in variables:
            value = assignment.get(variable.name)
            self.assertTrue(value in domain)
            self.assertFalse(value in encountered_values)
            encountered_values.add(value)
