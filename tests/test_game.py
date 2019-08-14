import unittest
from unittest.mock import Mock

from samples.objects import Cube, Snake
from samples.utils import Cell, Vector, RED, Point

cells = 20
cell_width = 25


class TestCubeMethods(unittest.TestCase):
    position = Cell(10, 10)
    rect = (
        position.i * cell_width + 1,
        position.j * cell_width + 1,
        cell_width - 1,
        cell_width - 1
    )

    def setUp(self):
        self.cube = Cube(self.position)

    def test_move(self):
        new_direction = Vector(-1, 0)

        self.cube.move(cells, new_direction)

        self.assertEqual(self.cube.position, Cell(9, 10))
        self.assertEqual(self.cube.direction, new_direction)

    def test_move_through_boarder(self):
        self.cube = Cube(Cell(0, 10))
        new_direction = Vector(-1, 0)

        self.cube.move(cells, new_direction)

        self.assertEqual(self.cube.position, Cell(19, 10))
        self.assertEqual(self.cube.direction, new_direction)

    def test_draw_cube(self):
        mocked_draw_rect = Mock()

        self.cube.draw(cell_width, mocked_draw_rect)

        mocked_draw_rect.assert_called_with(self.rect, RED)

    def test_draw_head_cube(self):
        mocked_draw_rect = Mock()
        mocked_draw_circle = Mock()

        radius = 3
        shift = 6
        cube_center_coordinate = 263
        left_eye_middle = Point(cube_center_coordinate - shift, cube_center_coordinate)
        right_eye_middle = Point(cube_center_coordinate + shift, cube_center_coordinate)

        self.cube.draw(cell_width, mocked_draw_rect, mocked_draw_circle, True)

        mocked_draw_rect.assert_called_with(self.rect, RED)
        self.assertEqual(mocked_draw_circle.call_count, 2)
        mocked_draw_circle.assert_any_call(left_eye_middle, radius)
        mocked_draw_circle.assert_any_call(right_eye_middle, radius)


class TestSnakeMethods(unittest.TestCase):
    def setUp(self):
        self.snake = Snake(Cell(10, 10))

    def test_update_direction(self):
        new_direction = Vector(-1, 0)
        self.snake.update_direction(new_direction)

        self.assertEqual(self.snake.get_head().direction, new_direction)

    def test_move(self):
        new_head = Cube(Cell(11, 10), Vector(1, 0))

        self.snake.move(cells)

        self.assertEqual(len(self.snake.get_body()), 2)
        self.assertEqual(self.snake.get_head(), new_head)

    def test_draw(self):
        mocked_draw_rect = Mock()
        mocked_draw_circle = Mock()
        mocked_head = Mock()

        def get_body():
            return [mocked_head]

        self.snake.get_body = get_body

        self.snake.draw(cell_width, mocked_draw_rect, mocked_draw_circle)

        mocked_head.draw.assert_called_with(cell_width, mocked_draw_rect, mocked_draw_circle, True)


if __name__ == '__main__':
    unittest.main()
