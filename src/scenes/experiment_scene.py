"""
Defines ExperimentScene class.
"""

import pygame

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
        self.fixation_cross = FixationCross(screen)

        self.is_resting = False
        self.rest_text = MultilineText(
            (
                "Take a break!"
                "\nWhen you are ready, press any key to continue with the experiment.\n"
                "\nRemember:"
                "\nIf the letter is an L, press the SPACE bar."
                "\nIf the letter is a T, press the H key."
            ),
            fonts["text"],
            (self.screen.get_width() // 2, 500),
        )

    def display(self, elements: list[Element]) -> None:
        if self.is_resting:
            self.rest_text.draw(self.screen)
            return
        self.fixation_cross.draw(self.screen)
        for image in elements:
            image.draw(self.screen)
