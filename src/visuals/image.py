"""
This module defines the Image class, which can draw itself onto a surface
at a specific position when enabled. 
"""
import pygame

from src.visuals.element import Element


class Image(Element):
    """
    Represents an image surface and position.

    Attributes
    ----------
    surface: pygame.Surface
        The pygame object representing the image.
    position : tuple[int, int]
        The x, y coordinates of the image.
    size : tuple[int, int]
        The width and height of the image.
    name : str
        The name of the element.
    is_enabled : bool
        A flag indicating whether the element is displayed.
    rect : pygame.Rect
        The rectangular area occupied by the element.

    Methods
    -------
    display(screen: pygame.Surface) -> None
        Renders the image on the provided screen if enabled.
    set_rect() -> None
        Sets the rectangular area occupied by the image based on its
        position and size.
    """

    def __init__(
        self,
        surface: pygame.Surface,
        position: tuple[int, int] = (0, 0),
        size: tuple[int, int] = (0, 0),
        name: str = "",
        is_enabled: bool = True,
    ) -> None:
        """
        Initialises a new instance of the Image class.

        Parameters
        ----------
        surface: pygame.Surface
            The pygame object representing the image.
        position : tuple[int, int], optional
            The x, y coordinates of the element on the screen. Defaults
            to (0, 0).
        size : tuple[int, int], optional
            The width and height of the element. Defaults to (0, 0).
        name : str, optional
            The name of the element. Defaults to an empty string.
        is_enabled : bool, optional
            A flag indicating whether the element is displayed. Defaults
            to True.
        """
        self.original_surface = surface
        if size == (0, 0):
            size = surface.get_size()
        self.surface = pygame.transform.scale(surface, size)
        super().__init__(position, size, name, is_enabled=is_enabled)

    @property
    def size(self) -> tuple[int, int]:
        """
        Gets or sets the size of the image.

        Returns
        -------
        tuple[int, int]
            The width and height of the image.
        """
        return self._size

    @size.setter
    def size(self, size: tuple[int, int]) -> None:
        self._size = size
        self._rect.size = size
        self.surface = pygame.transform.scale(self.original_surface, size)

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draws the image on the provided surface if enabled.

        Parameters
        ----------
        screen: pygame.Surface
            The surface on which this image will be drawn on.

        Returns
        -------
        None
        """
        if not self.is_enabled:
            return
        screen.blit(self.surface, self.position)
