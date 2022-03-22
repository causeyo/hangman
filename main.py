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
HANGMAN_PICS = [pygame.image.load('hangman0.png'), pygame.image.load('hangman1.png'), pygame.image.load('hangman2.png'),
                pygame.image.load('hangman3.png'), pygame.image.load('hangman4.png'), pygame.image.load('hangman5.png'),
                pygame.image.load('hangman6.png')]
LIMBS = 0


def get_random_word(filename="words.txt"):
    file = open(filename)
    words_list = file.readlines()
    random_word_index = random.randrange(0, len(words_list) - 1)

    return words_list[random_word_index][:-1]


def redraw_window(window, buttons, font, password, guessed_letters):
    global GUESSED
    global HANGMAN_PICS
    global LIMBS
    window.fill(GREEN)
    for button in buttons:
        if button[4]:
            pygame.draw.circle(window, BLACK, (button[1], button[2]), button[3])
            pygame.draw.circle(window, button[0], (button[1], button[2]), button[3] - 2)
            label = font.render(chr(button[5]), 1, BLACK)
            window.blit(label, (button[1] - (label.get_width() / 2), button[2] - (label.get_height() / 2)))
    password = hide_password(password, guessed_letters)
    password_label = font.render(password, 1, BLACK)
    frame = password_label.get_rect()
    frame_length = frame[2]
    window.blit(password_label, (WIN_WIDTH/2 - frame_length/2, 400))
    pic = HANGMAN_PICS[limbs]
    win.blit(pic, (WIN_WIDTH / 2 - pic.get_width() / 2 + 20, 150))

    pygame.display.update()
    # input("dajesz mordo: ")
    return window


def hide_password(password, guessed_letters):
    """
    Return hidden password
    :param password: string 'password'
    :return: hidden_password in format '_ _ _ _ _ _ _'
    """
    hidden_password = ''
    known_letters = guessed_letters
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


def button_push(x, y):
    for button in buttons:
        if button[1] - 20 < x < button[1] + 20:
            if button[2] - 20 < y < button[2] + 20:
                return button[5]
    return None


def hang(guess, word):
    if guess.lower() not in word.lower():
        return True
    else:
        return False


def end(word, winner=False):
    global limbs
    lostTxt = 'You Lost, press any key to play again...'
    winTxt = 'WINNER!, press any key to play again...'
    # redraw_window(window=win, buttons=buttons, font=button_font, password=random_word, guessed_letters=GUESSED)
    pygame.time.delay(1000)
    win.fill(GREEN)

    if winner == True:
        label = lost_font.render(winTxt, 1, BLACK)
    else:
        label = lost_font.render(lostTxt, 1, BLACK)

    wordTxt = lost_font.render(word.upper(), 1, BLACK)
    wordWas = lost_font.render('The phrase was: ', 1, BLACK)

    win.blit(wordTxt, (WIN_WIDTH/2 - wordTxt.get_width()/2, 295))
    win.blit(wordWas, (WIN_WIDTH/2 - wordWas.get_width()/2, 245))
    win.blit(label, (WIN_WIDTH / 2 - label.get_width() / 2, 140))
    pygame.display.update()
    again = True
    while again:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                again = False
    reset()


def reset():
    global limbs
    global guessed
    global buttons
    global word
    for button in buttons:
        button[4] = True

    limbs = 0
    guessed = []
    word = get_random_word(filename="words.txt")


if __name__ == '__main__':
    pygame.init()
    random_word = get_random_word(filename="words.txt")
    pygame.display.set_caption("HANGMAN GAME")
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    print(win.get_height())
    button_font = pygame.font.SysFont("arial", 20)
    guess_font = pygame.font.SysFont("monospace", 24)
    lost_font = pygame.font.SysFont('arial', 45)
    buttons = create_buttons()
    active_game = True
    limbs = 0
    while active_game:
        redraw_window(window=win, buttons=buttons, font=button_font, password=random_word, guessed_letters=GUESSED)

        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active_game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    active_game = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_pos = pygame.mouse.get_pos()
                letter = button_push(click_pos[0], click_pos[1])
                if letter:
                    GUESSED.append(chr(letter))
                    buttons[letter - 65][4] = False
                    if hang(chr(letter), random_word):
                        if limbs != 5:
                            limbs += 1
                            print(limbs)
                        else:
                            # active_game = False
                            end(word=random_word, winner=False)
    pygame.quit()


# f = input("dajesz mordo: ")
#
# win.fill(BLUE)
# pygame.display.update()
# f = input("dajesz mordo: ")


# f = input("dajesz mordo: ")
