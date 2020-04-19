import unittest
from assignment import Assignment
from constraint import EqualConstraint
from domain import Domain
from variable import Variable


class TestEqualConstraint(unittest.TestCase):
    def test_not_violated_if_variable_not_set(self):
        # Arrange
        variable = Variable('1', Domain([1]))
        constraint = EqualConstraint(variable, 1)
        assignment = Assignment()

        # Act
        result = constraint.is_violated(assignment)

        # Assert
        self.assertFalse(result)

    def test_not_violated_if_variable_equal(self):
        # Arrange
        expected_value = 1
        variable = Variable('1', Domain([expected_value]))
        constraint = EqualConstraint(variable, expected_value)
        assignment = Assignment()
        assignment.set(variable.name, expected_value)

        # Act
        result = constraint.is_violated(assignment)

        # Assert
        self.assertFalse(result)

    def test_violated_if_variable_not_equal(self):
        # Arrange
        actual_value = 1
        expected_value = 2
        variable = Variable('1', Domain([actual_value]))
        constraint = EqualConstraint(variable, expected_value)
        assignment = Assignment()
        assignment.set(variable.name, actual_value)

        # Act
        result = constraint.is_violated(assignment)

        # Assert
        self.assertTrue(result)
