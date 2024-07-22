import pygame

from src.gui.interactive import Interactive
from src.visuals.text import Text


class InteractiveText(Interactive):
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
        super().draw(surface)
        self.text.draw(surface)
