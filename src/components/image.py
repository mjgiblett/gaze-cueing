"""
Defines Image class.
"""
import pygame

from src.gui.position import Position


class Image:
    """
    Represents an image surface and position.
    Attributes
    ----------
    surface: pygame.Surface
        The pygame surface of the image.
    pos: Position
        Position of the surface on the screen.
    Methods
    -------
    display()
        Displays the image.
    """

    def __init__(self, surface: pygame.Surface, pos: Position) -> None:
        self.surface = surface
        self.pos = pos

    def display(self, screen: pygame.Surface) -> None:
        screen.blit(self.surface, self.pos)
