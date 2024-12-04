import pygame

DISPLAY_WIDTH = 900
DISPLAY_HEIGHT = 700

BACKGROUND_COLOR = (34,139,34)
GREY = (220,220,220)
BLACK = (0,0,0)
GREEN = (0, 200, 0)
RED = (255,0,0)
LIGHT_SLAT = (119,136,153)
DARK_SLAT = (47, 79, 79)
DARK_RED = (255, 0, 0)
pygame.init()
font = pygame.font.SysFont("Arial", 20)
textfont = pygame.font.SysFont('Comic Sans MS', 35)
game_end = pygame.font.SysFont('dejavusans', 100)
blackjack = pygame.font.SysFont('roboto', 70)


SUITS = ['C', 'S', 'H', 'D']
VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)