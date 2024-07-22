import unittest

import pygame

from src.constants import BLACK
from src.visuals.fonts import fonts
from src.visuals.text import Text
from tests.tools import minimal_setup, test_blit

screen = minimal_setup()

string: str = "pizza"
font: pygame.font.Font = fonts["text"]
position: tuple[int, int] = (40, 30)
colour: pygame.Color = BLACK
name: str = "victor"
is_enabled: bool = True


class TestText(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super(TestText, cls).setUpClass()
        cls.screen = screen

    def setUp(self) -> None:
        self.text = Text(string, font, position, colour, name, is_enabled)

    def test_init(self) -> None:
        self.assertEqual(self.text.string, string)
        self.assertEqual(self.text.font, font)
        self.assertEqual(self.text.position, position)
        self.assertEqual(self.text.text_colour, colour)
        self.assertEqual(self.text.name, name)
        self.assertEqual(self.text.is_enabled, is_enabled)
        self.assertIsInstance(self.text.render, pygame.Surface)
        self.assertIsInstance(self.text.rect, pygame.Rect)

    def test_change_string(self) -> None:
        old_size = self.text.size
        old_position = self.text.position
        new_string = "taco"

        self.text.string = new_string

        self.assertNotEqual(self.text.size, old_size)
        self.assertEqual(self.text.position, old_position)
        self.assertEqual(self.text.string, new_string)

    def test_change_font(self) -> None:
        old_size = self.text.size
        old_position = self.text.position
        new_font = fonts["title"]

        self.text.font = new_font

        self.assertNotEqual(self.text.size, old_size)
        self.assertEqual(self.text.position, old_position)
        self.assertEqual(self.text.font, new_font)

    def test_size_assignment(self):
        with self.assertRaises(AttributeError):
            self.text.size = (0, 0)

    def test_rect_assignment(self):
        with self.assertRaises(AttributeError):
            self.text.rect = pygame.Rect((0, 0), (0, 0))

    def test_display_when_enabled(self) -> None:
        blit_wrapper = test_blit(self, self.text, self.screen)
        self.assertTrue(
            ((self.text.render, self.text.rect), {}) in blit_wrapper.blit_calls
        )

    def test_display_when_disabled(self) -> None:
        self.text.is_enabled = False
        test_blit(self, self.text, self.screen, False)


if __name__ == "__main__":
    unittest.main()
