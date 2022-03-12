import pygame
import random


# GLOBAL VARIABLES

WIN_HEIGHT = 480
WIN_WIDTH = 800

BLACK = (0, 0, 0)
WHITE = (255, 255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (102, 255, 255)

WORD = ''
BUTTONS = []
GUESSED = []
HANGMAN_PICS = [pygame.image.load('hangman0.png')]
LIMBS = 0


def get_random_word():
    file = open('words.txt')
    words_list = file.readlines()
    random_word_index = random.randrange(0, len(words_list) - 1)

    return words_list[random_word_index][:-1]


def redraw_window(window, buttons, font):
    global GUESSED
    global HANGMAN_PICS
    global LIMBS
    window.fill(GREEN)
    for i in range(len(buttons)):
        if buttons[i][4]:
            pygame.draw.circle(window, BLACK, (buttons[i][1], buttons[i][2]), buttons[i][3])
            pygame.draw.circle(window, buttons[i][0], (buttons[i][1], buttons[i][2]), buttons[i][3] - 2
                               )
            label = font.render(chr(buttons[i][5]), 1, BLACK)
            window.blit(label, (buttons[i][1] - (label.get_width() / 2), buttons[i][2] - (label.get_height() / 2)))
    pygame.display.update()
    input("dajesz mordo: ")
    return window


def hide_password(password):
    """
    Return hidden password
    :param password: string 'password'
    :return: hidden_password in format '_ _ _ _ _ _ _'
    """
    hidden_password = ''
    known_letters = GUESSED
    for x in range(len(password)):
        if password[x] != ' ':
            hidden_password += '_ '
            for i in range(len(known_letters)):
                if password[x].upper() == known_letters[i].upper():
                    hidden_password = hidden_password[:-2]
                    hidden_password += password[x].upper() + ' '
        elif password[x] == ' ':
            hidden_password += ' '
    return hidden_password


def create_buttons():
    """

    :return:
    """
    buttons = []
    increase = round(WIN_WIDTH / 13)
    for i in range(26):
        if i < 13:
            y = 40
            x = 25 + (increase * i)
        else:
            x = 25 + (increase * (i - 13))
            y = 85
        buttons.append([LIGHT_BLUE, x, y, 20, True, 65 + i])
        # buttons.append([color, x_pos, y_pos, radius, visible, char])
    return buttons


if __name__ == '__main__':
    pygame.init()
    win = pygame.display.set_mode((WIN_HEIGHT, WIN_WIDTH))
    button_font = pygame.font.SysFont("arial", 20)
    guess_font = pygame.font.SysFont("monospace", 24)
    lost_font = pygame.font.SysFont('arial', 45)
    buttons = create_buttons()
    redraw_window(window=win, buttons=buttons, font=button_font)
    #
    # pygame.quit()


# f = input("dajesz mordo: ")
#
# win.fill(BLUE)
# pygame.display.update()
# f = input("dajesz mordo: ")


# f = input("dajesz mordo: ")




