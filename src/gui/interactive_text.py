"""
This module defines a base class for interactive text GUI elements.
The InteractiveText class includes essential attributes such as text, 
position, size, name, colour, border, enabled, and active stutus.
"""
import pygame

from src.gui.interactive import Interactive
from src.visuals import Text


class InteractiveText(Interactive):
    """
    Base class for all interactive text GUI elements.

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
    not_clicked() -> None
        Peform function after element is not clicked.
    key_down(key: int) -> None
        Handles key down events.
    """

    def __init__(
        self,
        text: Text,
        position: tuple[int, int] = (0, 0),
        size: tuple[int, int] = (0, 0),
        name: str = "",
        background_colour: pygame.Color | None = None,
        border_colour: pygame.Color | None = None,
        border_width: int = 4,
        border_radius: int = 0,
        is_enabled: bool = True,
        is_active: bool = False,
    ) -> None:
        """
        Initialises a new instance of the InteractiveText class.

        Parameters
        ----------
        text : Text
            The Text of the element.
        position : tuple[int, int], optional
            The x, y coordinates of the element. Defaults to (0, 0).
        size : tuple[int, int], optional
            The width and height of the element. Defaults to (0, 0).
        name : str, optional
            The name of the element. Defaults to an empty string.
        background_colour : pygame.Color | None, optional
            The colour of the element's border. Defaults to None.
        border_colour : pygame.Color | None, optional
            The colour of the element's background. Defaults to None.
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
        self.text = text
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

    def set_rect(self) -> None:
        """
        Sets the rectangular area occupied by the element based on its
        position and size.

        Returns
        -------
        None
        """
        char_size = self.text.font.size("_")
        if any(
            [
                rect < (text + char_size[0])
                for rect, text in zip(self.size, self.text.rect.size)
            ]
        ):
            default_size = self.text.font.size("_" * 6)
            if default_size[0] > self.text.rect.size[0]:
                size = default_size
            else:
                size = self.text.rect.size

            # increasing size of element relative to text
            size = (
                int(size[0] * 1.2) + self.border_radius,
                int(size[1] * 1.6),
            )

        else:
            size = self.size

        self.rect = pygame.Rect(self.position, size)
        self.text.position = self.position

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
        super().draw(surface)
        self.text.draw(surface)
