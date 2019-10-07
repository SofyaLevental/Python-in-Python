import random

from samples.utils import Vector, Cell, Point, RED, GREEN


class Cube:
    def __init__(self, position, direction=Vector(1, 0), color=RED):
        self.__position = position
        self.__direction = direction
        self.__color = color

    def move(self, cells, direction):
        self.set_direction(direction)
        position = Cell(
            self.__modulus_cells(self.get_position().get_i() + self.get_direction().get_i(), cells),
            self.__modulus_cells(self.get_position().get_j() + self.get_direction().get_j(), cells)
        )
        self.set_position(position)

    def draw(self, cell_width, draw_rect, draw_circle=None, eyes=False):
        rect = (
            self.get_position().get_i() * cell_width + 1,
            self.get_position().get_j() * cell_width + 1,
            cell_width - 1,
            cell_width - 1
        )

        draw_rect(rect, self.get_color())
        if eyes:
            self.__draw_eyes(cell_width, draw_circle)

    def is_on_cube(self, cube_position):
        return self.__position == cube_position

    def get_position(self):
        return self.__position

    def set_position(self, position):
        self.__position = position

    def get_direction(self):
        return self.__direction

    def set_direction(self, direction):
        self.__direction = direction

    def get_color(self):
        return self.__color

    @staticmethod
    def __modulus_cells(number, cells):
        return number % cells

    def __draw_eyes(self, cell_width, draw_circle):
        half_cell_width = cell_width // 2
        cube_center = Point(
            self.get_position().get_i() * cell_width + 1 + half_cell_width,
            self.get_position().get_j() * cell_width + 1 + half_cell_width
        )
        eye_radius = cell_width // 7
        eye_shift = cell_width // 4
        left_eye_middle = Point(cube_center.get_x() - eye_shift, cube_center.get_y())
        right_eye_middle = Point(cube_center.get_x() + eye_shift, cube_center.get_y())
        draw_circle(left_eye_middle, eye_radius)
        draw_circle(right_eye_middle, eye_radius)

    def __eq__(self, cube):
        return self.get_position() == cube.get_position() \
               and self.get_direction() == cube.get_direction() \
               and self.get_color() == cube.get_color()

    def __hash__(self):
        return hash((self.get_position(), self.get_direction(), self.get_color()))


class Snake:
    def __init__(self, position):
        self.__body = []
        self.__body.append(Cube(position))

    def reset(self, position):
        self.__init__(position)

    def move(self, cells):
        new_head = Cube(self.get_head().get_position(), self.get_head().get_direction())
        new_head.move(cells, new_head.get_direction())
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
        head.set_direction(direction)
        self.set_head(head)

    def create_food(self, cells):
        return Cube(self.__create_random_food_position(cells), color=GREEN)

    def remove_tail(self):
        del self.__body[-1]

    def has_collision(self):
        return self.__get_number_of_cells_with_position_in_body(self.get_head().get_position()) > 1

    def get_score(self):
        return str(len(self.get_body())-2)

    def get_body(self):
        return self.__body

    def set_body(self, body):
        self.__body = body

    def get_head(self):
        return self.get_body()[0]

    def set_head(self, head):
        self.__body[0] = head

    def __create_random_food_position(self, cells):
        while True:
            new_food_position = Cell(random.randrange(cells), random.randrange(cells))
            if self.__get_number_of_cells_with_position_in_body(new_food_position) > 0:
                continue
            else:
                break

        return new_food_position

    def __get_number_of_cells_with_position_in_body(self, position):
        return len(list(filter(lambda cube: cube.is_on_cube(position), self.get_body())))
