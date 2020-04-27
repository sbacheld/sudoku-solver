class ConstraintSatisfactionProblem:
    _variables = []
    _constraints = []

    def __init__(self, variables, constraints):
        self._variables = variables
        self._constraints = constraints

    @property
    def variables(self):
        return self._variables
    
    @property
    def constraints(self):
        return self._constraints

    def complete(self, assignment):
        if assignment.count() != len(self._variables):
            return False

        return self.consistent(assignment)

    def consistent(self, assignment):
        for constraint in self._constraints:
            if constraint.is_violated(assignment):
                return False
        return True

    def select_unassigned_variable(self, assignment):
        for variable in self._variables:
            if not assignment.is_set(variable.name):
                return variable
        raise Exception('All variables have already been assigned')

    def order_domain_values(self, variable, assignment):
        for value in variable.domain.values:
            yield value
