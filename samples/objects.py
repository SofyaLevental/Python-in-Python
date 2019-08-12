from samples.utils import Vector, Cell, Point, RED


class Cube:
    def __init__(self, position, direction=Vector(0, 1), color=RED):
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

        def draw_eyes():
            half_cell_width = cell_width // 2
            cube_center = Point(
                i_position * cell_width + 1 + half_cell_width,
                j_position * cell_width + 1 + half_cell_width
            )
            radius = cell_width // 7
            shift = cell_width // 4
            left_eye_middle = Point(cube_center.x - shift, cube_center.y)
            right_eye_middle = Point(cube_center.x + shift, cube_center.y)
            draw_circle(left_eye_middle, radius)
            draw_circle(right_eye_middle, radius)

        draw_rect(rect, self.color)
        if eyes:
            draw_eyes()
