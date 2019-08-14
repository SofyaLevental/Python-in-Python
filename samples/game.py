import random
import tkinter
from tkinter import messagebox

import paho.mqtt.client
import pygame

from samples.keys_publisher import Publisher
from samples.objects import Cube, Snake
from samples.utils import Cell, Vector, GREEN, BLACK, WHITE


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
    window = pygame.display.set_mode((width + 1, width + 1))
    python = Snake(Cell(10, 10))
    food = create_food()
    flag = True
    clock = pygame.time.Clock()
    publisher = Publisher()
    subscribe_for_keys()

    while flag:
        pygame.time.delay(50)
        clock.tick(6)
        publisher.listen_to_keyboard_events()
        python.move(cells)
        if python.get_head().position.i == food.position.i and python.get_head().position.j == food.position.j:
            food = create_food()
        else:
            body = python.get_body()
            del body[-1]
            python.set_body(body)
        redraw_window()

        for index in range(len(python.get_body())):
            if python.get_body()[index].position in list(map(lambda cube: cube.position, python.get_body()[index + 1:])):
                message_box("You Lost!", "Your Score: " + str(len(python.get_body())))
                python.reset(Cell(10, 10))
                break


def subscribe_for_keys():
    client = paho.mqtt.client.Client("keysSub")
    client.on_message = on_message
    client.connect("localhost")
    client.loop_start()
    client.subscribe("keys")


def on_message(client, userdata, message):
    key = str(message.payload.decode("utf-8"))
    switcher = {
        'L': Vector(-1, 0),
        'R': Vector(1, 0),
        'U': Vector(0, -1),
        'D': Vector(0, 1)
    }
    python.update_direction(switcher.get(key))


def create_food():
    return Cube(create_random_food_position(), color=GREEN)


def redraw_window():
    window.fill((0, 0, 0))
    python.draw(cell_width, draw_rect, draw_circle)
    food.draw(cell_width, draw_rect)
    draw_grid()
    pygame.display.update()


def draw_rect(rect, color):
    pygame.draw.rect(window, color, rect)


def draw_circle(eye_middle, radius):
    pygame.draw.circle(window, BLACK, (eye_middle.x, eye_middle.y), radius)


def draw_grid():
    x = 0
    y = 0
    for i in range(cells + 1):
        pygame.draw.line(window, WHITE, (0, y), (width, y))
        pygame.draw.line(window, WHITE, (x, 0), (x, width))
        x = x + cell_width
        y = y + cell_width


def create_random_food_position():
    snake_body_cubes = python.get_body()

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
