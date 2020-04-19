import unittest
from assignment import Assignment
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
        assignment = Assignment()

        # Act
        result = constraint.is_violated(assignment)

        # Assert
        self.assertFalse(result)

    def test_not_violated_if_some_variables_not_set(self):
        # Arrange
        assignment = Assignment()
        variables = []
        for i in range(9):
            variable = Variable(str(i), Domain(list(range(1, 10))))
            variables.append(variable)
            if i < 4:
                # Only assign some of the values
                assignment.set(variable.name, i + 1)
        constraint = AllDiffConstraint(variables)

        # Act
        result = constraint.is_violated(assignment)

        # Assert
        self.assertFalse(result)

    def test_not_violated_if_all_variables_different(self):
        # Arrange
        assignment = Assignment()
        variables = []
        for i in range(9):
            variable = Variable(str(i), Domain(list(range(1, 10))))
            variables.append(variable)
            assignment.set(variable.name, i + 1)
        constraint = AllDiffConstraint(variables)

        # Act
        result = constraint.is_violated(assignment)

        # Assert
        self.assertFalse(result)

    def test_violated_if_at_least_one_variable_not_different(self):
        # Arrange
        assignment = Assignment()
        variables = []
        for i in range(8):
            variable = Variable(str(i), Domain(list(range(1, 10))))
            variables.append(variable)
            assignment.set(variable.name, i + 1)
        non_unique_variable = Variable('8', Domain(list(range(1, 10))))
        variables.append(non_unique_variable)
        assignment.set(non_unique_variable.name, 1)
        constraint = AllDiffConstraint(variables)

        # Act
        result = constraint.is_violated(assignment)

        # Assert
        self.assertTrue(result)
