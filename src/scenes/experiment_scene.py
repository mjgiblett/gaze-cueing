"""
Defines ExperimentScene class.
"""

import pygame

from src.constants import SCREEN_DIMENSIONS, TEXT_REST
from src.scenes.scene import Scene
from src.visuals import Element, FixationCross, MultilineText, fonts


class ExperimentScene(Scene):
    """
    The scene in which the gaze-cueing experiment begins.
    Attributes
    ----------
    screen: pygame.Surface
        The main window displaying the experiment.
    participant_details: dict[str, int]
        Detials of the participant.
    Methods
    -------
    display()
        Displays the scene on the main window.
    update_state()
        Communicates to the SceneManager when to trasition from this scene to the next.
    key_down()
        Handles key down events.
    next_trial()
        Begins the next trial of the experiment once the active trial is complete.
    """

    def __init__(self, screen: pygame.Surface) -> None:
        super().__init__(screen)

        centre_x = SCREEN_DIMENSIONS["centre"][0]
        self.is_resting = False
        self.fixation_cross = FixationCross(screen)
        self.rest_text = MultilineText(
            string=TEXT_REST,
            font=fonts["text"],
            position=(centre_x, 500),
        )

    def display(self, elements: list[Element]) -> None:
        if self.is_resting:
            self.rest_text.draw(self.screen)
            return
        self.fixation_cross.draw(self.screen)
        for image in elements:
            image.draw(self.screen)
