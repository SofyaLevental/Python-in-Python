from samples.utils import Vector, Cell, Point, RED


class Cube:
    def __init__(self, position, direction=Vector(0, 1), color=RED):
        self.position = position
        self.direction = direction
        self.color = color

    def move(self, cells, direction):
        first_cell = 0
        last_cell = cells - 1

        self.direction = direction

        if self.direction.i == -1 and self.position.i == first_cell:
            self.position = Cell(last_cell, self.position.j)
        elif self.direction.i == 1 and self.position.i == last_cell:
            self.position = Cell(first_cell, self.position.j)
        elif self.direction.j == -1 and self.position.j == first_cell:
            self.position = Cell(self.position.i, last_cell)
        elif self.direction.j == 1 and self.position.j == last_cell:
            self.position = Cell(self.position.i, first_cell)
        else:
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


class Snake:
    def __init__(self, position, color=RED):
        self.body = []
        self.turns = {}
        self.position = position
        self.head = Cube(position)
        self.body.append(self.head)
        self.direction = Vector(1, 0)
        self.color = color

    def reset(self, position):
        self.body = []
        self.turns = {}
        self.position = position
        self.head = Cube(position)
        self.body.append(self.head)
        self.direction = Vector(1, 0)

    def add_cube(self):
        tail = self.body[-1]
        tail_direction = tail.direction

        if tail_direction.i == 1 and tail_direction.j == 0:
            self.create_new_tail_cube(tail.position.i - 1, tail.position.j)
        elif tail_direction.i == -1 and tail_direction.j == 0:
            self.create_new_tail_cube(tail.position.i + 1, tail.position.j)
        elif tail_direction.i == 0 and tail_direction.j == 1:
            self.create_new_tail_cube(tail.position.i, tail.position.j - 1)
        elif tail_direction.i == 0 and tail_direction.j == -1:
            self.create_new_tail_cube(tail.position.i, tail.position.j + 1)

    def create_new_tail_cube(self, i_grid_position, j_grid_position):
        self.body.append(Cube(Cell(i_grid_position, j_grid_position), self.body[-1].direction))

    def move(self, cells, listen_to_keyboard_events):
        first_cell = 0
        last_cell = cells - 1

        listen_to_keyboard_events()

        for index, cube in enumerate(self.body):
            position = cube.position
            if position in self.turns:
                turn = self.turns[position]
                cube.move(cells, turn)
                self.remove_tail_from_turns(index, position)
            else:
                cube.move(cells, cube.direction)

    def draw(self, cell_width, draw_rect, draw_circle):
        for index, cube in enumerate(self.body):
            if index == 0:
                cube.draw(cell_width, draw_rect, draw_circle, True)
            else:
                cube.draw(cell_width, draw_rect)

    def remove_tail_from_turns(self, index, position):
        if index == len(self.body) - 1:
            self.turns.pop(position)

    def update_direction(self, direction):
        self.direction = direction
        self.turns[self.head.position] = self.direction
