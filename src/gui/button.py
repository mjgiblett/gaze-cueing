import pygame

from src.constants import BLACK
from src.gui.interactive_text import InteractiveText
from src.visuals.text import Text


class Button(InteractiveText):
    def __init__(
        self,
        text: Text,
        position: tuple[int, int] = (0, 0),
        size: tuple[int, int] = (60, 30),
        name: str = "",
        background_colour: pygame.Color | None = BLACK,
        border_colour: pygame.Color | None = None,
        is_enabled: bool = True,
        is_active: bool = False,
        border_width: int = 4,
        border_radius: int = 30,
    ) -> None:
        super().__init__(
            text,
            position,
            size,
            name,
            background_colour,
            border_colour,
            is_enabled,
            is_active,
            border_width,
            border_radius,
        )

    def clicked(self) -> None:
        self.is_active = True
