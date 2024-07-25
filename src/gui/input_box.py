import pygame

from src.constants import BLACK, WHITE
from src.gui.interactive_text import InteractiveText
from src.visuals import Text


class InputBox(InteractiveText):
    def __init__(
        self,
        text: Text,
        position: tuple[int, int] = (0, 0),
        size: tuple[int, int] = (60, 30),
        name: str = "",
        background_colour: pygame.Color | None = None,
        border_colour: pygame.Color | None = BLACK,
        border_width: int = 4,
        border_radius: int = 10,
        is_enabled: bool = True,
        is_active: bool = False,
        is_numeric: bool = False,
        char_limit: int = 0,
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
        self.is_numeric = is_numeric
        self.char_limit = char_limit

    def clicked(self) -> None:
        self.is_active = True
        self.background_colour = WHITE

    def not_clicked(self) -> None:
        self.is_active = False
        self.background_colour = None

    def key_down(self, key: int) -> None:
        if not self.is_active:
            return
        if not key:
            return

        name: str = pygame.key.name(key)
        if name == "return":
            self.not_clicked()
            return
        if name == "backspace":
            self.text.string = self.text.string[:-1]
            self.set_rect()
            return
        if len(self.text.string) >= self.char_limit:
            return

        if self.is_numeric and name.isnumeric():
            self.text.string += name
        elif not self.is_numeric and (name.isalpha() or name.isnumeric()):
            self.text.string += name
        self.set_rect()
