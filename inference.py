class Inference:
    def apply(self, csp):
        raise NotImplementedError


class NodeConsistency(Inference):
    def apply(self, csp):
        unary_constraints = [c for c in csp.constraints if c.is_unary()]
        for uc in unary_constraints:
            variable = uc.variable
            allowed_values = uc.allowed_values()
            variable.domain.update_values(allowed_values)
