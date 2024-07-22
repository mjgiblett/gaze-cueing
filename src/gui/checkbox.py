import pygame

from src.constants import BLACK, WHITE
from src.gui.interactive import Interactive


class Checkbox(Interactive):
    def __init__(
        self,
        position: tuple[int, int] = (0, 0),
        size: tuple[int, int] = (25, 25),
        name: str = "",
        background_colour: pygame.Color = WHITE,
        border_colour: pygame.Color = BLACK,
        border_width: int = 4,
        border_radius: int = 0,
        is_enabled: bool = True,
        is_active: bool = False,
    ) -> None:
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

    def draw(self, surface: pygame.Surface) -> None:
        if self.is_active:
            pygame.draw.rect(surface, WHITE, self.rect)
        pygame.draw.rect(
            surface, BLACK, self.rect, self.border_width, self.border_radius
        )

    def clicked(self) -> None:
        self.is_active = not self.is_active
