import random
import tkinter
from tkinter import messagebox
import pygame

from samples.objects import Cube
from samples.utils import Cell, Vector, Point


class Game:
    def __init__(self):
        pass


class Snake:

    def __init__(self, position, color=(255, 0, 0)):
        self.reset(position)
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

    def move(self):
        first_cell = 0
        last_cell = cells - 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.update_direction(Vector(-1, 0))
                elif keys[pygame.K_RIGHT]:
                    self.update_direction(Vector(1, 0))
                elif keys[pygame.K_UP]:
                    self.update_direction(Vector(0, -1))
                elif keys[pygame.K_DOWN]:
                    self.update_direction(Vector(0, 1))

        for index, cube in enumerate(self.body):
            position = cube.position
            if position in self.turns:
                turn = self.turns[position]
                cube.move(turn)
                self.remove_tail_from_turns(index, position)
            else:
                if cube.direction.i == -1 and cube.position.i == first_cell:
                    cube.position = Cell(last_cell, cube.position.j)
                elif cube.direction.i == 1 and cube.position.i == last_cell:
                    cube.position = Cell(first_cell, cube.position.j)
                elif cube.direction.j == -1 and cube.position.j == first_cell:
                    cube.position = Cell(cube.position.i, last_cell)
                elif cube.direction.j == 1 and cube.position.j == last_cell:
                    cube.position = Cell(cube.position.i, first_cell)
                else:
                    cube.move(cube.direction)

    def draw(self):
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


def message_box(subject, content):
    root = tkinter.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


def main():
    global width, cells, cell_width, window, python, food
    width = 500
    cells = 20
    cell_width = width // cells
    window = pygame.display.set_mode((width, width))
    python = Snake(Cell(10, 10))
    food = create_food()
    flag = True
    clock = pygame.time.Clock()
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        python.move()
        if python.body[0].position.i == food.position.i and python.body[0].position.j == food.position.j:
            python.add_cube()
            food = create_food()
        redraw_window()

        for index in range(len(python.body)):
            if python.body[index].position in list(map(lambda cube: cube.position, python.body[index + 1:])):
                print("Score: ", len(python.body))
                message_box("You Lost!", "Your Score: " + str(len(python.body)))
                python.reset(Cell(10, 10))
                break


def create_food():
    return Cube(create_random_food_position(), color=(0, 255, 0))


def redraw_window():
    window.fill((0, 0, 0))
    python.draw()
    food.draw(cell_width, draw_rect)
    draw_grid()
    pygame.display.update()


def draw_rect(rect, color):
    pygame.draw.rect(window, color, rect)


def draw_circle(eye_middle, radius):
    pygame.draw.circle(window, (0, 0, 0), (eye_middle.x, eye_middle.y), radius)


def draw_grid():
    x = 0
    y = 0
    for i in range(cells):
        x = x + cell_width
        y = y + cell_width
        pygame.draw.line(window, (255, 255, 255), (0, y), (width, y))
        pygame.draw.line(window, (255, 255, 255), (x, 0), (x, width))


def create_random_food_position():
    snake_body_cubes = python.body

    while True:
        i_food_position = random.randrange(cells)
        j_food_position = random.randrange(cells)
        if len(list(
                filter(lambda cube: is_food_on_body_cube(cube, i_food_position, j_food_position),
                       snake_body_cubes))) > 0:
            continue
        else:
            break

    return Cell(i_food_position, j_food_position)


def is_food_on_body_cube(cube, i_food_position, j_food_position):
    return cube.position.i == i_food_position and cube.position.j == j_food_position


main()
