RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Cell:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __eq__(self, cell):
        return self.i == cell.i and self.j == cell.j

    def __hash__(self):
        return hash((self.i, self.j))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, point):
        return self.x == point.x and self.y == point.y

    def __hash__(self):
        return hash((self.x, self.y))


class Vector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __eq__(self, vector):
        return self.i == vector.i and self.j == vector.j

    def __hash__(self):
        return hash((self.i, self.j))
