import pygame

from samples.utils import BLACK, WHITE


class Timer:
    def __init__(self):
        self.clock = pygame.time.Clock()

    def delay(self, time):
        pygame.time.delay(time)
        self.clock.tick(6)


class Window:
    __in_game = False

    def __init__(self, cell_width, number_of_cells):
        self.cell_width = cell_width
        self.number_of_cells = number_of_cells
        self.width = self.cell_width * self.number_of_cells
        pygame.init()
        self.__in_game = True
        self.window = pygame.display.set_mode((self.width + 1, self.width + 1))
        pygame.display.set_caption("Python Game")

    def quit_game(self):
        self.__in_game = False
        pygame.quit()
        quit()

    def show_message(self, subject, content):
        font = pygame.font.Font('freesansbold.ttf', 32)
        self.__blit_text(font, subject, self.width / 2 - self.cell_width)
        self.__blit_text(font, content, self.width / 2 + self.cell_width)
        pygame.display.update()

    def redraw_window(self, python, food):
        self.window.fill(BLACK)
        python.draw(self.cell_width, self.__draw_rect, self.__draw_circle)
        food.draw(self.cell_width, self.__draw_rect)
        self.__draw_grid()
        pygame.display.update()

    def is_in_game(self):
        return self.__in_game

    def __blit_text(self, font, text, j_position):
        rended_text = font.render(text, True, WHITE, BLACK)
        rended_text_rect = rended_text.get_rect()
        rended_text_rect.center = (self.width / 2, j_position)
        self.window.blit(rended_text, rended_text_rect)

    def __draw_rect(self, rect, color):
        pygame.draw.rect(self.window, color, rect)

    def __draw_circle(self, eye_middle, radius):
        pygame.draw.circle(self.window, BLACK, (eye_middle.get_x(), eye_middle.get_y()), radius)

    def __draw_grid(self):
        x = 0
        y = 0
        for i in range(self.number_of_cells + 1):
            self.__draw_line((0, y), (self.width, y))
            self.__draw_line((x, 0), (x, self.width))
            x = x + self.cell_width
            y = y + self.cell_width

    def __draw_line(self, begin, end):
        pygame.draw.line(self.window, WHITE, begin, end)
