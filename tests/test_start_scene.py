import unittest

from src.scenes.start_scene import StartScene
from tests.tools import minimal_setup


class TestStartScene(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super(TestStartScene, cls).setUpClass()
        cls.screen = minimal_setup()

    def setUp(self) -> None:
        self.start_scene = StartScene(self.screen)

    def test_start_experiment(self) -> None:
        self.assertFalse(self.start_scene.progress)
        self.assertFalse(self.start_scene.update_state())

    def test_button_down_on_nothing(self) -> None:
        for mouse_button in range(1, 4):
            self.start_scene.button_down(mouse_button, (0, 0))
            self.assertFalse(self.start_scene.progress)
            self.assertFalse(self.start_scene.update_state())


if __name__ == "__main__":
    unittest.main()
