"""
Defines FixationCross class.
"""
import pygame

from src.constants import BLACK
from src.constants import FIXATION_CROSS_HEIGHT as HEIGHT
from src.constants import FIXATION_CROSS_WIDTH as WIDTH
from src.visuals.element import Element


class FixationCross(Element):
    """
    Contains two pygame rectangles located at the centre of the screen.
    Used to display a fixation cross.
    Attributes
    ----------
    screen: pygame.Surface
        The main window displaying the experiment.
    Methods
    -------
    display()
        Displays the fixation cross.
    """

    def __init__(self, screen: pygame.Surface) -> None:
        x = screen.get_width() // 2
        y = screen.get_height() // 2

        self.rects = [
            pygame.Rect(x - WIDTH // 2, y - HEIGHT // 2, WIDTH, HEIGHT),
            pygame.Rect(x - HEIGHT // 2, y - WIDTH // 2, HEIGHT, WIDTH),
        ]

    def display(self, screen: pygame.Surface) -> None:
        for rect in self.rects:
            pygame.draw.rect(screen, BLACK, rect)
