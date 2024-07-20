"""
This module defines an abstract base class for visual and GUI elements. 
The Element class includes essential attributes such as position, size, 
name, and enabled stutus. It also includes an abstract method for 
displaying the element on the screen, which must be implemented by 
any subclasses.
"""
from abc import ABC, abstractmethod

import pygame


class Element(ABC):
    """
    Abstract base class for all visual and GUI elements.

    Attributes
    ----------
    position : tuple[int, int]
        The x, y coordinates of the element on the screen.
    size : tuple[int, int]
        The width and height of the element.
    name : str
        The name of the element.
    is_enabled : bool
        A flag indicating whether the element is displayed.
    rect : pygame.Rect
        The rectangular area occupied by the element.

    Methods
    -------
    display(screen: pygame.Surface) -> None
        Renders the element on the provided screen if enabled.
    set_rect() -> None
        Sets the rectangular area occupied by the element based on its
        position and size.
    """

    def __init__(
        self,
        position: tuple[int, int] = (0, 0),
        size: tuple[int, int] = (0, 0),
        name: str = "",
        is_enabled: bool = True,
    ) -> None:
        """
        Initialises a new instance of the Element class.

        Parameters
        ----------
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
        self._position = position
        self._size = size
        self.name = name
        self.is_enabled = is_enabled
        self.set_rect()

    @property
    def position(self) -> tuple[int, int]:
        """
        Gets or sets the position of the element.

        Returns
        -------
        tuple[int, int]
            The x, y coordinates of the element on the screen.
        """
        return self._position

    @position.setter
    def position(self, position: tuple[int, int]) -> None:
        self._position = position
        self._rect.center = position

    @property
    def size(self) -> tuple[int, int]:
        """
        Gets or sets the size of the element.

        Returns
        -------
        tuple[int, int]
            The width and height of the element.
        """
        return self._size

    @size.setter
    def size(self, size: tuple[int, int]) -> None:
        self._size = size
        self._rect.size = size

    @property
    def rect(self) -> pygame.Rect:
        """
        Gets or sets the rectangular area occupied by the element
        without changing its position.

        Returns
        -------
        pygame.Rect
            The rectangular area occupied by the element.
        """
        return self._rect

    @rect.setter
    def rect(self, rect: pygame.Rect) -> None:
        self._rect = rect
        self._rect.center = self.position
        self._size = self.rect.size

    @abstractmethod
    def display(self, screen: pygame.Surface) -> None:
        """
        Renders the element on the provided screen if enabled.

        Parameters
        ----------
        screen: pygame.Surface
            The main window displaying the experiment.

        Returns
        -------
        None
        """
        pass

    def set_rect(self) -> None:
        """
        Sets the rectangular area occupied by the element based on its
        position and size.

        Returns
        -------
        None
        """
        self._rect = pygame.Rect(self.position, self.size)
