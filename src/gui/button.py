"""
This module defines the Button class, an interactive element allowing
users to trigger an event.
"""
import pygame

from src.constants import BLACK
from src.gui.interactive_text import InteractiveText
from src.visuals import Text


class Button(InteractiveText):
    """
    A class allowing users to trigger an event.

    Attributes
    ----------
    text : Text
        The Text of the element.
    position : tuple[int, int]
        The x, y coordinates of the element.
    size : tuple[int, int]
        The width and height of the element.
    name : str
        The name of the element.
    background_colour : pygame.Color | None
        The colour of the element's border.
    border_colour : pygame.Color | None
        The colour of the element's background.
    border_width : int
        The width of the element's border.
    border_radius: int
        The radius of the border's rounded corners.
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
        text: Text,
        position: tuple[int, int] = (0, 0),
        size: tuple[int, int] = (60, 30),
        name: str = "",
        background_colour: pygame.Color | None = BLACK,
        border_colour: pygame.Color | None = None,
        border_width: int = 4,
        border_radius: int = 30,
        is_enabled: bool = True,
        is_active: bool = False,
    ) -> None:
        """
        Initialises a new instance of the Button class.

        Parameters
        ----------
        text : Text
            The Text of the element.
        position : tuple[int, int], optional
            The x, y coordinates of the element. Defaults to (0, 0).
        size : tuple[int, int], optional
            The width and height of the element. Defaults to (60, 30).
        name : str, optional
            The name of the element. Defaults to an empty string.
        background_colour : pygame.Color | None, optional
            The colour of the element's border. Defaults to black.
        border_colour : pygame.Color | None, optional
            The colour of the element's background. Defaults to None.
        border_width : int, optional
            The width of the element's border. Defaults to 4.
        border_radius: int, optional
            The radius of the border's rounded corners. Defaults to 30.
        is_enabled : bool, optional
            A flag indicating whether the element is displayed. Defaults
            to True.
        is_active : bool
            A flag indicating whether the element is active. Defaults to
            False.
        """
        super().__init__(
            text,
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

    def clicked(self) -> None:
        """
        Peform function after element is clicked.

        Returns
        -------
        None
        """
        self.is_active = True
