class AllDiffConstraint:
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
