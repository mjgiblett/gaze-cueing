import unittest
from pathlib import Path
from random import choice

import pygame

from src.visuals import Image
from tests.tools import minimal_setup, test_blit

images_path = "resources"
position = (10, 10)
size = (25, 25)
name = "Lily"
is_enabled = True


class TestImage(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super(TestImage, cls).setUpClass()
        cls.screen = minimal_setup()
        cls.paths = [str(path) for path in Path(images_path).rglob("*.tif")]

        # Test that python can load all image resources

    def setUp(self) -> None:
        self.image = Image(choice(self.paths), position, size, name, is_enabled)

    def test_load_all_image_resources(self) -> None:
        for path in self.paths:
            image = pygame.image.load(path)
            Image(image, position, size)

    def test_init_image(self) -> None:
        self.assertEqual(position, self.image.position)
        self.assertEqual(size, self.image.size)
        self.assertEqual(is_enabled, self.image.is_enabled)
        self.assertIsInstance(self.image.rect, pygame.Rect)
        self.assertIsInstance(self.image.surface, pygame.Surface)

    def test_assign_position(self) -> None:
        new_position = (50, 50)
        self.image.position = new_position
        self.assertEqual(self.image.position, new_position)

    def test_assign_size(self) -> None:
        old_surface = self.image.surface
        new_size = (50, 50)
        self.image.size = new_size
        self.assertEqual(self.image.size, new_size)
        self.assertNotEqual(self.image.surface, old_surface)

    def test_assign_native_resolution(self) -> None:
        self.assertNotEqual(self.image.surface, self.image._original_surface)
        self.image.size = (0, 0)
        self.assertEqual(self.image.surface, self.image._original_surface)

    def test_assign_rect(self):
        with self.assertRaises(AttributeError):
            self.image.rect = pygame.Rect((0, 0), (0, 0))

    def test_assign_surface(self) -> None:
        old_surface = self.image.surface
        old_position = self.image.position
        old_size = self.image.size
        self.image.surface = choice(self.paths)
        self.assertNotEqual(self.image.surface, old_surface)
        self.assertEqual(self.image.position, old_position)
        self.assertEqual(self.image.size, old_size)

    def test_draw_when_enabled(self) -> None:
        test_blit(self, self.image, self.screen)

    def test_draw_when_disabled(self) -> None:
        self.image.is_enabled = False
        test_blit(self, self.image, self.screen, False)


if __name__ == "__main__":
    unittest.main()
