import unittest
from assignment import Assignment
from constraint import EqualConstraint
from constraint_satisfaction_problem import ConstraintSatisfactionProblem
from domain import Domain
from variable import Variable


class TestConstraintSatisfactionProblem(unittest.TestCase):
    def test_consistent_for_empty_assignment(self):
        # Arrange
        variables = [Variable('1', Domain([1, 2, 3]))]
        constraints = [EqualConstraint(variables[0], 2)]
        csp = ConstraintSatisfactionProblem(variables, constraints)
        assignment = Assignment()

        # Act
        consistent = csp.consistent(assignment)

        # Assert
        self.assertTrue(consistent)

    def test_consistent_for_partial_assignment(self):
        # Arrange
        variables = [
            Variable('1', Domain([1, 2, 3])),
            Variable('2', Domain([1, 2]))
        ]
        constraints = [EqualConstraint(variables[0], 2)]
        csp = ConstraintSatisfactionProblem(variables, constraints)
        assignment = Assignment()
        assignment.set(variables[0].name, 2)

        # Act
        consistent = csp.consistent(assignment)

        # Assert
        self.assertTrue(consistent)

    def test_consistent_and_complete_for_full_assignment(self):
        # Arrange
        variables = [
            Variable('1', Domain([1, 2, 3])),
            Variable('2', Domain([1, 2]))
        ]
        constraints = [EqualConstraint(variables[0], 2)]
        csp = ConstraintSatisfactionProblem(variables, constraints)
        assignment = Assignment()
        assignment.set(variables[0].name, 2)
        assignment.set(variables[1].name, 1)

        # Act
        consistent = csp.consistent(assignment)
        complete = csp.complete(assignment)

        # Assert
        self.assertTrue(consistent)
        self.assertTrue(complete)

    def test_not_consistent_if_assignment_violates_constraint(self):
        # Arrange
        variables = [
            Variable('1', Domain([1, 2, 3])),
            Variable('2', Domain([1, 2]))
        ]
        constraints = [EqualConstraint(variables[0], 2)]
        csp = ConstraintSatisfactionProblem(variables, constraints)
        assignment = Assignment()
        assignment.set(variables[0].name, 3)

        # Act
        consistent = csp.consistent(assignment)

        # Assert
        self.assertFalse(consistent)

    def test_select_unassigned_variable_returns_valid_variable(self):
        # Arrange
        variables = [
            Variable('1', Domain([1, 2, 3])),
            Variable('2', Domain([1, 2]))
        ]
        constraints = [EqualConstraint(variables[0], 2)]
        csp = ConstraintSatisfactionProblem(variables, constraints)
        assignment = Assignment()
        assignment.set(variables[0].name, 2)

        # Act
        variable = csp.select_unassigned_variable(assignment)

        # Assert
        self.assertIsNotNone(variable)
        self.assertEqual(variables[1].name, variable.name)

    def test_select_unassigned_variable_raises_exception_if_variable_not_available(self):
        # Arrange
        exception_thrown = False
        variables = [Variable('1', Domain([1]))]
        constraints = []
        csp = ConstraintSatisfactionProblem(variables, constraints)
        assignment = Assignment()
        assignment.set(variables[0].name, 1)

        # Act
        try:
            csp.select_unassigned_variable(assignment)
        except:
            exception_thrown = True

        # Assert
        self.assertTrue(exception_thrown)

    def test_order_domain_values_returns_all_domain_values(self):
        expected_values = set([1, 2, 3])
        variables = [Variable('1', Domain(list(expected_values)))]
        constraints = []
        csp = ConstraintSatisfactionProblem(variables, constraints)
        assignment = Assignment()
        values = set()

        # Act
        for value in csp.order_domain_values(variables[0], assignment):
            values.add(value)

        # Assert
        self.assertEqual(expected_values, values)
