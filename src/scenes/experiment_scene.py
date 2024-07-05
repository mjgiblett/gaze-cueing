"""
Defines ExperimentScene class.
"""
import pygame

from src.components.fixation_cross import FixationCross
from src.components.trials import Response, trials_init
from src.constants import INTER_TRIAL_INTERVAL, MAX_RESPONSE_TIME, TRIAL_DEBUGGING
from src.gui.fonts import fonts
from src.gui.text import Text
from src.gui.tools import show_trial
from src.scenes.scene import Scene


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

    def __init__(
        self, screen: pygame.Surface, participant_details: dict[str, int]
    ) -> None:
        super().__init__(screen)
        self.fixation_cross = FixationCross(screen)
        pygame.mouse.set_visible(False)

        self.trials = trials_init(participant_details)
        self.trials_count = len(self.trials.index)
        self.trial_number = -1

        self.rest = False
        self.rest_text = Text(
            (
                "Take a break!"
                "\nWhen you are ready, press any key to continue with the experiment.\n"
                "\nRemember:"
                "\nIf the letter is an L, press the SPACE bar."
                "\nIf the letter is a T, press the H key."
            ),
            fonts["text"],
            (self.screen.get_width() // 2, 500),
            is_centred=True,
        )

        self.next_trial()

    def display(self) -> None:
        if self.rest:
            self.rest_text.display(self.screen)
            return
        time = pygame.time.get_ticks()
        if TRIAL_DEBUGGING and self.trial_number > 0:
            show_trial(
                self.screen, self.trials.loc[self.trial_number - 1], fonts["small"]
            )

        self.fixation_cross.display(self.screen)

        if time >= self.display_stimulus_time:
            self.current_stimulus.display(self.screen)
        if time >= self.display_target_time:
            self.current_target.display(self.screen)
        if time - self.display_target_time >= MAX_RESPONSE_TIME:
            self.next_trial()

    def key_down(self, key: int) -> None:
        time = pygame.time.get_ticks()
        if self.rest:
            if time > self.trial_start_time + 2000:
                self.next_trial()
            return
        if time < self.display_target_time:
            return
        name = pygame.key.name(key)
        if name not in ["space", "h"]:
            return
        response = Response.SPACE if name == "space" else Response.H
        self.trials.at[self.trial_number, "response"] = response.value

        accuracy = response.value == self.trials.at[self.trial_number, "target_letter"]
        self.trials.at[self.trial_number, "response_accuracy"] = int(accuracy)

        self.next_trial()

    def next_trial(self) -> None:
        """
        Begins the next trial of the experiment once the active trial is complete.
        Returns
        -------
        None
        """
        time = pygame.time.get_ticks()
        if self.trial_number == -1:
            self.trial_start_time = time + 1000
        else:
            self.trials.at[self.trial_number, "reaction_time"] = (
                time - self.display_target_time
            )
            self.trial_start_time = time

        if self.rest:
            self.rest = False
        else:
            if self.trial_number == (self.trials_count // 2):
                self.rest = True
                return

        self.trial_number += 1
        if self.trial_number >= self.trials_count:
            self.progress = True
            return

        self.display_stimulus_time = self.trial_start_time + INTER_TRIAL_INTERVAL
        self.display_target_time = (
            self.display_stimulus_time + self.trials.at[self.trial_number, "soa"]
        )
        self.current_stimulus = self.trials.at[self.trial_number, "stimulus_image"]
        self.current_target = self.trials.at[self.trial_number, "target_image"]
