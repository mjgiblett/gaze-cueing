import pygame

from src.constants import BLACK
from src.visuals.element import Element


class Text(Element):
    def __init__(
        self,
        string: str,
        font: pygame.font.Font,
        position: tuple[int, int] = (0, 0),
        colour: pygame.Color = BLACK,
        name: str = "",
        is_enabled: bool = True,
    ) -> None:
        self._string = string
        self._font = font
        self._colour = colour
        super().__init__(
            position=position,
            name=name,
            is_enabled=is_enabled,
        )

    @property
    def string(self) -> str:
        return self._string

    @string.setter
    def string(self, string: str) -> None:
        self._string = string
        self.set_rect()

    @property
    def font(self) -> pygame.font.Font:
        return self._font

    @font.setter
    def font(self, font: pygame.font.Font) -> None:
        self._font = font
        self.set_rect()

    @property
    def colour(self) -> pygame.Color:
        return self._colour

    @colour.setter
    def colour(self, colour: pygame.Color) -> None:
        self._colour = colour
        self.set_rect()

    def set_rect(self) -> None:
        self.render = self.font.render(self.string, True, self.colour)
        rect = self.render.get_rect()
        rect.center = self.position
        self.rect = rect

    def display(self, screen: pygame.Surface) -> None:
        if not self.is_enabled:
            return
        screen.blit(self.render, self.rect)
