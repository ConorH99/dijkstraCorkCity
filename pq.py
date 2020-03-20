class Element:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __eq__(self, other):
        return self.key == other.key:

    def __lt__(self, other):
        return self.key < other.key