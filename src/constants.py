"""
Module providing default project constants.
"""
import pygame

# Display

FRAMERATE = 144
SHOW_FRAMERATE = False

IS_FULLSCREEN = True
DISPLAY_WIDTH = 1200
DISPLAY_HEIGHT = 1200

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
TRIAL_DEBUGGING = False

SPECIES_COUNTERBALANCING = True  # Complete one species condition before the other.
COUNTERBALANCING_ASCENDING = (
    False  # Determines the order of counterbalancing. Humans first when True.
)
