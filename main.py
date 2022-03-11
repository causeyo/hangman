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
HANGMAN_PICS =  [pygame.image.load('hangman0.png')]
LIMBS = 0


def get_random_word():
    file = open('words.txt')
    words_list = file.readlines()
    random_word_index = random.randrange(0, len(words_list) - 1)

    return words_list[random_word_index][:-1]


def redraw_window():
    global GUESSED
    global HANGMAN_PICS
    global LIMBS
    win.fill(GREEN)
    pic = pygame.image.load('hangman0.png')
    win.blit(pic, (WIN_WIDTH / 2 - pic.get_width() / 2 + 20, 50))
    pygame.display.update()
    input("dajesz mordo: ")
    for i in range(len(BUTTONS)):
        if BUTTONS[i][4]:
            pygame.draw.circle(win, BLACK, (BUTTONS[i][1], BUTTONS[i][2]), BUTTONS[i][3])
            pygame.draw.circle(win, BUTTONS[i][0], (BUTTONS[i][1], BUTTONS[i][2]), BUTTONS[i][3] - 2
                               )
            label = btn_font.render(chr(BUTTONS[i][5]), 1, BLACK)
            win.blit(label, (BUTTONS[i][1] - (label.get_width() / 2), BUTTONS[i][2] - (label.get_height() / 2)))


def spacedOut(word):
    spacedWord = ''
    guessedLetters = GUESSED
    for x in range(len(word)):
        if word[x] != ' ':
            spacedWord += '_ '
            for i in range(len(guessedLetters)):
                if word[x].upper() == guessedLetters[i].upper():
                    spacedWord = spacedWord[:-2]
                    spacedWord += word[x].upper() + ' '
        elif word[x] == ' ':
            spacedWord += ' '
    return spacedWord


if __name__ == '__main__':
    # pygame.init()
    # win = pygame.display.set_mode((WIN_HEIGHT, WIN_WIDTH))
    # btn_font = pygame.font.SysFont("arial", 20)
    # guess_font = pygame.font.SysFont("monospace", 24)
    # lost_font = pygame.font.SysFont('arial', 45)
    # redraw_window()
    #
    # pygame.quit()


# f = input("dajesz mordo: ")
#
# win.fill(BLUE)
# pygame.display.update()
# f = input("dajesz mordo: ")


# f = input("dajesz mordo: ")




