import pygame
import random

pygame.init()
winHeight = 480
winWidth = 700
win=pygame.display.set_mode((winWidth,winHeight))

# GLOBAL VARIABLES

BLACK = (0,0, 0)
WHITE = (255,255,255)
RED = (255,0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)
LIGHT_BLUE = (102,255,255)

win.fill(GREEN)
pygame.display.update()
f = input("dajesz mordo: ")

win.fill(BLUE)
pygame.display.update()
f = input("dajesz mordo: ")
