"""
This module defines the FixationCross class. A fixation cross consists
of two intersecting rectangles centred on the screen, typically used in
psychological experiments to help participants focus their attention.
"""
import pygame

from src.constants import BLACK
from src.constants import FIXATION_CROSS_HEIGHT as HEIGHT
from src.constants import FIXATION_CROSS_WIDTH as WIDTH
from src.visuals.element import Element


class FixationCross(Element):
    """
    A class representing a fixation cross, composed of two intersecting
    rectangles at the centre of the screen.
    Used to display a fixation cross.

    Attributes
    ----------
    screen : pygame.Surface
        The main window displaying the experiment.
    size : tuple[int, int]
        The size of the fixation cross, defined by its height and width.
    name : str
        The name of the fixation cross.
    is_enabled : bool
        A flag indicating whether the fixation cross is displayed.

    Methods
    -------
    display(screen: pygame.Surface) -> None
        Renders the fixation cross on the provided screen.
    set_rect() -> None
        Sets the position and dimensions of the fixation cross rectangles.
    """

    def __init__(
        self,
        screen: pygame.Surface,
        size: tuple[int, int] = (HEIGHT, WIDTH),
        name: str = "",
        is_enabled: bool = True,
    ) -> None:
        """
        Initialises the FixationCross object.

        Parameters
        ----------
        screen : pygame.Surface
            The main window displaying the experiment.
        size : tuple[int, int], optional
            The size of the fixation cross. Defaults to
            (FIXATION_CROSS_HEIGHT, FIXATION_CROSS_WIDTH) from src.constants.
        name : str, optional
            The name of the fixation cross. Defaults to an empty string.
        is_enabled : bool, optional
            A flag indicating whether the fixation cross is enabled.
            Defaults to True.
        """
        position = screen.get_width() // 2, screen.get_height() // 2
        super().__init__(position, size, name, is_enabled)

    def display(self, screen: pygame.Surface) -> None:
        """
        Renders the fixation cross on the provided screen if it is enabled.

        Parameters
        ----------
        screen : pygame.Surface
            The main window displaying the experiment.
        """
        if not self.is_enabled:
            return
        for rect in self.rects:
            pygame.draw.rect(screen, BLACK, rect)

    def set_rect(self) -> None:
        """
        Sets the position and dimensions of the fixation cross rectangles.

        Returns
        -------
        None
        """
        super().set_rect()

        def create_rect(step: int) -> pygame.Rect:
            """
            Creates a rectangle for the fixation cross.

            Parameters
            ----------
            step : int
                Determines the direction of the size dimensions for the
                rectangle.

            Returns
            -------
            pygame.Rect
            """
            return pygame.Rect(
                [p - (s // 2) for p, s in zip(self.position, self.size[::step])],
                self.size[::step],
            )

        self.rects = [create_rect(1), create_rect(-1)]
