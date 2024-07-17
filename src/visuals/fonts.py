"""
Defines system fonts after pygame initialisation. 
"""
import pygame

fonts: dict[str, pygame.font.Font] = {}


def init_fonts() -> None:
    """
    Initiates fonts. Should be called immediantly after pygame initialisation.
    """
    fonts["title"] = pygame.font.SysFont("calibri", 75, bold=True)
    fonts["heading"] = pygame.font.SysFont("calibri", 40)
    fonts["text"] = pygame.font.SysFont("calibri", 30)
    fonts["small"] = pygame.font.SysFont("calibri", 20)
    fonts["button"] = pygame.font.SysFont("calibri", 30, bold=True)
