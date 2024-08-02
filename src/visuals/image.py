"""
This module defines the Image class, which can draw itself onto a surface
at a specific position when enabled. 
"""

import pygame

from .element import Element


def load_image(path: str) -> pygame.Surface:
    try:
        return pygame.image.load(path)
    except Exception as e:
        print(e)
        return pygame.Surface((0, 0))


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
    draw(screen: pygame.Surface) -> None
        Draws the image on the provided surface if enabled.
    set_rect() -> None
        Sets the rectangular area occupied by the image based on its
        position and size.
    """

    def __init__(
        self,
        surface: pygame.Surface | str,
        position: tuple[int, int] = (0, 0),
        size: tuple[int, int] = (0, 0),
        name: str = "",
        is_enabled: bool = True,
    ) -> None:
        """
        Initialises a new instance of the Image class.

        Parameters
        ----------
        surface: pygame.Surface | str
            The pygame object representing the image, or a path to an
            image file.
        position : tuple[int, int], optional
            The x, y coordinates of the element. Defaults to (0, 0).
        size : tuple[int, int], optional
            The width and height of the element. Defaults to (0, 0),
            which will set the size to the native resolution of the image.
        name : str, optional
            The name of the element. Defaults to an empty string.
        is_enabled : bool, optional
            A flag indicating whether the element is displayed. Defaults
            to True.
        """
        if isinstance(surface, str):
            surface = load_image(surface)

        self._original_surface = surface
        if size == (0, 0):
            size = surface.get_size()
        self._surface = pygame.transform.scale(surface, size)
        super().__init__(position, size, name, is_enabled=is_enabled)

    @property
    def surface(self) -> pygame.Surface:
        """
        Gets or sets the Surface object representing the image without
        changing the position or size. Accepts a string to an image file.

        Returns
        -------
        surface: pygame.Surface
            The pygame object representing the image.
        """
        return self._surface

    @surface.setter
    def surface(self, surface: pygame.Surface | str) -> None:
        if isinstance(surface, str):
            surface = load_image(surface)

        self._original_surface = surface
        self._surface = pygame.transform.scale(surface, self.size)

    @property
    def size(self) -> tuple[int, int]:
        """
        Gets or sets the size of the image. Setting the size to (0, 0)
        will restore the image to its native resolution.

        Returns
        -------
        tuple[int, int]
            The width and height of the image.
        """
        return self._size

    @size.setter
    def size(self, size: tuple[int, int]) -> None:
        if size == (0, 0):
            self._surface = self._original_surface
            size = self._surface.get_size()
        else:
            self._surface = pygame.transform.scale(self._original_surface, size)
        self._size = size
        self._rect.size = size

    @property
    def rect(self) -> pygame.Rect:
        """
        Gets the rectangular area occupied by the image.

        Returns
        -------
        pygame.Rect
            The rectangular area occupied by the image.
        """
        return self._rect

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
