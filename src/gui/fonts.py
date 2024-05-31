"""
Defines system fonts after pygame initialisation. 
"""
import pygame

fonts: dict[str, pygame.font.Font] = {}


def init_fonts() -> None:
    """
    Initiates fonts. Should be called immediantly after pygame initialisation.
    """
    fonts["title"] = pygame.font.SysFont("timesnewroman", 75)
    fonts["heading"] = pygame.font.SysFont("timesnewroman", 50)
    fonts["text"] = pygame.font.SysFont("timesnewroman", 30)
    fonts["small"] = pygame.font.SysFont("timesnewroman", 20)
    fonts["button"] = pygame.font.SysFont("timesnewroman", 35, bold=True)
