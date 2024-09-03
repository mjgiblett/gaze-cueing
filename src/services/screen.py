import pygame

from src.constants import (
    DISPLAY_HEIGHT,
    DISPLAY_WIDTH,
    IS_FULLSCREEN,
    POSITIONS,
    SCREEN_DIMENSIONS,
    STIMULUS_SCALE,
    TARGET_OFFSET,
    TARGET_SCALE,
)


def init_screen() -> pygame.Surface:
    flags = 0
    size = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
    if IS_FULLSCREEN:
        size = (0, 0)
        flags = pygame.FULLSCREEN
    pygame.display.set_caption("Gaze Cueing Experiment")
    screen = pygame.display.set_mode(size, flags)
    x, y = screen.get_size()
    SCREEN_DIMENSIONS.update(
        {
            "centre": (x // 2, y // 2),
            "size": (x, y),
        }
    )
    scale_offset = TARGET_SCALE[0] // 2
    x, y = SCREEN_DIMENSIONS["centre"]
    POSITIONS.update(
        {
            "stimuli": (x - (STIMULUS_SCALE[0] // 2), y - STIMULUS_SCALE[1] // 2),
            "left_target": (x - TARGET_OFFSET - scale_offset, y - scale_offset),
            "right_target": (x + TARGET_OFFSET, y - scale_offset),
        }
    )
    return screen
