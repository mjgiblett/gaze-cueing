import pygame

from src.constants import BLACK, WHITE


class InputBox:
    def __init__(
        self,
        title: str,
        font: pygame.font.Font,
        pos: tuple[int, int],
        colour: pygame.Color = BLACK,
        is_numeric: bool = False,
        is_centred: bool = False,
        char_limit: int = 10,
    ) -> None:
        self.text: str = ""
        self.is_active: bool = False
        self.title = title
        self.font = font
        self.pos = pos
        self.colour = colour
        self.bg_colour: pygame.Color | None = None
        self.is_numeric = is_numeric
        self.is_centred = is_centred
        self.char_limit = char_limit

        self.border = self.create_border()

    def display(self, screen: pygame.Surface) -> None:
        if self.bg_colour:
            pygame.draw.rect(screen, self.bg_colour, self.border, border_radius=10)
        pygame.draw.rect(screen, BLACK, self.border, 2, border_radius=10)
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
        if self.border.collidepoint(mouse_pos):
            self.is_active = True
            self.bg_colour = WHITE
            return True
        self.is_active = False
        self.bg_colour = None
        return False

    def edit_text(self, key: int) -> None:
        if not self.is_active:
            return
        if not key:
            return

        name: str = pygame.key.name(key)
        if name == "return":
            self.is_active = False
            return
        if name == "backspace":
            self.text = self.text[:-1]
            self.border = self.create_border()
            return
        if len(self.text) >= self.char_limit:
            return

        if self.is_numeric and name.isnumeric():
            self.text += name
        elif not self.is_numeric and (name.isalpha() or name.isnumeric()):
            self.text += name
        self.border = self.create_border()
