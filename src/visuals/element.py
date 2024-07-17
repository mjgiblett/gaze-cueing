from abc import ABC, abstractmethod

import pygame


class Element(ABC):
    def __init__(
        self,
        position: tuple[int, int] = (0, 0),
        size: tuple[int, int] = (0, 0),
        name: str = "",
        is_enabled: bool = True,
    ) -> None:
        self._position = position
        self._size = size
        self.name = name
        self.is_enabled = is_enabled
        self.set_rect()

    @property
    def position(self) -> tuple[int, int]:
        return self._position

    @position.setter
    def position(self, position: tuple[int, int]) -> None:
        self._position = position
        self._rect.center = position

    @property
    def size(self) -> tuple[int, int]:
        return self._size

    @size.setter
    def size(self, size: tuple[int, int]) -> None:
        self._size = size
        self._rect.size = size

    @property
    def rect(self) -> pygame.Rect:
        return self._rect

    @rect.setter
    def rect(self, rect: pygame.Rect) -> None:
        self._rect = rect
        self._rect.center = self.position
        self._size = self.rect.size

    @abstractmethod
    def display(self, screen: pygame.Surface) -> None:
        """
        Displays the gui element on the main window if enabled.
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
        self.rect = pygame.Rect(self.position, self.size)
