"""
Module providing constants used by other modules.
"""
import pygame

# Display

FRAMERATE = 144
DISPLAY_FRAMERATE = False

IS_FULLSCREEN = True
DISPLAY_WIDTH = 1200
DISPLAY_HEIGHT = 1200

# Colours

WHITE = pygame.Color("white")
BLACK = pygame.Color("black")
BG_GREY = pygame.Color(175, 175, 175)
DARK_GREY = pygame.Color(75, 75, 75)
SUBTLE = pygame.Color(192, 190, 200)
LIGHT = pygame.Color(224, 222, 244)
ERROR_RED = pygame.Color(244, 80, 105)

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

SPECIES_COUNTERBALANCING = False  # When false, species of stimuli will be random.
COUNTERBALANCING_ASCENDING = True
