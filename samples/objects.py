from samples.utils import Vector, Cell, Point


class Cube:
    def __init__(self, position, direction=Vector(0, 1), color=(255, 0, 0)):
        self.position = position
        self.direction = direction
        self.color = color

    def move(self, direction):
        self.direction = direction
        self.position = Cell(self.position.i + self.direction.i, self.position.j + self.direction.j)

    def draw(self, cell_width, draw_rect, draw_circle=None, eyes=False):
        i_position = self.position.i
        j_position = self.position.j
        rect = (i_position * cell_width + 1, j_position * cell_width + 1, cell_width - 1, cell_width - 1)
        draw_rect(rect, self.color)
        if eyes:
            half_cell_width = cell_width // 2
            cube_center = Point(
                i_position * cell_width + 1 + half_cell_width,
                j_position * cell_width + 1 + half_cell_width
            )
            radius = 3
            left_eye_middle = Point(cube_center.x - 6, cube_center.y)
            right_eye_middle = Point(cube_center.x + 6, cube_center.y)
            draw_circle(left_eye_middle, radius)
            draw_circle(right_eye_middle, radius)
