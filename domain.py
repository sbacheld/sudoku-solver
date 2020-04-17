class IntRangeDomain:
    _values = set()

    def __init__(self, lower_bound, upper_bound):
        self._values = set([i for i in range(lower_bound, upper_bound + 1)])
    
    @property
    def values(self):
        return self._values
