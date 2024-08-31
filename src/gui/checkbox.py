"""
This module defines the Checkbox class, an interactive element allowing
users to make a binary choice.
"""
import pygame

from src.constants import BLACK, WHITE
from src.gui.interactive import Interactive


class Checkbox(Interactive):
    """
    A class allowing users to make a binary choice.

    Attributes
    ----------
    position : tuple[int, int]
        The x, y coordinates of the element.
    size : tuple[int, int]
        The width and height of the element.
    name : str
        The name of the element.
    background_colour : pygame.Color | None, optional
        The colour of the element's border. Defaults to None.
    border_colour : pygame.Color | None, optional
        The colour of the element's background. Defaults to None.
    border_width : int, optional
        The width of the element's border. Defaults to 4.
    border_radius: int, optional
        The radius of the border's rounded corners. Defaults to 0
        (rectangle without rounded corners).
    is_enabled : bool
        A flag indicating whether the element is displayed.
    is_active : bool
        A flag indicating whether the element is active.
    rect : pygame.Rect
        The rectangular area occupied by the element.

    Methods
    -------
    draw(surface: pygame.Surface) -> None
        Draws the element on the provided surface if enabled.
    set_rect() -> None
        Sets the rectangular area occupied by the element based on its
        position and size.
    is_clicked(mouse_pos: tuple[int, int]) -> bool
        Detects whether the mouse clicks the element.
    clicked() -> None
        Peform function after element is clicked.
    """

    def __init__(
        self,
        position: tuple[int, int] = (0, 0),
        size: tuple[int, int] = (25, 25),
        name: str = "",
        background_colour: pygame.Color = WHITE,
        border_colour: pygame.Color = BLACK,
        border_width: int = 4,
        border_radius: int = 0,
        is_enabled: bool = True,
        is_active: bool = False,
    ) -> None:
        """
        Initialises a new instance of the Checkbox class.

        Parameters
        ----------
        position : tuple[int, int], optional
            The x, y coordinates of the element. Defaults to (0, 0).
        size : tuple[int, int], optional
            The width and height of the element. Defaults to (25, 25).
        name : str, optional
            The name of the element. Defaults to an empty string.
        background_colour : pygame.Color, optional
            The colour of the element's border. Defaults to white.
        border_colour : pygame.Color, optional
            The colour of the element's background. Defaults to black.
        border_width : int, optional
            The width of the element's border. Defaults to 4.
        border_radius: int, optional
            The radius of the border's rounded corners. Defaults to 0
            (rectangle without rounded corners).
        is_enabled : bool, optional
            A flag indicating whether the element is displayed. Defaults
            to True.
        is_active : bool
            A flag indicating whether the element is active. Defaults to
            False.
        """
        super().__init__(
            position,
            size,
            name,
            background_colour,
            border_colour,
            border_width,
            border_radius,
            is_enabled,
            is_active,
        )

    def draw(self, surface: pygame.Surface) -> None:
        """
        Draws the element on the provided surface if enabled.

        Parameters
        ----------
        surface: pygame.Surface
            The surface on which the element will be drawn on.

        Returns
        -------
        None
        """
        if self.is_active:
            pygame.draw.rect(surface, WHITE, self.rect)
        pygame.draw.rect(
            surface, BLACK, self.rect, self.border_width, self.border_radius
        )

    def clicked(self) -> None:
        """
        Peform function after element is clicked.

        Returns
        -------
        None
        """
        self.is_active = not self.is_active
