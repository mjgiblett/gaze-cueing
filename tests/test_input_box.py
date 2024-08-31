import unittest

import pygame

from src.constants import BLACK, WHITE
from src.gui import InputBox
from src.visuals import Text, fonts
from tests.tools import minimal_setup, test_blit, test_draw_rect

screen = minimal_setup()

string = "I am an input box"
font = fonts["text"]
position = (10, 10)
size = (25, 25)
name = "Scarlet"
background_colour = None
border_colour = None
border_width = 6
border_radius = 10
is_enabled = True
is_active = False
is_numeric = False


class TestInputBox(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super(TestInputBox, cls).setUpClass()
        cls.screen = screen

    def setUp(self) -> None:
        text = Text(string, font)
        self.input_box = InputBox(
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
            is_numeric,
        )

    def test_init_input_box(self) -> None:
        self.assertEqual(position, self.input_box.position)
        self.assertNotEqual(size, self.input_box.size)
        self.assertEqual(is_enabled, self.input_box.is_enabled)
        self.assertIsInstance(self.input_box.rect, pygame.Rect)

    def test_move_element(self) -> None:
        move_position = (50, 50)
        self.input_box.position = move_position
        self.assertEqual(self.input_box.position, move_position)

    def test_change_size(self) -> None:
        new_size = (50, 50)
        self.input_box.size = new_size
        self.assertEqual(self.input_box.size, new_size)

    def test_change_rect(self) -> None:
        new_rect_position = (100, 100)
        new_rect_size = (50, 50)
        new_rect = pygame.Rect(new_rect_position, new_rect_size)

        self.input_box.rect = new_rect

        self.assertEqual(self.input_box.rect, new_rect)
        self.assertEqual(self.input_box.position, position)
        self.assertEqual(self.input_box.size, new_rect_size)

    def test_draw_when_enabled(self) -> None:
        test_draw_rect(self, self.input_box, self.screen, False)

    def test_draw_when_disabled(self) -> None:
        self.input_box.is_enabled = False
        test_draw_rect(self, self.input_box, self.screen, False)

    def test_draw_background_and_border(self) -> None:
        self.input_box.background_colour = BLACK
        self.input_box.border_colour = WHITE
        test_draw_rect(self, self.input_box, self.screen)
        pygame.draw.rect.assert_any_call(
            self.screen, BLACK, self.input_box.rect, border_radius=border_radius
        )
        pygame.draw.rect.assert_any_call(
            self.screen, WHITE, self.input_box.rect, border_width, border_radius
        )

    def test_display_when_enabled(self) -> None:
        blit_wrapper = test_blit(self, self.input_box, self.screen)
        self.assertTrue(
            ((self.input_box.text.render, self.input_box.text.rect), {})
            in blit_wrapper.blit_calls
        )

    def test_display_when_disabled(self) -> None:
        self.input_box.is_enabled = False
        test_blit(self, self.input_box, self.screen, False)

    def test_edit_string(self) -> None:
        self.input_box.is_active = True
        self.input_box.key_down(pygame.K_EXCLAIM)
        self.assertEqual(self.input_box.text.string, string + "!")
        self.input_box.key_down(pygame.K_BACKSPACE)
        self.assertEqual(self.input_box.text.string, string)
        self.input_box.key_down(pygame.K_RETURN)
        self.assertFalse(self.input_box.is_active)

    def test_edit_string_numeric_only(self) -> None:
        self.input_box.is_active = True
        self.input_box.is_numeric = True
        self.input_box.key_down(pygame.K_1)
        self.input_box.key_down(pygame.K_EXCLAIM)
        self.assertEqual(self.input_box.text.string, string + "1")


if __name__ == "__main__":
    unittest.main()
