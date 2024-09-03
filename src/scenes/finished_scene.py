"""
Defines FinishedScene class.
"""

import pygame

from src.scenes.scene import Scene
from src.visuals import MultilineText, fonts


class FinishedScene(Scene):
    """
    The final scene of the experiment. Saves results and forces participant to quit or restart.
    Attributes
    ----------
    screen: pygame.Surface
        The main window displaying the experiment.
    trials: pandas.DataFrame
        Contains participant details as well as data from all trials in the experiment.
        The
    Methods
    -------
    display()
        Display the scene on the main window.
    save_output()
        Saves all trials to an Excel file once the experiment is finished.
    """

    def __init__(self, screen: pygame.Surface) -> None:
        super().__init__(screen)

        finished_text = MultilineText(
            (
                "Experiment completed!\nThank you for participating!\n\nPress ESCAPE to quit or R to restart."
            ),
            fonts["text"],
            (self.screen.get_width() // 2, self.screen.get_height() // 2),
        )

        self.elements.append(finished_text)
