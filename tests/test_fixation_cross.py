import unittest

import pygame

from src.visuals.fixation_cross import FixationCross
from tests.tools import minimal_setup

size = (25, 25)
name = "bob"
is_enabled = False


class TestElement(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super(TestElement, cls).setUpClass()
        cls.screen = minimal_setup()

    def setUp(self) -> None:
        self.fixation_cross = FixationCross(self.screen, size, name, is_enabled)

    def test_init(self) -> None:
        position = self.screen.get_width() // 2, self.screen.get_height() // 2
        self.assertEqual(position, self.fixation_cross.position)
        self.assertEqual(size, self.fixation_cross.size)
        self.assertEqual(is_enabled, self.fixation_cross.is_enabled)
        self.assertIsInstance(self.fixation_cross.rect, pygame.Rect)
        self.assertIsInstance(self.fixation_cross.rects, list)


if __name__ == "__main__":
    unittest.main()
