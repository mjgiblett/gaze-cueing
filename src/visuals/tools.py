"""
Defines visual utility functions, including displays for framerate and 
trial information. 
"""

import pygame
from pandas import Series

from src.constants import BLACK


def show_fps(
    surface: pygame.Surface, clock: pygame.time.Clock, font: pygame.font.Font
) -> None:
    """
    Displays the application's framerate in the top left corner.

    Parameters
    ----------
    surface: pygame.Surface
        The surface on which the framerate will be drawn on.
    clock: pygame.time.Clock
        The pygame clock regulating the application's framerate.
    font: pygame.font.Font
        The font of the text displaying the framerate.

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
        The surface on which the trial information will be drawn on.
    trial: pandas.Series
        An array of trial variables.
    font: pygame.font.Font
        The font of the text displaying the information.

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
