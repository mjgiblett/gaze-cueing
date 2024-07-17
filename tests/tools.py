import pygame

from src.constants import DISPLAY_HEIGHT, DISPLAY_WIDTH
from src.visuals import fonts


def minimal_setup() -> pygame.Surface:
    pygame.init()
    fonts.init_fonts()
    return pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
