import pygame
import random


def randomWord():
    file = open('words.txt')
    words_list = file.readlines()
    random_word_index = random.randrange(0, len(words_list) - 1)

    return words_list[random_word_index][:-1]


pygame.init()
winHeight = 480
winWidth = 700
win=pygame.display.set_mode((winWidth,winHeight))

# GLOBAL VARIABLES

BLACK = (0, 0, 0)
WHITE = (255, 255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (102, 255, 255)

btn_font = pygame.font.SysFont("arial", 20)
guess_font = pygame.font.SysFont("monospace", 24)
lost_font = pygame.font.SysFont('arial', 45)
word = ''
buttons = []
guessed = []

win.fill(GREEN)
pygame.display.update()
# f = input("dajesz mordo: ")
#
# win.fill(BLUE)
# pygame.display.update()
# f = input("dajesz mordo: ")

pic = pygame.image.load('hangman0.png')
win.blit(pic, (winWidth/2 - pic.get_width()/2 + 20, 50))
pygame.display.update()
# f = input("dajesz mordo: ")

pygame.quit()


