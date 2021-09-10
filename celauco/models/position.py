class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({},{})'.format(self.x, self.y)

    def is_equal(self, x, y):
        if x != self.x:
            return False
        if y != self.y:
            return False
        return True
