import pygame

from src.visuals import Element


class Interactive(Element):
    def __init__(
        self,
        position: tuple[int, int] = (0, 0),
        size: tuple[int, int] = (0, 0),
        name: str = "",
        background_colour: pygame.Color | None = None,
        border_colour: pygame.Color | None = None,
        border_width: int = 4,
        border_radius: int = 0,
        is_enabled: bool = True,
        is_active: bool = False,
    ) -> None:
        super().__init__(
            position,
            size,
            name,
            background_colour,
            border_colour,
            border_width,
            border_radius,
            is_enabled,
        )
        self.is_active = is_active

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
