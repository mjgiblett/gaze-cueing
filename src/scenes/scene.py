from abc import abstractmethod
from enum import IntEnum, auto

import pygame

from src.gui.interactive import Interactive
from src.visuals import Element


class QuitActionType(IntEnum):
    """
    Defines scene game states.
    """

    CONTINUE = auto()
    QUIT = auto()
    RESTART = auto()


class Scene:
    """
    Abstract class for all scenes to inherit from.
    Attributes
    ----------
    screen: pygame.Surface
        The main window displaying the experiment.
    Methods
    -------
    display()
        Displays the scene on the main window.
    update_state()
        Communicates to the SceneManager when to trasition from this scene to the next.
    key_down()
        Handles key down events.
    button_down()
        Handles mouse button down events.
    mouse_motion()
        Handles mouse motion events.
    """

    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.progress = False
        self.elements: list[Element] = []
        self.interactables: list[Interactive] = []

    def update_state(self) -> bool:
        """
        Communicates to the SceneManager when to trasition from this scene to the next.
        Returns
        -------
        bool
        """
        return self.progress

    def display(self) -> None:
        """
        Displays the scene on the main window.
        Returns
        -------
        None
        """
        for element in self.elements:
            element.draw(self.screen)
        for interactable in self.interactables:
            interactable.draw(self.screen)

    @abstractmethod
    def button_down(self, button: int, mouse_pos: tuple[int, int]) -> None:
        """
        Handles mouse button down events.
        Parameters
        ----------
        button: int
            pygame constant representing the pressed mouse button.
        mouse_pos: tuple[int, int]
            Position of the cursor when button clicked.
        Returns
        -------
        None
        """
        pass

    @abstractmethod
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

    @abstractmethod
    def mouse_motion(self, mouse_pos: tuple[int, int]) -> None:
        """
        Handles mouse motion events.
        Parameters
        ----------
        mouse_pos: tuple[int, int]
            Position of the cursor after motion.
        Returns
        -------
        None
        """
        pass
