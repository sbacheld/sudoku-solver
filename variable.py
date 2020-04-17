class Variable:
    _name = None
    _domain = None
    _value = None

    def __init__(self, name, domain, value=None):
        self._name = name
        self._domain = domain
        self._value = value

    @property
    def name(self):
        return self._name

    @property
    def domain(self):
        return self._domain
    
    @property
    def value(self):
        return self._value

    @property
    def is_set(self):
        return self._value != None
