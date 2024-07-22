import pygame

from src.constants import BLACK
from src.visuals.element import Element
from src.visuals.text import Text


class MultilineText(Element):
    def __init__(
        self,
        string: str,
        font: pygame.font.Font,
        position: tuple[int, int] = (0, 0),
        colour: pygame.Color = BLACK,
        name: str = "",
        is_enabled: bool = True,
    ) -> None:
        self._lines = []
        self._font = font
        self._colour = colour
        super().__init__(
            position=position,
            name=name,
            is_enabled=is_enabled,
        )
        self.string = string

    @property
    def string(self) -> str:
        return self._string

    @string.setter
    def string(self, string: str) -> None:
        self._string = string
        self.lines = string

    @property
    def font(self) -> pygame.font.Font:
        return self._font

    @font.setter
    def font(self, font: pygame.font.Font) -> None:
        self._font = font
        for line in self.lines:
            line.font = font

    @property
    def colour(self) -> pygame.Color:
        return self._colour

    @colour.setter
    def colour(self, colour: pygame.Color) -> None:
        self._colour = colour
        for line in self.lines:
            line.colour = colour

    @property
    def position(self) -> tuple[int, int]:
        return self._position

    @position.setter
    def position(self, position: tuple[int, int]) -> None:
        self._position = position

    @property
    def lines(self) -> list[Text]:
        return self._lines

    @lines.setter
    def lines(self, string: str) -> None:
        line_height = self.font.size(" ")[1]
        self._lines = []
        for x, line in enumerate(string.split("\n")):
            pos = (self.position[0], self.position[1] + (x * line_height))
            self._lines.append(Text(line, self.font, pos, self.colour))

    def draw(self, screen: pygame.Surface) -> None:
        if not self.is_enabled:
            return
        for line in self.lines:
            line.draw(screen)
