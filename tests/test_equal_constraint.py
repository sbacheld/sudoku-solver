import unittest
from constraint import EqualConstraint
from domain import Domain
from variable import Variable


class TestEqualConstraint(unittest.TestCase):
    def test_not_violated_if_variable_not_set(self):
        # Arrange
        variable = Variable('1', Domain([1]))
        constraint = EqualConstraint(variable, 1)

        # Act
        result = constraint.is_violated()

        # Assert
        self.assertFalse(result)

    def test_not_violated_if_variable_equal(self):
        # Arrange
        variable = Variable('1', Domain([1]), 1)
        constraint = EqualConstraint(variable, 1)

        # Act
        result = constraint.is_violated()

        # Assert
        self.assertFalse(result)

    def test_violated_if_variable_not_equal(self):
        # Arrange
        variable = Variable('1', Domain([1]), 1)
        constraint = EqualConstraint(variable, 2)

        # Act
        result = constraint.is_violated()

        # Assert
        self.assertTrue(result)
