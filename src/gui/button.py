import pygame

from src.constants import BLACK, DARK_GREY, LIGHT, SUBTLE


class Button:
    def __init__(
        self,
        text: str,
        font: pygame.font.Font,
        pos: tuple[int, int],
        colour: pygame.Color = BLACK,
        is_centred: bool = False,
    ) -> None:
        self.text = text
        self.font = font
        self.pos = pos
        self.colour = colour
        self.is_centred = is_centred
        self.bg_colour = SUBTLE
        self.border_colour = DARK_GREY
        self.is_active: bool = False

        self.border = self.create_border()

    def display(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, self.bg_colour, self.border, border_radius=10)
        pygame.draw.rect(screen, self.border_colour, self.border, 2, border_radius=10)
        text = self.font.render(self.text, True, self.colour)
        text_rect = text.get_rect()
        if self.is_centred:
            text_rect.center = self.pos
        else:
            text_rect.topleft = self.pos

        screen.blit(text, text_rect)

    def create_border(self) -> pygame.Rect:
        default_size = self.font.size("------------")
        text_size = self.font.size(self.text)
        size = default_size if default_size[0] > text_size[0] else text_size

        rect = pygame.Rect(self.pos, size)
        if self.is_centred:
            rect.center = self.pos
        rect = rect.inflate(int(size[0] * 0.1), int(size[1] * 0.1))

        return rect

    def is_clicked(self, mouse_pos: tuple[int, int]) -> bool:
        self.is_active = self.border.collidepoint(mouse_pos)
        return self.is_active

    def on_hover(self, mouse_pos: tuple[int, int]) -> bool:
        collision = self.border.collidepoint(mouse_pos)
        if collision:
            self.bg_colour = LIGHT
            self.border_colour = BLACK
            return collision
        self.bg_colour = SUBTLE
        self.border_colour = DARK_GREY
        return collision
