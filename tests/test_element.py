import unittest
from unittest.mock import patch

import pygame

from src.visuals.element import Element
from tests.tools import minimal_setup

position = (10, 10)
size = (25, 25)
name = "bob"
is_enabled = False


class TestElement(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super(TestElement, cls).setUpClass()
        cls.screen = minimal_setup()

    @patch.multiple(Element, __abstractmethods__=set())
    def setUp(self) -> None:
        self.element = Element(position, size, name, is_enabled)

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


if __name__ == "__main__":
    unittest.main()
