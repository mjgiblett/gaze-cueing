from dataclasses import dataclass

import pygame

from src.constants import BLACK, WHITE


@dataclass
class Checkbox:
    size: int
    pos: tuple[int, int]
    border_radius: int = 4
    is_active: bool = False

    def __post_init__(self) -> None:
        self.rect = pygame.Rect(self.pos, (self.size, self.size))

    def display(self, screen: pygame.Surface) -> None:
        if self.is_active:
            pygame.draw.rect(screen, WHITE, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, self.border_radius)

    def is_clicked(self, mouse_pos: tuple[int, int]) -> bool:
        is_clicked = self.rect.collidepoint(mouse_pos)
        if is_clicked:
            self.is_active = not self.is_active
        return is_clicked
