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
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def __eq__(self, point):
        return self.__x == point.get_x() and self.__y == point.get_y()

    def __hash__(self):
        return hash((self.__x, self.__y))


class Vector:
    def __init__(self, i, j):
        self.__i = i
        self.__j = j

    def get_i(self):
        return self.__i

    def get_j(self):
        return self.__j

    def __eq__(self, vector):
        return self.__i == vector.get_i() and self.__j == vector.get_j()

    def __hash__(self):
        return hash((self.__i, self.__j))
