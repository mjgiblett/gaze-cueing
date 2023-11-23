"""
Defines experimental stimuli. 
"""
from enum import IntEnum, auto
from pathlib import Path

import pygame

from src.components.image import Image
from src.constants import STIMULUS_SCALE


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


stimuli: list[dict] = []


def init_stimuli(screen: pygame.Surface) -> None:
    """
    Initialises the experimental stimuli.
    Parameters
    ----------
    screen: pygame.Surface
        Main window displaying the experiment.
    Returns
    -------
    None
    """
    centre = screen.get_size()[0] // 2, screen.get_size()[1] // 2
    centre = centre[0] - (STIMULUS_SCALE[0] // 2), centre[1] - (STIMULUS_SCALE[1] // 2)

    for file in Path("resources/stimuli").rglob("*.tif"):
        image = pygame.image.load(file)
        image = pygame.transform.scale(image, STIMULUS_SCALE)
        species = StimulusSpecies.HUMAN if "human" in str(file) else StimulusSpecies.DOG
        direction = (
            StimulusGazeDirection.LEFT_GAZE
            if "_L" in str(file)
            else StimulusGazeDirection.RIGHT_GAZE
        )
        number = int("".join([i for i in [*str(file)] if i.isdigit()]))
        stimuli.append(
            {
                "stimulus_species": species.value,
                "stimulus_gaze_direction": direction.value,
                "stimulus_number": number,
                "stimulus_image": Image(image, centre),
            }
        )
