"""
Defines SceneManager class, which handles pygame events and game scenes.
"""

import pygame

from src.scenes.details_scene import DetailsScene
from src.scenes.experiment_scene import ExperimentScene
from src.scenes.finished_scene import FinishedScene
from src.scenes.scene import QuitActionType, Scene
from src.scenes.start_scene import StartScene
from src.services.trial_manager import TrialManager


class SceneManager:
    """
    Manages pygame events and game scenes during each game iteration.
    Attributes
    ----------
    screen: pygame.Surface
        The main window displaying the experiment.
    Methods
    -------
    process_game_events()
        Manages all pygame events, delegates events to the active scene, and updates the state of scenes.
    start_new_scene()
        Replaces the active scene with the next.
    """

    def __init__(self, screen: pygame.Surface) -> None:
        self.active_scene: Scene = StartScene(screen)
        self.trial_manager: TrialManager = TrialManager()
        self.time = 0

    def process_game_events(self) -> QuitActionType:
        """
        Manages all pygame events, delegates events to the active scene, and updates the state of scenes.
        Returns
        -------
        QuitActionType
            Communicates whether program should continue, quit, or restart.
        """
        self.time = pygame.time.get_ticks()
        quit_action = QuitActionType.CONTINUE

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return QuitActionType.QUIT
            elif event.type == pygame.MOUSEMOTION:
                self.active_scene.mouse_motion(event.pos)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button in (1, 3):
                    self.active_scene.button_down(event.button, event.pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return QuitActionType.QUIT
                if event.key == pygame.K_r and isinstance(
                    self.active_scene, FinishedScene
                ):
                    return QuitActionType.RESTART
                if isinstance(self.active_scene, ExperimentScene):
                    self.trial_manager.key_down(self.time, event.key)
                self.active_scene.key_down(event.key)

        if self.active_scene.update_state():
            self.start_new_scene()
            return QuitActionType.CONTINUE

        if isinstance(self.active_scene, ExperimentScene):
            if self.trial_manager.has_experiment_finished:
                self.start_new_scene()
                return QuitActionType.CONTINUE
            elements = self.trial_manager.during_trial(self.time)
            self.active_scene.is_resting = self.trial_manager.is_resting
            self.active_scene.display(elements)
        else:
            self.active_scene.display()

        return quit_action

    def start_new_scene(self) -> None:
        """
        Replaces the active scene with the next.
        Uses the class of the active scene to determine the next.
        Returns
        -------
        None
        """
        if isinstance(self.active_scene, StartScene):
            self.active_scene = DetailsScene(self.active_scene.screen)
        elif isinstance(self.active_scene, DetailsScene):
            if self.active_scene.participant:
                self.trial_manager.participant = self.active_scene.participant
            else:
                assert self.active_scene.participant, "No Participant"
            self.active_scene = ExperimentScene(self.active_scene.screen)
            self.trial_manager.start_experiment(self.time)
        elif isinstance(self.active_scene, ExperimentScene):
            self.active_scene = FinishedScene(self.active_scene.screen)
            self.trial_manager.end_experiment(self.time)
