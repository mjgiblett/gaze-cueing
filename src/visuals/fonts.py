"""
Defines system fonts after pygame initialisation. 
"""
import pygame

from src.constants import FONT_PROPERTIES

fonts: dict[str, pygame.font.Font] = {}


def init_fonts() -> None:
    """
    Initialises fonts. Should be called immediantly after pygame initialisation.
    """
    fonts.update(
        {
            name: pygame.font.SysFont(**kwargs)
            for name, kwargs in FONT_PROPERTIES.items()
        }
    )
