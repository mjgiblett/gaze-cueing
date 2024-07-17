import unittest

import pygame

from src.scenes.details_scene import DetailsScene
from src.scenes.experiment_scene import ExperimentScene
from src.scenes.finished_scene import FinishedScene
from src.scenes.scene import QuitActionType
from src.scenes.start_scene import StartScene
from src.services.scene_manager import SceneManager
from tests.tools import minimal_setup


class TestSceneManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super(TestSceneManager, cls).setUpClass()
        cls.screen = minimal_setup()

    def setUp(self) -> None:
        self.scene_manager = SceneManager(self.screen)

    def test_start_scene(self) -> None:
        self.assertIsInstance(self.scene_manager.active_scene, StartScene)
        self.assertFalse(self.scene_manager.active_scene.update_state())

    def test_escape_key_down(self) -> None:
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE)
        pygame.event.post(event)
        self.assertEqual(self.scene_manager.process_game_events(), QuitActionType.QUIT)

    def test_pygame_quit(self) -> None:
        event = pygame.event.Event(pygame.QUIT)
        pygame.event.post(event)
        self.assertEqual(self.scene_manager.process_game_events(), QuitActionType.QUIT)

    def test_experiment_progression(self) -> None:
        # details scene
        self.scene_manager.start_new_scene()
        self.assertIsInstance(self.scene_manager.active_scene, DetailsScene)
        # experiment scene
        self.scene_manager.start_new_scene()
        self.assertIsInstance(self.scene_manager.active_scene, ExperimentScene)
        # finished scene
        self.scene_manager.start_new_scene()
        self.assertIsInstance(self.scene_manager.active_scene, FinishedScene)

        # test restart
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_r)
        pygame.event.post(event)
        self.assertEqual(
            self.scene_manager.process_game_events(), QuitActionType.RESTART
        )

    def test_continue_when_nothing_happens(self) -> None:
        self.assertEqual(
            self.scene_manager.process_game_events(), QuitActionType.CONTINUE
        )


if __name__ == "__main__":
    unittest.main()
