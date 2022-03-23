import pygame
import random

WIN_HEIGHT = 480
WIN_WIDTH = 800

BLACK = (0, 0, 0)
WHITE = (255, 255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (102, 255, 255)


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.window = self.set_window()
        self.buttons = self.set_buttons()
        self.fonts = self.set_fonts()

    def set_fonts(self):
        button_font = pygame.font.SysFont("arial", 20)
        guess_font = pygame.font.SysFont("monospace", 24)
        lost_font = pygame.font.SysFont('arial', 45)
        return {'button_font': button_font, 'guess_font': guess_font, 'lost_font': lost_font}

    def set_window(self):
        return pygame.display.set_mode((self.width, self.height))

    def set_buttons(self):
        buttons = []
        increase = round(self.width / 13)
        for i in range(26):
            if i < 13:
                y = 40
                x = 25 + (increase * i)
            else:
                x = 25 + (increase * (i - 13))
                y = 85
            buttons.append(Button(LIGHT_BLUE, x, y, 20, True, 65 + i))
            return buttons


class Password:
    def __init__(self):
        self.password = self.set_password()

    def set_password(self, filename="words.txt"):
        file = open(filename)
        words_list = file.readlines()
        random_word_index = random.randrange(0, len(words_list) - 1)
        return words_list[random_word_index][:-1]



class Button:
    def __init__(self, color, pos_x, pos_y, radius, visible, char):
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radius = radius
        self.visible = visible
        self.char = char


# buttons = []
# increase = round(WIN_WIDTH / 13)
# for i in range(26):
#     if i < 13:
#         y = 40
#         x = 25 + (increase * i)
#     else:
#         x = 25 + (increase * (i - 13))
#         y = 85
#     buttons.append(Button(LIGHT_BLUE, x, y, 20, True, 65 + i))
#     # buttons.append([color, x_pos, y_pos, radius, visible, char])
# return buttons


pygame.init()
b = Board(400, 800)
print(b.fonts)
# pygame.display.set_caption("HANGMAN GAME")
# win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
# button_font = pygame.font.SysFont("arial", 20)
#
# for button in buttons:
#     pygame.draw.circle(win, BLACK, (button.pos_x, button.pos_y), button.radius)
#     pygame.draw.circle(win, button.color, (button.pos_x, button.pos_y), button.radius - 2)
#     label = button_font.render(chr(button.char), 1, BLACK)
#     win.blit(label, (button.pos_x - (label.get_width() / 2), button.pos_y - (label.get_height() / 2)))
#
# pygame.display.update()
input("dajesz mordo: ")

pygame.quit()