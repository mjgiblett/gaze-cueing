import unittest

import pygame

from src.constants import BLACK
from src.visuals.fixation_cross import FixationCross
from tests.tools import minimal_setup, test_draw_rect

size = (25, 25)
name = "bob"
is_enabled = True


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

    def test_position_assignment(self):
        with self.assertRaises(AttributeError):
            self.fixation_cross.position = (0, 0)

    def test_size_assignment(self):
        with self.assertRaises(AttributeError):
            self.fixation_cross.size = (0, 0)

    def test_rect_assignment(self):
        with self.assertRaises(AttributeError):
            self.fixation_cross.rect = pygame.Rect((0, 0), (0, 0))

    def test_rects_assignment(self):
        with self.assertRaises(AttributeError):
            self.fixation_cross.rects = []

    def test_display_when_enabled(self) -> None:
        test_draw_rect(self, self.fixation_cross, self.screen)

        # Check if fixation cross calls the rect method with the correct parameters
        for rect in self.fixation_cross.rects:
            pygame.draw.rect.assert_any_call(self.screen, BLACK, rect)

    def test_display_when_disabled(self) -> None:
        self.fixation_cross.is_enabled = False
        test_draw_rect(self, self.fixation_cross, self.screen, False)


if __name__ == "__main__":
    unittest.main()
