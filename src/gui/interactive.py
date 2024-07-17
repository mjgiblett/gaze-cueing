from abc import abstractmethod

import pygame

from src.visuals.element import Element


class Interactive(Element):
    def __init__(
        self,
        position: tuple[int, int] = (0, 0),
        size: tuple[int, int] = (0, 0),
        name: str = "",
        background_colour: pygame.Color | None = None,
        border_colour: pygame.Color | None = None,
        is_enabled: bool = True,
        is_active: bool = False,
        border_width: int = 4,
        border_radius: int = 0,
    ) -> None:
        self.background_colour = background_colour
        self.border_colour = border_colour
        self.is_active = is_active
        self.border_width = border_width
        self.border_radius = border_radius
        super().__init__(
            position,
            size,
            name,
            is_enabled,
        )

    def display(self, screen: pygame.Surface) -> None:
        if not self.is_enabled:
            return
        if self.background_colour:
            pygame.draw.rect(
                screen,
                self.background_colour,
                self.rect,
                border_radius=self.border_radius,
            )
        if self.border_colour:
            pygame.draw.rect(
                screen,
                self.border_colour,
                self.rect,
                self.border_width,
                self.border_radius,
            )

    def is_clicked(self, mouse_pos: tuple[int, int]) -> bool:
        """
        Detects whether the mouse clicks the element.
        Parameters
        ----------
        mouse_pos: tuple[int, int]
            Position of the mouse.
        Returns
        -------
        None
        """
        is_clicked = self.rect.collidepoint(mouse_pos)
        if is_clicked:
            self.clicked()
        else:
            self.not_clicked()
        return is_clicked

    def clicked(self) -> None:
        """
        Peform function after element is clicked.
        Returns
        -------
        None
        """
        pass

    def not_clicked(self) -> None:
        """
        Peform function after element is not clicked.
        Returns
        -------
        None
        """
        pass

    def key_down(self, key: int) -> None:
        """
        Handles key down events.
        Parameters
        ----------
        key: int
            pygame constant representing the pressed key.
        Returns
        -------
        None
        """
        pass
