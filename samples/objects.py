from samples.utils import Vector, Cell, Point, RED


class Cube:
    def __init__(self, position, direction=Vector(1, 0), color=RED):
        self.position = position
        self.direction = direction
        self.color = color

    def move(self, cells, direction):
        self.direction = direction
        self.position = Cell(
            self.__modulus_cells(self.position.i + self.direction.i, cells),
            self.__modulus_cells(self.position.j + self.direction.j, cells)
        )

    def draw(self, cell_width, draw_rect, draw_circle=None, eyes=False):
        rect = (
            self.position.i * cell_width + 1,
            self.position.j * cell_width + 1,
            cell_width - 1,
            cell_width - 1
        )

        draw_rect(rect, self.color)
        if eyes:
            self.__draw_eyes(cell_width, draw_circle)

    @staticmethod
    def __modulus_cells(number, cells):
        return number % cells

    def __draw_eyes(self, cell_width, draw_circle):
        half_cell_width = cell_width // 2
        cube_center = Point(
            self.position.i * cell_width + 1 + half_cell_width,
            self.position.j * cell_width + 1 + half_cell_width
        )
        radius = cell_width // 7
        shift = cell_width // 4
        left_eye_middle = Point(cube_center.x - shift, cube_center.y)
        right_eye_middle = Point(cube_center.x + shift, cube_center.y)
        draw_circle(left_eye_middle, radius)
        draw_circle(right_eye_middle, radius)

    def __eq__(self, cube):
        return self.position == cube.position and self.direction == cube.direction and self.color == cube.color

    def __hash__(self):
        return hash((self.position, self.direction, self.color))


class Snake:
    def __init__(self, position, color=RED):
        self.__body = []
        self.position = position
        self.__body.append(Cube(self.position))
        self.color = color

    def reset(self, position):
        self.__init__(position)

    def move(self, cells):
        new_head = Cube(self.get_head().position, self.get_head().direction)
        new_head.move(cells, new_head.direction)
        body = self.get_body()
        body.insert(0, new_head)
        self.set_body(body)

    def draw(self, cell_width, draw_rect, draw_circle):
        for index, cube in enumerate(self.get_body()):
            if index == 0:
                cube.draw(cell_width, draw_rect, draw_circle, True)
            else:
                cube.draw(cell_width, draw_rect)

    def update_direction(self, direction):
        head = self.get_head()
        head.direction = direction
        self.set_head(head)

    def get_body(self):
        return self.__body

    def set_body(self, body):
        self.__body = body

    def get_head(self):
        return self.get_body()[0]

    def set_head(self, head):
        self.__body[0] = head
