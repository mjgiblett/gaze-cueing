import unittest

import pygame

from src.constants import BLACK, WHITE
from src.visuals.element import Element
from tests.tools import minimal_setup, test_draw_rect

position = (10, 10)
size = (25, 25)
name = "bob"
background_colour = None
border_colour = None
border_width = 6
border_radius = 10
is_enabled = True


class TestElement(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super(TestElement, cls).setUpClass()
        cls.screen = minimal_setup()

    def setUp(self) -> None:
        self.element = Element(
            position,
            size,
            name,
            background_colour,
            border_colour,
            border_width,
            border_radius,
            is_enabled,
        )

    def test_init_element(self) -> None:
        self.assertEqual(position, self.element.position)
        self.assertEqual(size, self.element.size)
        self.assertEqual(is_enabled, self.element.is_enabled)
        self.assertIsInstance(self.element.rect, pygame.Rect)

    def test_move_element(self) -> None:
        move_position = (50, 50)
        self.element.position = move_position
        self.assertEqual(self.element.position, move_position)

    def test_change_size(self) -> None:
        new_size = (50, 50)
        self.element.size = new_size
        self.assertEqual(self.element.size, new_size)

    def test_change_rect(self) -> None:
        new_rect_position = (100, 100)
        new_rect_size = (50, 50)
        new_rect = pygame.Rect(new_rect_position, new_rect_size)

        self.element.rect = new_rect

        self.assertEqual(self.element.rect, new_rect)
        self.assertEqual(self.element.position, position)
        self.assertEqual(self.element.size, new_rect_size)

    def test_draw_nothing_enabled(self) -> None:
        test_draw_rect(self, self.element, self.screen, False)

    def test_draw_nothing_disabled(self) -> None:
        self.element.is_enabled = False
        test_draw_rect(self, self.element, self.screen, False)

    def test_draw_background(self) -> None:
        self.element.background_colour = BLACK
        test_draw_rect(self, self.element, self.screen)
        pygame.draw.rect.assert_any_call(
            self.screen, BLACK, self.element.rect, border_radius=border_radius
        )

    def test_draw_border(self) -> None:
        self.element.border_colour = WHITE
        test_draw_rect(self, self.element, self.screen)
        pygame.draw.rect.assert_any_call(
            self.screen, WHITE, self.element.rect, border_width, border_radius
        )

    def test_draw_background_and_border(self) -> None:
        self.element.background_colour = BLACK
        self.element.border_colour = WHITE
        test_draw_rect(self, self.element, self.screen)
        pygame.draw.rect.assert_any_call(
            self.screen, BLACK, self.element.rect, border_radius=border_radius
        )
        pygame.draw.rect.assert_any_call(
            self.screen, WHITE, self.element.rect, border_width, border_radius
        )


if __name__ == "__main__":
    unittest.main()
