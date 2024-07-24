from typing import Any
from unittest import TestCase
from unittest.mock import Mock

import pygame

from src.constants import DISPLAY_HEIGHT, DISPLAY_WIDTH
from src.visuals import Element, init_fonts


class BlitWrapper(pygame.Surface):
    """
    The BlitWrapper class wraps around a Pygame surface and intercepts
    blit calls, storing the arguments and keyword arguments of each call
    in a list. This class is a substitute for
    pygame.Surface.blit = unittest.mock.Mock since blit is read-only.
    """

    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.blit_calls = []

    def blit(self, *args, **kwargs) -> pygame.Rect:
        self.blit_calls.append((args, kwargs))
        return self.screen.blit(*args, **kwargs)

    def __getattr__(self, attr) -> Any:
        return getattr(self.screen, attr)


def minimal_setup() -> pygame.Surface:
    pygame.init()
    init_fonts()
    return pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))


def test_draw_rect(
    test: TestCase, element: Element, screen: pygame.Surface, assert_true: bool = True
) -> None:
    pygame.draw.rect = Mock()
    element.draw(screen)

    # check if element calls the pygame.draw.rect method.
    if assert_true:
        test.assertTrue(pygame.draw.rect.called)
    else:
        test.assertFalse(pygame.draw.rect.called)


def test_blit(
    test: TestCase, element: Element, screen: pygame.Surface, assert_true: bool = True
) -> BlitWrapper:
    blit_wrapper = BlitWrapper(screen)
    element.draw(blit_wrapper)

    # check if element calls screen.blit method.
    if assert_true:
        test.assertTrue(len(blit_wrapper.blit_calls) > 0)
    else:
        test.assertFalse(len(blit_wrapper.blit_calls) > 0)

    return blit_wrapper
