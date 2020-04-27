from assignment import Assignment
from collections import namedtuple


SolverResult = namedtuple('SolverResult', ['success', 'assignment'])


class Solver:
    _inferencers = []

    def __init__(self, inferencers = []):
        self._inferencers = inferencers

    def solve(self, csp):
        for inferencer in self._inferencers:
            inferencer.apply(csp)

        return self._backtracking_search(csp)

    def _backtracking_search(self, csp):
        result = self._backtrack(Assignment(), csp)
        if result == False:
            return SolverResult(False, None)
        return SolverResult(True, result)

    def _backtrack(self, assignment, csp):
        if csp.complete(assignment):
            return assignment

        variable = csp.select_unassigned_variable(assignment)
        for value in csp.order_domain_values(variable, assignment):
            assignment.set(variable.name, value)
            if csp.consistent(assignment):
                result = self._backtrack(assignment, csp)
                if result != False:
                    return result
            assignment.unset(variable.name)

        return False
