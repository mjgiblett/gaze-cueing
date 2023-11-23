import pygame

from src.constants import BLACK
from src.gui.position import Position


class Text:
    def __init__(
        self,
        text: str,
        font: pygame.font.Font,
        pos: Position,
        colour: pygame.Color = BLACK,
        is_centred: bool = False,
        limit: int = 0,
        is_enabled: bool = True,
    ) -> None:
        self.text = text
        self.font = font
        self.pos = int(pos[0]), int(pos[1])
        self.colour = colour
        self.is_centred = is_centred
        self.limit = limit
        self.is_enabled = is_enabled

    def display(self, screen: pygame.Surface) -> None:
        if not self.is_enabled:
            return
        height = self.font.size(" ")[1]
        n = 0
        for line in self.text.split("\n"):
            if self.limit != 0 and self.font.size(line)[0] > self.limit:
                width = 0
                string = ""
                strings: dict[int, str] = {}
                for word in line.split(" "):
                    width += self.font.size(word)[0]
                    if width > self.limit:
                        strings[n] = string
                        n += 1
                        string = word + " "
                    else:
                        string += word + " "
                for sn, string in strings.items():
                    text = self.font.render(string, True, self.colour)
                    text_rect = text.get_rect()
                    if self.is_centred:
                        text_rect.center = self.pos[0], self.pos[1] + (height * sn)
                    else:
                        text_rect.topleft = self.pos[0], self.pos[1] + (height * sn)
                    screen.blit(text, text_rect)
            else:
                text = self.font.render(line, True, self.colour)
                text_rect = text.get_rect()
                if self.is_centred:
                    text_rect.center = self.pos[0], self.pos[1] + (height * n)
                else:
                    text_rect.topleft = self.pos[0], self.pos[1] + (height * n)
                screen.blit(text, text_rect)
            n += 1
