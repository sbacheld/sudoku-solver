class Domain:
    _values = []

    def __init__(self, values):
        self._values = values
    
    @property
    def values(self):
        return self._values
