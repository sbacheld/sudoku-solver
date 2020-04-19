import unittest
from assignment import Assignment


class TestAssignment(unittest.TestCase):
    def test_assignment_starts_with_empty_state(self):
        # Arrange
        assignment = Assignment()

        # Act
        count = assignment.count()

        # Assert
        self.assertEqual(0, count)

    def test_unset_variable_name_is_none(self):
        # Arrange
        assignment = Assignment()

        # Act
        value = assignment.get('UNSET')

        # Assert
        self.assertIsNone(value)

    def test_set_adds_assignment(self):
        # Arrange
        assignment = Assignment()
        variable_name = 'A'
        variable_value = 10

        # Act
        assignment.set(variable_name, variable_value)

        # Assert
        self.assertEqual(1, assignment.count())
        self.assertTrue(assignment.is_set(variable_name))
        self.assertEqual(variable_value, assignment.get(variable_name))

    def test_unset_removes_assignment(self):
        # Arrange
        variable_name = 'A'
        assignment = Assignment()
        assignment.set(variable_name, 10)

        # Act
        assignment.unset(variable_name)

        # Assert
        self.assertEqual(0, assignment.count())
        self.assertFalse(assignment.is_set(variable_name))
        self.assertIsNone(assignment.get(variable_name))
