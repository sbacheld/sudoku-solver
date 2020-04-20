class Assignment:
    _state = {}

    def __init__(self):
        self._state = {}

    def set(self, name, value):
        self._state[name] = value

    def get(self, name):
        return self._state.get(name)

    def is_set(self, name):
        return self.get(name) != None

    def unset(self, name):
        del self._state[name]

    def count(self):
        return len(self._state)

    @property
    def state(self):
        return self._state
