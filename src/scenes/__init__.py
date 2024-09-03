"""
Defines game scenes. 
"""

from .details_scene import DetailsScene
from .experiment_scene import ExperimentScene
from .finished_scene import FinishedScene
from .scene import QuitActionType, Scene
from .start_scene import StartScene

__all__ = [
    "DetailsScene",
    "ExperimentScene",
    "FinishedScene",
    "QuitActionType",
    "Scene",
    "StartScene",
]
