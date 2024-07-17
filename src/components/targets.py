"""
Defines experimental targets. 
"""
from enum import IntEnum, auto
from pathlib import Path

import pygame

from src.constants import TARGET_OFFSET, TARGET_SCALE
from src.visuals.image import Image


class TargetLetter(IntEnum):
    """
    An int representing the letter of a target.
    """

    L = auto()
    T = auto()


class TargetLocation(IntEnum):
    """
    An int representing the location of a target.
    """

    LEFT_TARGET = auto()
    RIGHT_TARGET = auto()


targets: list[dict] = []


def init_targets(screen: pygame.Surface) -> None:
    """
    Initialises the experimental targets.
    Parameters
    ----------
    screen: pygame.Surface
        Main window displaying the experiment.
    Returns
    -------
    None
    """
    centre = tuple(x // 2 for x in screen.get_size())

    for file in Path("resources/targets").glob("*.tif"):
        image = pygame.image.load(file)
        image = pygame.transform.scale(image, TARGET_SCALE)

        letter = TargetLetter.L if "L" in str(file) else TargetLetter.T

        targets.append(
            {
                "target_letter": letter.value,
                "target_location": TargetLocation.LEFT_TARGET.value,
                "target_image": Image(
                    image,
                    (
                        centre[0] - TARGET_OFFSET - (TARGET_SCALE[0] // 2),
                        centre[1] - (TARGET_SCALE[0] // 2),
                    ),
                ),
            }
        )
        targets.append(
            {
                "target_letter": letter.value,
                "target_location": TargetLocation.RIGHT_TARGET.value,
                "target_image": Image(
                    image,
                    (
                        centre[0] + TARGET_OFFSET,
                        centre[1] - (TARGET_SCALE[0] // 2),
                    ),
                ),
            }
        )
