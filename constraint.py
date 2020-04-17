class Constraint:
    def is_violated(self):
        raise NotImplementedError


class AllDiffConstraint(Constraint):
    _variables = []

    def __init__(self, variables):
        self._variables = variables

    def is_violated(self):
        values = set()
        for variable in self._variables:
            if not variable.is_set:
                continue
            if variable.value in values:
                return True
            values.add(variable.value)

        return False


class EqualConstraint(Constraint):
    _variable = None
    _value = None

    def __init__(self, variable, value):
        self._variable = variable
        self._value = value

    def is_violated(self):
        if self._variable.value is None:
            return False

        return self._variable.value != self._value
