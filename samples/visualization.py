import pygame

from samples.utils import BLACK, WHITE


class Timer:
    def __init__(self):
        self.clock = pygame.time.Clock()

    def delay(self, time):
        pygame.time.delay(time)
        self.clock.tick(6)


class Window:
    def __init__(self, width, cells):
        self.width = width
        self.cells = cells
        self.cell_width = self.width // self.cells
        pygame.init()
        self.window = pygame.display.set_mode((width + 1, width + 1))
        pygame.display.set_caption("Python Game")

    @staticmethod
    def quit_game():
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

    def __blit_text(self, font, text, j_position):
        rended_text = font.render(text, True, WHITE, BLACK)
        rended_text_rect = rended_text.get_rect()
        rended_text_rect.center = (self.width / 2, j_position)
        self.window.blit(rended_text, rended_text_rect)

    def __draw_rect(self, rect, color):
        pygame.draw.rect(self.window, color, rect)

    def __draw_circle(self, eye_middle, radius):
        pygame.draw.circle(self.window, BLACK, (eye_middle.x, eye_middle.y), radius)

    def __draw_grid(self):
        x = 0
        y = 0
        for i in range(self.cells + 1):
            self.__draw_line((0, y), (self.width, y))
            self.__draw_line((x, 0), (x, self.width))
            x = x + self.cell_width
            y = y + self.cell_width

    def __draw_line(self, begin, end):
        pygame.draw.line(self.window, WHITE, begin, end)
