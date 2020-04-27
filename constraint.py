class Constraint:
    def is_violated(self, assignment):
        raise NotImplementedError

    def is_unary(self):
        raise NotImplementedError

    def is_binary(self):
        raise NotImplementedError

    def get_arcs(self):
        raise NotImplementedError


class AllDiffConstraint(Constraint):
    _variables = []

    def __init__(self, variables):
        self._variables = variables

    def is_violated(self, assignment):
        values = set()
        for variable in self._variables:
            if not assignment.is_set(variable.name):
                continue

            assigned_value = assignment.get(variable.name)
            if assigned_value in values:
                return True

            values.add(assigned_value)

        return False

    def is_unary(self):
        return False

    def is_binary(self):
        return True

    def get_arcs(self):
        return []  # TODO


class EqualConstraint(Constraint):
    _variable = None
    _value = None

    def __init__(self, variable, value):
        self._variable = variable
        self._value = value

    def is_violated(self, assignment):
        if not assignment.is_set(self._variable.name):
            return False

        assigned_value = assignment.get(self._variable.name)

        return assigned_value != self._value

    def is_unary(self):
        return True

    def is_binary(self):
        return False

    def get_arcs(self):
        return []

    @property
    def variable(self):
        return self._variable

    def allowed_values(self):
        return [self._value]
