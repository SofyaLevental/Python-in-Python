import unittest

from samples.objects import Cube
from samples.utils import Cell, Vector


class TestCubeMethods(unittest.TestCase):

    def test_move(self):
        cube = Cube(Cell(10, 10))
        cube.move(Vector(1, 0))
        self.assertEqual(cube.position, Cell(11, 10))


if __name__ == '__main__':
    unittest.main()
