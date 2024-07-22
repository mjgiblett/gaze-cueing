"""
This module defines a base class for visual and GUI elements. 
The Element class includes essential attributes such as position, size,
name, colour, border, and enabled stutus.
"""

import pygame


class Element:
    """
    Base class for all visual and GUI elements.

    Attributes
    ----------
    position : tuple[int, int]
        The x, y coordinates of the element on the screen.
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
    rect : pygame.Rect
        The rectangular area occupied by the element.

    Methods
    -------
    draw(surface: pygame.Surface) -> None
        Draws the element on the provided surface if enabled.
    set_rect() -> None
        Sets the rectangular area occupied by the element based on its
        position and size.
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
    ) -> None:
        """
        Initialises a new instance of the Element class.

        Parameters
        ----------
        position : tuple[int, int], optional
            The x, y coordinates of the element on the screen. Defaults
            to (0, 0).
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
        """
        self._position = position
        self._size = size
        self.name = name
        self.background_colour = background_colour
        self.border_colour = border_colour
        self.border_width = border_width
        self.border_radius = border_radius
        self.is_enabled = is_enabled
        self.set_rect()

    @property
    def position(self) -> tuple[int, int]:
        """
        Gets or sets the position of the element.

        Returns
        -------
        tuple[int, int]
            The x, y coordinates of the element on the screen.
        """
        return self._position

    @position.setter
    def position(self, position: tuple[int, int]) -> None:
        self._position = position
        self._rect.center = position

    @property
    def size(self) -> tuple[int, int]:
        """
        Gets or sets the size of the element.

        Returns
        -------
        tuple[int, int]
            The width and height of the element.
        """
        return self._size

    @size.setter
    def size(self, size: tuple[int, int]) -> None:
        self._size = size
        self._rect.size = size

    @property
    def rect(self) -> pygame.Rect:
        """
        Gets or sets the rectangular area occupied by the element
        without changing its position.

        Returns
        -------
        pygame.Rect
            The rectangular area occupied by the element.
        """
        return self._rect

    @rect.setter
    def rect(self, rect: pygame.Rect) -> None:
        self._rect = rect
        self._rect.center = self.position
        self._size = self.rect.size

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
        if not self.is_enabled:
            return
        if self.background_colour:
            pygame.draw.rect(
                surface,
                self.background_colour,
                self.rect,
                border_radius=self.border_radius,
            )
        if self.border_colour:
            pygame.draw.rect(
                surface,
                self.border_colour,
                self.rect,
                self.border_width,
                self.border_radius,
            )

    def set_rect(self) -> None:
        """
        Sets the rectangular area occupied by the element based on its
        position and size.

        Returns
        -------
        None
        """
        self._rect = pygame.Rect(self.position, self.size)
