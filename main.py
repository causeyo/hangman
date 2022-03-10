import pygame
import random


# GLOBAL VARIABLES

WIN_HEIGHT = 480
WIN_WIDTH = 700

BLACK = (0, 0, 0)
WHITE = (255, 255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (102, 255, 255)

WORD = ''
BUTTONS = []
GUESSED = []


def get_random_word():
    file = open('words.txt')
    words_list = file.readlines()
    random_word_index = random.randrange(0, len(words_list) - 1)

    return words_list[random_word_index][:-1]


def redraw_window():
    win.fill(GREEN)
    pygame.display.update()
    pic = pygame.image.load('hangman0.png')
    win.blit(pic, (WIN_WIDTH / 2 - pic.get_width() / 2 + 20, 50))
    pygame.display.update()
    input("dajesz mordo: ")


if __name__ == '__main__':
    pygame.init()
    win = pygame.display.set_mode((WIN_HEIGHT, WIN_WIDTH))
    redraw_window()
    btn_font = pygame.font.SysFont("arial", 20)
    guess_font = pygame.font.SysFont("monospace", 24)
    lost_font = pygame.font.SysFont('arial', 45)

    pygame.quit()



# f = input("dajesz mordo: ")
#
# win.fill(BLUE)
# pygame.display.update()
# f = input("dajesz mordo: ")


# f = input("dajesz mordo: ")




