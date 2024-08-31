"""
This module defines a base class for interactive GUI elements.
The Interactive class includes essential attributes such as position, 
size, name, colour, border, enabled, and active stutus.
"""
from abc import abstractmethod

import pygame

from src.visuals import Element


class Interactive(Element):
    """
    Base class for all interactive GUI elements.

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
    not_clicked() -> None
        Peform function after element is not clicked.
    key_down(key: int) -> None
        Handles key down events.
    """

    def __init__(
        self,
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
        Initialises a new instance of the Interactive class.

        Parameters
        ----------
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
        super().__init__(
            position,
            size,
            name,
            background_colour,
            border_colour,
            border_width,
            border_radius,
            is_enabled,
        )
        self.is_active = is_active

    def is_clicked(self, mouse_pos: tuple[int, int]) -> bool:
        """
        Detects whether the mouse clicks the element.

        Parameters
        ----------
        mouse_pos: tuple[int, int]
            Position of the mouse.

        Returns
        -------
        None
        """
        is_clicked = self.rect.collidepoint(mouse_pos)
        if is_clicked:
            self.clicked()
        else:
            self.not_clicked()
        return is_clicked

    def clicked(self) -> None:
        """
        Peform function after element is clicked.

        Returns
        -------
        None
        """
        pass

    def not_clicked(self) -> None:
        """
        Peform function after element is not clicked.

        Returns
        -------
        None
        """
        pass

    @abstractmethod
    def key_down(self, key: int) -> None:
        """
        Handles key down events.

        Parameters
        ----------
        key: int
            pygame constant representing the pressed key.

        Returns
        -------
        None
        """
        pass
