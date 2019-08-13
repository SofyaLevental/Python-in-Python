from samples.utils import Vector, Cell, Point, RED


class Cube:
    def __init__(self, position, direction=Vector(0, 1), color=RED):
        self.position = position
        self.direction = direction
        self.color = color

    def move(self, cells, direction):
        def modulus_cells(number):
            return number % cells

        self.direction = direction
        self.position = Cell(
            modulus_cells(self.position.i + self.direction.i),
            modulus_cells(self.position.j + self.direction.j)
        )

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


class Snake:
    def __init__(self, position, color=RED):
        self.body = []
        self.position = position
        self.head = Cube(position)
        self.body.append(self.head)
        self.direction = Vector(1, 0)
        self.color = color

    def reset(self, position):
        self.body = []
        self.position = position
        self.head = Cube(position)
        self.body.append(self.head)
        self.direction = Vector(1, 0)

    def move(self, cells):
        new_head = Cube(self.body[0].position, self.body[0].direction)
        new_head.move(cells, new_head.direction)
        self.body.insert(0, new_head)

    def draw(self, cell_width, draw_rect, draw_circle):
        for index, cube in enumerate(self.body):
            if index == 0:
                cube.draw(cell_width, draw_rect, draw_circle, True)
            else:
                cube.draw(cell_width, draw_rect)

    def update_direction(self, direction):
        self.direction = direction
        self.body[0].direction = self.direction
