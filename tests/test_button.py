import unittest

import pygame

from src.constants import BLACK, WHITE
from src.gui import Button
from src.visuals import Text, fonts
from tests.tools import minimal_setup, test_blit, test_draw_rect

screen = minimal_setup()

string = "I am a button"
font = fonts["button"]
position = (10, 10)
size = (25, 25)
name = "Lincoln"
background_colour = None
border_colour = None
border_width = 6
border_radius = 10
is_enabled = True
is_active = False


class TestButton(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super(TestButton, cls).setUpClass()
        cls.screen = screen

    def setUp(self) -> None:
        text = Text(string, font)
        self.button = Button(
            text,
            position,
            size,
            name,
            background_colour,
            border_colour,
            border_width,
            border_radius,
            is_enabled,
            is_active,
        )

    def test_init_button(self) -> None:
        self.assertEqual(position, self.button.position)
        self.assertNotEqual(size, self.button.size)
        self.assertEqual(is_enabled, self.button.is_enabled)
        self.assertIsInstance(self.button.rect, pygame.Rect)

    def test_move_element(self) -> None:
        move_position = (50, 50)
        self.button.position = move_position
        self.assertEqual(self.button.position, move_position)

    def test_change_size(self) -> None:
        new_size = (50, 50)
        self.button.size = new_size
        self.assertEqual(self.button.size, new_size)

    def test_change_rect(self) -> None:
        new_rect_position = (100, 100)
        new_rect_size = (50, 50)
        new_rect = pygame.Rect(new_rect_position, new_rect_size)

        self.button.rect = new_rect

        self.assertEqual(self.button.rect, new_rect)
        self.assertEqual(self.button.position, position)
        self.assertEqual(self.button.size, new_rect_size)

    def test_draw_when_enabled(self) -> None:
        test_draw_rect(self, self.button, self.screen, False)

    def test_draw_when_disabled(self) -> None:
        self.button.is_enabled = False
        test_draw_rect(self, self.button, self.screen, False)

    def test_draw_background_and_border(self) -> None:
        self.button.background_colour = BLACK
        self.button.border_colour = WHITE
        test_draw_rect(self, self.button, self.screen)
        pygame.draw.rect.assert_any_call(
            self.screen, BLACK, self.button.rect, border_radius=border_radius
        )
        pygame.draw.rect.assert_any_call(
            self.screen, WHITE, self.button.rect, border_width, border_radius
        )

    def test_display_when_enabled(self) -> None:
        blit_wrapper = test_blit(self, self.button, self.screen)
        self.assertTrue(
            ((self.button.text.render, self.button.text.rect), {})
            in blit_wrapper.blit_calls
        )

    def test_display_when_disabled(self) -> None:
        self.button.is_enabled = False
        test_blit(self, self.button, self.screen, False)


if __name__ == "__main__":
    unittest.main()
