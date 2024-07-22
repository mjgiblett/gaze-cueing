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
        border_width: int = 4,
        border_radius: int = 30,
        is_enabled: bool = True,
        is_active: bool = False,
    ) -> None:
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
        self.is_active = True
