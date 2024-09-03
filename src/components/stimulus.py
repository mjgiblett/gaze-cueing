"""
Defines experimental stimuli. 
"""

from dataclasses import dataclass
from enum import IntEnum, auto
from pathlib import Path
from typing import Any, Iterator

from pygame.image import load
from pygame.transform import scale

from src.constants import POSITIONS, STIMULI_PATH, STIMULUS_SCALE
from src.visuals import Image


class StimulusSpecies(IntEnum):
    """
    An int representing the species of a stimulus.
    """

    HUMAN = auto()
    DOG = auto()


class StimulusGazeDirection(IntEnum):
    """
    An int representing the gaze direction of a stimulus.
    """

    LEFT_GAZE = auto()
    RIGHT_GAZE = auto()


@dataclass
class Stimulus:
    image: Image
    number: int
    species: StimulusSpecies
    gaze_direction: StimulusGazeDirection

    def __iter__(self) -> Iterator[tuple[str, Any]]:
        for key, value in self.__dict__.items():
            yield f"stimulus_{key}", value


stimuli: list[Stimulus] = []


def init_stimuli() -> None:
    """
    Initialises the experimental stimuli.

    Returns
    -------
    None
    """
    for file in Path(STIMULI_PATH).rglob("*.tif"):
        path = str(file)
        surface = scale(load(path), STIMULUS_SCALE)
        stimulus = Stimulus(
            image=Image(surface, POSITIONS["stimuli"]),
            number=int("".join([i for i in path if i.isdigit()])),
            species=StimulusSpecies.HUMAN if "human" in path else StimulusSpecies.DOG,
            gaze_direction=(
                StimulusGazeDirection.LEFT_GAZE
                if "_L" in path
                else StimulusGazeDirection.RIGHT_GAZE
            ),
        )
        stimuli.append(stimulus)
