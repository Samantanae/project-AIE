class NotInCategory(Exception):
    def __init__(self, delta=""):
        self.__delta = delta

    @property
    def delta(self):
        return self.__delta