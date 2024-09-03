"""
Module providing default project constants.
"""

import pygame

# resources paths

STIMULI_PATH = "resources/stimuli"
TARGETS_PATH = "resources/targets"

# Display

FRAMERATE = 144
TRIAL_DEBUGGING = False
SHOW_FRAMERATE = False or TRIAL_DEBUGGING

IS_FULLSCREEN = True
DISPLAY_WIDTH = 1920
DISPLAY_HEIGHT = 1080
SCREEN_DIMENSIONS: dict[str, tuple[int, int]] = {}
POSITIONS: dict[str, tuple[int, int]] = {}

# Colours

WHITE = pygame.Color("white")
BLACK = pygame.Color("black")
BG_GREY = pygame.Color(175, 175, 175)
ERROR_RED = pygame.Color(244, 80, 105)

# Fonts

FONT_NAME = "calibri"
FONT_PROPERTIES = {
    "title": {"name": FONT_NAME, "size": 75, "bold": True},
    "heading": {"name": FONT_NAME, "size": 40, "bold": False},
    "text": {"name": FONT_NAME, "size": 30, "bold": False},
    "small": {"name": FONT_NAME, "size": 20, "bold": False},
    "button": {"name": FONT_NAME, "size": 30, "bold": True},
}

# Experiment parameters

INTER_TRIAL_INTERVAL = 670
STIMULUS_ONSET_ASYNCS = (100, 300, 700)
MAX_RESPONSE_TIME = 2000

FIXATION_CROSS_WIDTH = 4
FIXATION_CROSS_HEIGHT = 20

TARGET_SCALE = (100, 100)
STIMULUS_SCALE = (400, 400)

TARGET_OFFSET = 500

RANDOM_TRIAL_ORDER = True

FIRST_TRIAL_DELAY = 1000
MINIMUM_REST_TIME = 2000

SPECIES_COUNTERBALANCING = True  # Complete one species condition before the other.
COUNTERBALANCING_ASCENDING = (
    False  # Determines the order of counterbalancing. Humans first when True.
)
