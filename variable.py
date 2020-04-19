class Variable:
    _name = None
    _domain = None

    def __init__(self, name, domain):
        self._name = name
        self._domain = domain

    @property
    def name(self):
        return self._name

    @property
    def domain(self):
        return self._domain
