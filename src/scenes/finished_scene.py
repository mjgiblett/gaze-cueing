"""
Defines FinishedScene class.
"""
import pandas
import pygame

from src.components.stimuli import StimulusGazeDirection, StimulusSpecies
from src.components.targets import TargetLetter, TargetLocation
from src.components.trials import Response, Validity
from src.scenes.scene import Scene
from src.visuals.fonts import fonts
from src.visuals.multiline_text import MultilineText


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

        finished_text = MultilineText(
            (
                "Experiment completed!\nThank you for participating!\n\nPress ESCAPE to quit or R to restart."
            ),
            fonts["text"],
            (self.screen.get_width() // 2, self.screen.get_height() // 2),
        )

        self.elements.append(finished_text)

    def save_output(self) -> None:
        """
        Saves all trials to excel file once experiment is finished.
        Returns
        -------
        None
        """

        if self.output.empty:
            return

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
