import unittest
from constraint import AllDiffConstraint
from domain import Domain
from variable import Variable


class TestAllDiffConstraint(unittest.TestCase):
    def test_not_violated_if_variables_not_set(self):
        # Arrange
        variables = [
            Variable(str(i), Domain(list(range(1, 10))))
            for i in range(9)
        ]
        constraint = AllDiffConstraint(variables)

        # Act
        result = constraint.is_violated()

        # Assert
        self.assertFalse(result)

    def test_not_violated_if_some_variables_not_set(self):
        # Arrange
        variables = [
            Variable(str(i), Domain(list(range(1, 10))), i + 1)
            for i in range(4)
        ]
        variables += [
            Variable(str(i), Domain(list(range(1, 10))))
            for i in range(4, 9)
        ]
        constraint = AllDiffConstraint(variables)

        # Act
        result = constraint.is_violated()

        # Assert
        self.assertFalse(result)

    def test_not_violated_if_all_variables_different(self):
        # Arrange
        variables = [
            Variable(str(i), Domain(list(range(1, 10))), i+1)
            for i in range(9)
        ]
        constraint = AllDiffConstraint(variables)

        # Act
        result = constraint.is_violated()

        # Assert
        self.assertFalse(result)

    def test_violated_if_at_least_variable_not_different(self):
        # Arrange
        variables = [
            Variable(str(i), Domain(list(range(1, 10))), i+1)
            for i in range(9)
        ]
        variables.append(Variable('9', Domain(list(range(1, 10))), 1))
        constraint = AllDiffConstraint(variables)

        # Act
        result = constraint.is_violated()

        # Assert
        self.assertTrue(result)
