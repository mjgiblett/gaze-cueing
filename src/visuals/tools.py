"""
Defines visual utility functions, including a display for framerate.
"""

import pygame

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
