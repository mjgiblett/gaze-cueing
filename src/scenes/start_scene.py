"""
Defines StartScene class.
"""

import pygame

from src.constants import (
    BG_GREY,
    SCREEN_DIMENSIONS,
    TEXT_CONTINUE,
    TEXT_INSTRUCTIONS,
    TEXT_TITLE,
)
from src.gui import Button
from src.scenes.scene import Scene
from src.visuals import MultilineText, Text, fonts


class StartScene(Scene):
    """
    The initial scene of the experiment. Displays instructions and begins experiment.
    Attributes
    ----------
    screen: pygame.Surface
        The main window displaying the experiment.
    Methods
    -------
    display()
        Display the scene on the main window.
    update_state()
        Communicates to the SceneManager when to trasition from this scene to the next.
    key_down()
        Handles key down events.
    """

    def __init__(self, screen: pygame.Surface) -> None:
        super().__init__(screen)
        centre_x = SCREEN_DIMENSIONS["centre"][0]
        self.elements = [
            Text(
                string=TEXT_TITLE,
                font=fonts["title"],
                position=(centre_x, 150),
            ),
            MultilineText(
                string=TEXT_INSTRUCTIONS,
                font=fonts["text"],
                position=(centre_x, 300),
            ),
        ]
        self.interactables = [
            Button(
                text=Text(
                    string=TEXT_CONTINUE,
                    font=fonts["button"],
                    text_colour=BG_GREY,
                ),
                position=(centre_x, 900),
                name=TEXT_CONTINUE,
            ),
        ]

    def button_down(self, _: int, pos: tuple[int, int]) -> None:
        for interactable in self.interactables:
            if not interactable.is_clicked(pos):
                continue
            if interactable.name == TEXT_CONTINUE:
                self.progress = True
