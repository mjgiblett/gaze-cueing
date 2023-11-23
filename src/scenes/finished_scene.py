"""
Defines FinishedScene class.
"""
import pandas
import pygame

from src.components.stimuli import StimulusGazeDirection, StimulusSpecies
from src.components.targets import TargetLetter, TargetLocation
from src.components.trials import Response, Validity
from src.gui.fonts import fonts
from src.gui.text import Text
from src.scenes.scene import Scene


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
        Saves all trials to excel file once experiment is finished.
    """

    def __init__(self, screen: pygame.Surface, trials: pandas.DataFrame) -> None:
        super().__init__(screen)

        self.output = trials[
            [
                "participant_number",
                "age",
                "gender",
                "culture",
                "stimulus_species",
                "stimulus_gaze_direction",
                "stimulus_number",
                "target_letter",
                "target_location",
                "gaze_validity",
                "soa",
                "response",
                "response_accuracy",
                "reaction_time",
            ]
        ]
        self.save_output()

        self.finished_text = Text(
            (
                "Experiment completed!\nThank you for participating!\n\nPress ESCAPE to quit or R to restart."
            ),
            fonts["text"],
            (self.screen.get_width() // 2, self.screen.get_height() // 2),
            is_centred=True,
        )

    def display(self) -> None:
        self.finished_text.display(self.screen)

    def save_output(self) -> None:
        """
        Saves all trials to excel file once experiment is finished.
        Returns
        -------
        None
        """
        number = self.output["participant_number"].min()

        data_labels = pandas.DataFrame(columns=["value"])
        data_labels.index.name = "variable"

        labels = [
            StimulusGazeDirection,
            StimulusSpecies,
            TargetLetter,
            TargetLocation,
            Response,
            Validity,
        ]

        for label in labels:
            for direction in label:
                data_labels.loc[direction.name] = direction.value

        with pandas.ExcelWriter(f"data/{number}.xlsx") as writer:
            self.output.to_excel(writer, sheet_name="output")
            data_labels.to_excel(writer, sheet_name="labels")
