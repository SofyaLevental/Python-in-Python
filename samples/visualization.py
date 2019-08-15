import tkinter
from tkinter import messagebox

import pygame

from samples.utils import BLACK, WHITE


class Timer:
    def __init__(self):
        self.clock = pygame.time.Clock()

    def delay(self):
        pygame.time.delay(50)
        self.clock.tick(6)


class Popup:
    @staticmethod
    def show(subject, content):
        root = tkinter.Tk()
        root.attributes("-topmost", True)
        root.withdraw()
        messagebox.showinfo(subject, content)
        root.destroy()


class Window:
    def __init__(self, width, cells):
        self.width = width
        self.cells = cells
        self.cell_width = self.width // self.cells
        self.window = pygame.display.set_mode((width + 1, width + 1))
        pygame.display.set_caption("Python Game")

    @staticmethod
    def quit_game():
        pygame.quit()

    def redraw_window(self, python, food):
        self.window.fill(BLACK)
        python.draw(self.cell_width, self.draw_rect, self.draw_circle)
        food.draw(self.cell_width, self.draw_rect)
        self.draw_grid()
        pygame.display.update()

    def draw_rect(self, rect, color):
        pygame.draw.rect(self.window, color, rect)

    def draw_circle(self, eye_middle, radius):
        pygame.draw.circle(self.window, BLACK, (eye_middle.x, eye_middle.y), radius)

    def draw_grid(self):
        x = 0
        y = 0
        for i in range(self.cells + 1):
            self.draw_line((0, y), (self.width, y))
            self.draw_line((x, 0), (x, self.width))
            x = x + self.cell_width
            y = y + self.cell_width

    def draw_line(self, begin, end):
        pygame.draw.line(self.window, WHITE, begin, end)
