import pygame

from src.visuals.element import Element


class Image(Element):
    """
    Represents an image surface and position.
    Attributes
    ----------
    surface: pygame.Surface
        The pygame surface of the image.
    pos: tuple[int, int]
        Position of the surface on the screen.
    Methods
    -------
    display()
        Displays the image.
    """

    def __init__(
        self,
        surface: pygame.Surface,
        position: tuple[int, int] = (0, 0),
        size: tuple[int, int] = (0, 0),
        name: str = "",
        is_enabled: bool = True,
    ) -> None:
        self.surface = surface
        super().__init__(position, size, name, is_enabled)

    def display(self, screen: pygame.Surface) -> None:
        screen.blit(self.surface, self.position)
