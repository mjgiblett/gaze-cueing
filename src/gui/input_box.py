"""
This module defines the InputBox class, an interactive element allowing
users to input text and numbers. 
"""
import pygame

from src.constants import BLACK, WHITE
from src.gui.interactive_text import InteractiveText
from src.visuals import Text


class InputBox(InteractiveText):
    """
    A class allowing users to input text and numbers.

    Attributes
    ----------
    text : Text
        The Text of the element.
    position : tuple[int, int]
        The x, y coordinates of the element.
    size : tuple[int, int]
        The width and height of the element.
    name : str
        The name of the element.
    background_colour : pygame.Color | None
        The colour of the element's border.
    border_colour : pygame.Color | None
        The colour of the element's background.
    border_width : int
        The width of the element's border.
    border_radius: int
        The radius of the border's rounded corners.
    is_enabled : bool
        A flag indicating whether the element is displayed.
    is_active : bool
        A flag indicating whether the element is active.
    is_numeric : bool
        A flag indicating whether the input is limited to numbers only.
    char_limit : int
        The maximum number of characters the input box can display.
    rect : pygame.Rect
        The rectangular area occupied by the element.

    Methods
    -------
    draw(surface: pygame.Surface) -> None
        Draws the element on the provided surface if enabled.
    set_rect() -> None
        Sets the rectangular area occupied by the element based on its
        position and size.
    is_clicked(mouse_pos: tuple[int, int]) -> bool
        Detects whether the mouse clicks the element.
    clicked() -> None
        Peform function after element is clicked.
    not_clicked() -> None
        Peform function after element is not clicked.
    key_down(key: int) -> None
        Handles key down events.
    """

    def __init__(
        self,
        text: Text,
        position: tuple[int, int] = (0, 0),
        size: tuple[int, int] = (60, 30),
        name: str = "",
        background_colour: pygame.Color | None = None,
        border_colour: pygame.Color | None = BLACK,
        border_width: int = 4,
        border_radius: int = 10,
        is_enabled: bool = True,
        is_active: bool = False,
        is_numeric: bool = False,
        char_limit: int = 20,
    ) -> None:
        """
        Initialises a new instance of the InputBox class.

        Parameters
        ----------
        text : Text
            The Text of the element.
        position : tuple[int, int], optional
            The x, y coordinates of the element. Defaults to (0, 0).
        size : tuple[int, int], optional
            The width and height of the element. Defaults to (60, 30).
        name : str, optional
            The name of the element. Defaults to an empty string.
        background_colour : pygame.Color | None, optional
            The colour of the element's border. Defaults to None.
        border_colour : pygame.Color | None, optional
            The colour of the element's background. Defaults to None.
        border_width : int, optional
            The width of the element's border. Defaults to 4.
        border_radius: int, optional
            The radius of the border's rounded corners. Defaults to 10.
        is_enabled : bool, optional
            A flag indicating whether the element is displayed. Defaults
            to True.
        is_active : bool
            A flag indicating whether the element is active. Defaults to
            False.
        is_numeric : bool
            A flag indicating whether the input is limited to numbers
            only. Defaults to False.
        char_limit : int
            The maximum number of characters the input box can display.
            Defaults to 20.
        """
        super().__init__(
            text,
            position,
            size,
            name,
            background_colour,
            border_colour,
            border_width,
            border_radius,
            is_enabled,
            is_active,
        )
        self.is_numeric = is_numeric
        self.char_limit = char_limit

    def clicked(self) -> None:
        """
        Peform function after element is clicked.

        Returns
        -------
        None
        """
        self.is_active = True
        self.background_colour = WHITE

    def not_clicked(self) -> None:
        """
        Peform function after element is not clicked.

        Returns
        -------
        None
        """
        self.is_active = False
        self.background_colour = None

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
        if not self.is_active:
            return
        if not key:
            return

        name: str = pygame.key.name(key)
        if name == "return":
            self.not_clicked()
            return
        if name == "backspace":
            self.text.string = self.text.string[:-1]
            self.set_rect()
            return
        if len(self.text.string) >= self.char_limit:
            return

        if self.is_numeric and name.isnumeric():
            self.text.string += name
        elif not self.is_numeric and len(name) == 1:
            self.text.string += name
        self.set_rect()
