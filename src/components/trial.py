from collections.abc import Iterable
from dataclasses import dataclass
from enum import IntEnum, auto
from random import shuffle
from typing import Any, Iterator

from src.components import Stimulus, StimulusSpecies, Target, stimuli, targets
from src.constants import (
    COUNTERBALANCING_ASCENDING,
    RANDOM_TRIAL_ORDER,
    SPECIES_COUNTERBALANCING,
    STIMULUS_ONSET_ASYNCS,
)


class GazeValidity(IntEnum):
    VALID = auto()
    INVALID = auto()


class Response(IntEnum):
    NONE = 0
    SPACE = auto()
    H = auto()


@dataclass
class Trial:
    stimulus: Stimulus
    target: Target
    stimulus_onset_async: int
    response: Response
    reaction_time: int | None = None

    @property
    def response_accuracy(self) -> bool:
        return self.response == self.target.letter

    @property
    def gaze_validity(self) -> bool:
        return self.stimulus.gaze_direction == self.target.location

    def __iter__(self) -> Iterator[tuple[str, Any]]:
        for key, value in self.__dict__.items():
            if isinstance(value, Iterable):
                for k, v in value:
                    yield k, v
            else:
                yield key, value

        yield "response_accuracy", int(self.response_accuracy)
        yield "gaze_validity", int(self.gaze_validity)


def generate_trials() -> list[Trial]:
    trials: list[Trial] = []
    for stimulus in stimuli:
        for target in targets:
            for soa in STIMULUS_ONSET_ASYNCS:
                trials.append(
                    Trial(
                        stimulus=stimulus,
                        target=target,
                        stimulus_onset_async=soa,
                        response=Response.NONE,
                    )
                )
    if RANDOM_TRIAL_ORDER:
        shuffle(trials)

    if SPECIES_COUNTERBALANCING:
        first_species = (
            StimulusSpecies.DOG if COUNTERBALANCING_ASCENDING else StimulusSpecies.HUMAN
        )
        trials.sort(key=lambda trial: trial.stimulus.species == first_species)

    return trials
