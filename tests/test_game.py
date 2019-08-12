import unittest

from unittest.mock import Mock

from samples.objects import Cube
from samples.utils import Cell, Vector


class TestCubeMethods(unittest.TestCase):
    position = Cell(10, 10)
    cell_width = 20

    def setUp(self):
        self.cube = Cube(self.position)

    def test_move(self):
        new_direction = Vector(-1, 0)

        self.cube.move(new_direction)

        self.assertEqual(self.cube.position, Cell(9, 10))
        self.assertEqual(self.cube.direction, new_direction)

    def test_draw(self):
        mocked_draw_rect = Mock()
        rect = (
            self.position.i * self.cell_width + 1,
            self.position.j * self.cell_width + 1,
            self.cell_width - 1,
            self.cell_width - 1
        )

        self.cube.draw(self.cell_width, mocked_draw_rect)

        mocked_draw_rect.assert_called_with(rect, (255, 0, 0))


if __name__ == '__main__':
    unittest.main()
