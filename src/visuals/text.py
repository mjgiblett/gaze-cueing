"""
This module defines the Text class, used to representing a single line
of text. 
"""
import pygame

from src.constants import BLACK
from src.visuals.element import Element


class Text(Element):
    """
    A class representing a text element.

    Attributes
    ----------
    string : str
        The string value of the text element.
    font : pygame.font.Font
        The font of the text element.
    position : tuple[int, int]
        The x, y coordinates of the text element.
    size : tuple[int, int]
        The width and height of the text element's rectangle.
    text_colour : pygame.Color
        The text colour of the text element.
    name : str
        The name of the text element.
    is_enabled : bool
        A flag indicating whether the text element is displayed.
    rect : pygame.Rect
        The rectangular area occupied by the text element.

    Methods
    -------
    draw(surface: pygame.Surface) -> None
        Draws the text element on the provided surface if enabled.
    set_rect() -> None
        Renders the text and sets the rectangular area occupied by the
        text element based on its position and size.
    """

    def __init__(
        self,
        string: str,
        font: pygame.font.Font,
        position: tuple[int, int] = (0, 0),
        text_colour: pygame.Color = BLACK,
        name: str = "",
        is_enabled: bool = True,
    ) -> None:
        """
        Initialises a new instance of the Text class.

        Parameters
        ----------
        string : str
            The string value of the text element.
        font : pygame.font.Font,
            The font of the text element.
        position : tuple[int, int], optional
            The x, y coordinates of the text element. Defaults to (0, 0).
        text_colour : pygame.Color, optional
            The text colour of the text element. Defaults to black.
        name : str, optional
            The name of the text element. Defaults to an empty string.
        is_enabled : bool, optional
            A flag indicating whether the text element is displayed.
            Defaults to True.
        """
        self._string = string
        self._font = font
        self._text_colour = text_colour
        super().__init__(
            position,
            name=name,
            is_enabled=is_enabled,
        )

    @property
    def string(self) -> str:
        """
        Gets or sets the string value of the text element.

        Returns
        -------
        str
            The string value of the text element.
        """
        return self._string

    @string.setter
    def string(self, string: str) -> None:
        self._string = string
        self.set_rect()

    @property
    def font(self) -> pygame.font.Font:
        """
        Gets or sets the font of the text element.

        Returns
        -------
        pygame.font.Font
            The font of the text element.
        """
        return self._font

    @font.setter
    def font(self, font: pygame.font.Font) -> None:
        self._font = font
        self.set_rect()

    @property
    def text_colour(self) -> pygame.Color:
        """
        Gets or sets the text_colour of the text element.

        Returns
        -------
        pygame.font.Font
            The font of the text element.
        """
        return self._text_colour

    @text_colour.setter
    def text_colour(self, colour: pygame.Color) -> None:
        self._text_colour = colour
        self.set_rect()

    @property
    def size(self) -> tuple[int, int]:
        """
        Gets the size of the text element.

        Returns
        -------
        tuple[int, int]
            The width and height of the text element.
        """
        return self._size

    @property
    def rect(self) -> pygame.Rect:
        """
        Gets the rectangular area occupied by the text element without
        changing its position.

        Returns
        -------
        pygame.Rect
            The rectangular area occupied by the text element.
        """
        return self._rect

    def set_rect(self) -> None:
        """
        Renders the text and sets the rectangular area occupied by the
        text element based on its position and size.

        Returns
        -------
        None
        """
        self.render = self.font.render(self.string, True, self.text_colour)
        rect = self.render.get_rect()
        rect.center = self.position
        self._rect = rect
        self._size = rect.size

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draws the text element on the provided surface if enabled.

        Parameters
        ----------
        surface: pygame.Surface
            The surface on which the text element will be drawn on.

        Returns
        -------
        None
        """
        if not self.is_enabled:
            return
        screen.blit(self.render, self.rect)
