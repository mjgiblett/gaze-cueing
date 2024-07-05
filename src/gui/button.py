from dataclasses import dataclass

import pygame

from src.constants import BG_GREY, BLACK


@dataclass
class Button:
    text: str
    font: pygame.font.Font
    pos: tuple[int, int]
    is_centred: bool = False
    is_active: bool = False
    border_radius: int = 30

    def __post_init__(self) -> None:
        # render and get rectancle of button's text
        self.text_render = self.font.render(self.text, True, BG_GREY)
        self.text_rect = self.text_render.get_rect()

        default_size = self.font.size("-" * 10)  # default button size
        # if text is bigger than button, use text size
        if default_size[0] > self.text_rect.size[0]:
            rect_size = default_size
        else:
            rect_size = self.text_rect.size

        # increasing size of button relative to text
        rect_size = (rect_size[0] * 1.2 + self.border_radius, int(rect_size[1] * 1.6))

        # button rectangle
        self.rect = pygame.Rect(self.pos, rect_size)
        if self.is_centred:
            self.rect.center = self.pos
        self.text_rect.center = self.rect.center  # centre text to button

    def display(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, BLACK, self.rect, border_radius=self.border_radius)
        screen.blit(self.text_render, self.text_rect)

    def is_clicked(self, mouse_pos: tuple[int, int]) -> bool:
        self.is_active = self.rect.collidepoint(mouse_pos)
        return self.is_active
