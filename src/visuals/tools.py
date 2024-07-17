"""
Defines visual utility functions.
"""

import pygame
from pandas import Series

from src.constants import BLACK


def show_fps(
    surface: pygame.Surface, clock: pygame.time.Clock, font: pygame.font.Font
) -> None:
    """
    Displays application framerate in the top left corner.
    Parameters
    ----------
    surface: pygame.Surface
        Main window displaying the experiment.
    clock: pygame.time.Clock
        Pygame clock regulating the game's framerate.
    font: pygame.font.Font
        Font used to display the framerate.
    Returns
    -------
    None
    """
    fps_text = font.render(f"FPS: {clock.get_fps():.0f}", True, BLACK)
    surface.blit(fps_text, (5, 5))


def show_trial(screen: pygame.Surface, trial: Series, font: pygame.font.Font) -> None:
    """
    Displays information regarding the previous experimental trial.
    Parameters
    ----------
    surface: pygame.Surface
        Main window displaying the experiment.
    trial: pandas.Series
        Array of trial variables.
    font: pygame.font.Font
        Font used to display the framerate.
    Returns
    -------
    None
    """
    y = 50
    height = font.size(" ")[1]
    for key, val in trial.items():
        text = font.render(f"{key}: {val}", True, BLACK)
        screen.blit(text, (5, y))
        y += height
    text = font.render(f"trial_number: {trial.name}", True, BLACK)
    screen.blit(text, (5, y))
