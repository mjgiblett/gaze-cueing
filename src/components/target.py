"""
Defines experimental targets. 
"""

from dataclasses import dataclass
from enum import IntEnum, auto
from pathlib import Path
from typing import Any, Iterator

from pygame.image import load
from pygame.transform import scale

from src.constants import POSITIONS, TARGET_SCALE, TARGETS_PATH
from src.visuals import Image


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


@dataclass
class Target:
    image: Image
    letter: TargetLetter
    location: TargetLocation

    def __iter__(self) -> Iterator[tuple[str, Any]]:
        for key, value in self.__dict__.items():
            yield f"target_{key}", value


targets: list[Target] = []


def init_targets() -> None:
    """
    Initialises the experimental targets.

    Returns
    -------
    None
    """
    for file in Path(TARGETS_PATH).glob("*.tif"):
        path = str(file)
        surface = scale(load(path), TARGET_SCALE)

        left_target = Target(
            image=Image(surface, POSITIONS["left_target"]),
            letter=TargetLetter.L if "L" in str(file) else TargetLetter.T,
            location=TargetLocation.LEFT_TARGET,
        )
        right_target = Target(
            image=Image(surface, POSITIONS["right_target"]),
            letter=TargetLetter.L if "L" in str(file) else TargetLetter.T,
            location=TargetLocation.RIGHT_TARGET,
        )

        targets.extend([left_target, right_target])
