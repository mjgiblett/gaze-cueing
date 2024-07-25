"""
This module defines the MultilineText class, used to represent multiple
lines of text. 
"""
import pygame

from src.constants import BLACK

from .element import Element
from .text import Text


class MultilineText(Element):
    """
    A class representing multiple lines of text.

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
        Initialises a new instance of the MultilineText class.

        Parameters
        ----------
        string : str
            The string value of the text element. Uses newlines
            '\n' to split the string into seperate lines.
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
        self._lines = []
        self._font = font
        self._text_colour = text_colour
        super().__init__(
            position=position,
            name=name,
            is_enabled=is_enabled,
        )

    @property
    def string(self) -> str:
        """
        Gets or sets the string value of the text element. Uses newlines
        '\n' to split the string into seperate lines.

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
        for line in self._lines:
            line.font = font
        self.set_rect()

    @property
    def text_colour(self) -> pygame.Color:
        """
        Gets or sets the text colour of the text element.

        Returns
        -------
        pygame.Color
            The text colour of the text element.
        """
        return self._text_colour

    @text_colour.setter
    def text_colour(self, colour: pygame.Color) -> None:
        self._text_colour = colour
        for line in self._lines:
            line.text_colour = colour

    @property
    def position(self) -> tuple[int, int]:
        """
        Gets or sets the position of the text element.

        Returns
        -------
        tuple[int, int]
            The x, y coordinates of the text element on the screen.
        """
        return self._position

    @position.setter
    def position(self, position: tuple[int, int]) -> None:
        self._position = position
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
        line_height = self.font.size(" ")[1]
        self._lines = []
        x = 0
        for x, line in enumerate(self._string.split("\n")):
            pos = (self.position[0], self.position[1] + (x * line_height))
            self._lines.append(Text(line, self.font, pos, self.text_colour))

        width = max([line.size[0] for line in self._lines])

        rect = pygame.Rect(self.position, (width, (x + 1) * line_height))
        rect.centerx = self.position[0]  # centres rect with text in the x-axis
        rect.y -= line_height // 2  # centres rect with text in the y-axis
        self._rect = rect
        self._size = rect.size

    def draw(self, surface: pygame.Surface) -> None:
        """
        Draws each line of text on the provided surface if enabled.

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
        super().draw(surface)
        for line in self._lines:
            line.draw(surface)
