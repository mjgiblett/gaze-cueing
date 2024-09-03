import pygame
from pandas import DataFrame, ExcelWriter

from src.components import (
    GazeValidity,
    Participant,
    Response,
    StimulusGazeDirection,
    StimulusSpecies,
    TargetLetter,
    TargetLocation,
    Trial,
    generate_trials,
    init_stimuli,
    init_targets,
)
from src.constants import (
    COUNTERBALANCING_ASCENDING,
    FIRST_TRIAL_DELAY,
    INTER_TRIAL_INTERVAL,
    MAX_RESPONSE_TIME,
    MINIMUM_REST_TIME,
    TRIAL_DEBUGGING,
)
from src.visuals import MultilineText, fonts
from src.visuals.element import Element


class TrialManager:
    participant: Participant
    trials: list[Trial]
    trials_length: int
    trial_number: int
    current_trial: Trial | None = None
    time_trial_start: int = 0
    time_draw_stimulus: int = 0
    time_draw_target: int = 0
    experiment_start_time: int = 0
    experiment_end_time: int = 0
    has_experiment_started: bool = False
    has_experiment_finished: bool = False
    is_resting: bool = False
    time_rest_start: int = 0

    def __init__(self) -> None:
        init_stimuli()
        init_targets()
        self.trials = generate_trials()
        self.trials_length = len(self.trials)
        self.trial_number = -1

    def start_experiment(self, time: int) -> None:
        pygame.mouse.set_visible(False)
        self.has_experiment_started = True
        self.experiment_start_time = time
        self.start_trial(time + FIRST_TRIAL_DELAY)

    def end_experiment(self, time: int) -> None:
        if not self.has_experiment_started:
            return
        pygame.mouse.set_visible(True)
        self.has_experiment_finished = True
        self.experiment_end_time = time
        self.save_data()

    def start_trial(self, time: int) -> None:
        if self.is_resting and time < self.time_rest_start + MINIMUM_REST_TIME:
            return
        # if next trial is the middle trial, begin rest if not already resting.
        if self.trial_number + 1 == self.trials_length // 2:
            if self.is_resting:
                self.is_resting = False
            else:
                self.is_resting = True
                self.time_rest_start = time
                return

        self.trial_number += 1
        if self.trial_number >= self.trials_length:
            self.end_experiment(time)
            return
        self.current_trial = self.trials[self.trial_number]
        soa = self.current_trial.stimulus_onset_async
        self.time_trial_start = time
        self.time_draw_stimulus = time + INTER_TRIAL_INTERVAL
        self.time_draw_target = time + INTER_TRIAL_INTERVAL + soa

    def during_trial(self, time: int) -> list[Element]:
        elements: list[Element] = []
        if self.is_resting:
            return elements
        if time - self.time_draw_target >= MAX_RESPONSE_TIME:
            self.end_trial(time, Response.NONE)
            return elements
        trial = self.trials[self.trial_number]
        if TRIAL_DEBUGGING:
            elements.append(self.trial_debugging())
        if time >= self.time_draw_stimulus:
            elements.append(trial.stimulus.image)
        if time >= self.time_draw_target:
            elements.append(trial.target.image)
        return elements

    def end_trial(self, time: int, response: Response) -> None:
        if not self.current_trial:
            return
        self.current_trial.response = response
        self.current_trial.reaction_time = time - self.time_draw_target
        self.start_trial(time)

    def key_down(self, time: int, key: int) -> None:
        if self.is_resting:
            if time < self.time_rest_start + MINIMUM_REST_TIME:
                return
            else:
                self.start_trial(time)
                return
        if time < self.time_draw_target:
            return
        name = pygame.key.name(key)
        if name not in ["space", "h"]:
            return
        response = Response.SPACE if name == "space" else Response.H
        self.end_trial(time, response)

    def save_data(self) -> None:
        if not self.has_experiment_finished:
            return

        df_trial_data = DataFrame(
            [{k: v for k, v in trial if "image" not in k} for trial in self.trials]
        )
        for k, v in self.participant:
            df_trial_data[k] = v
        df_trial_data["counterbalancing"] = int(COUNTERBALANCING_ASCENDING)
        df_trial_data.index.name = "trial_number"
        df_trial_data.index += 1

        variables = [
            StimulusSpecies,
            StimulusGazeDirection,
            TargetLetter,
            TargetLocation,
            Response,
            GazeValidity,
        ]

        df_variable_levels = DataFrame(
            {
                variable.__name__: {level.name: level.value for level in variable}
                for variable in variables
            }
        )

        with ExcelWriter(f"data/{self.participant.id}.xlsx") as writer:
            df_trial_data.to_excel(writer, sheet_name="trial_data")
            df_variable_levels.to_excel(writer, sheet_name="variable_levels")

        # print(df.index)

    def trial_debugging(self) -> MultilineText:
        string = ""
        text = MultilineText(string=string, font=fonts["small"])
        if not self.current_trial:
            return text
        string += "--- Participant ---"
        for k, v in self.participant:
            string += f"\n{k}: {v}"
        string += "\n\n--- Current Trial ---"
        string += f"\nTrial Number: {self.trial_number + 1} / {self.trials_length}"
        string += f"\nProgress: {round((self.trial_number + 1) / self.trials_length * 100, 3)}%"
        for k, v in self.current_trial:
            if "image" in k:
                continue
            string += f"\n{k}: {v}"
        if self.trial_number > 0:
            string += "\n\n--- Previous Trial ---"
            for k, v in self.trials[self.trial_number - 1]:
                if "image" in k:
                    continue
                string += f"\n{k}: {v}"
        text.string = string
        position = (5, 50)
        text.position = position
        for line in text._lines:
            line.rect.left = position[0]
        return text
