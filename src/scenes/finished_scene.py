"""
Defines FinishedScene class.
"""

import pygame

from src.constants import SCREEN_DIMENSIONS, TEXT_FINISHED
from src.scenes.scene import Scene
from src.visuals import MultilineText, fonts


class FinishedScene(Scene):
    """
    The final scene of the experiment. Saves results and forces participant to quit or restart.

    Attributes
    ----------
    screen: pygame.Surface
        The main window displaying the experiment.

    Methods
    -------
    display()
        Display the scene on the main window.
    save_output()
        Saves all trials to an Excel file once the experiment is finished.
    """

    def __init__(self, screen: pygame.Surface) -> None:
        super().__init__(screen)

        self.elements = [
            MultilineText(
                string=TEXT_FINISHED,
                font=fonts["text"],
                position=SCREEN_DIMENSIONS["centre"],
            )
        ]
