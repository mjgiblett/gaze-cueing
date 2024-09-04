"""
Module providing default project constants.
"""

import pygame

# resources paths

DATA_PATH = "data/"
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
BG_SELECTED = pygame.Color(220, 220, 220)
ERROR_RED = pygame.Color(255, 0, 51)

# Fonts

FONT_NAME = "calibri"
FONT_PROPERTIES = {
    "title": {"name": FONT_NAME, "size": 75, "bold": True},
    "heading": {"name": FONT_NAME, "size": 35, "bold": True},
    "text": {"name": FONT_NAME, "size": 30, "bold": False},
    "small": {"name": FONT_NAME, "size": 25, "bold": False},
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

# --- Text ---

# Start

TEXT_CONTINUE = "Continue"
TEXT_TITLE = "Gaze Cueing Experiment"
TEXT_INSTRUCTIONS = (
    "This experiment is part of a project examining the tuning properties"
    "\nunderlying our capacity to follow gaze direction cues in more naturalistic"
    "\nphotographs of faces. In this experiment you will be responding to letters"
    "\nappearing to the left or right of a central face."
    "\n\nIf the letter is an L, press the SPACE bar. If the letter is a T, press the H key."
    "\nIt is important that you respond as quickly and accurately as you can."
    "\nOnce the experiment begins, it will take 25 - 30 minutes to complete."
    "\nYou may terminate the experiment at any time by pressing the ESCAPE key."
    "\nSome people can experience discomfort (such as a headache) while doing"
    "\nthis type of experiment. Please terminate the experiment if you do."
    "\n\nIf you have read and understood all of this information, please"
    f"\nclick the '{TEXT_CONTINUE}' button when you are ready to continue."
)

# Details

TEXT_INSTRUCTIONS_DETAILS = "Please fill out the following details about yourself."

TEXT_ID = "ID"
TEXT_AGE = "Age"
TEXT_GENDER = "Gender"
TEXT_CULTURE = "Culture"

TEXT_ID_INFO = "Please type your participant ID."
TEXT_AGE_INFO = "Please type your age in years."
TEXT_GENDER_INFO = (
    "Please indicate the category that best describes your gender:"
    "\n1 - male"
    "\n2 - female"
    "\n3 - unspecified"
)
TEXT_CULTURE_INFO = (
    "Please indicate the category that best describes your cultural background:"
    "\n1 - Caucasian"
    "\n2 - Asian (including Indian, south Asian, and multiracial Asian)"
    "\n3 - Indigenous Australian"
    "\n4 - African"
    "\n5 - Hispanic"
    "\n6 - Middle Eastern"
    "\n7 - Pacific Islander"
    "\n8 - other not listed"
    "\n9 - unspecified or prefer not to answer"
)

# Experiment

TEXT_REST = (
    "Take a break!"
    "\nWhen you are ready, press any key to continue with the experiment."
    "\n\nRemember:"
    "\nIf the letter is an L, press the SPACE bar."
    "\nIf the letter is a T, press the H key."
)

# Finished

TEXT_FINISHED = (
    "Experiment complete!\nThank you for participating."
    "\n\nPress ESCAPE to quit or R to restart."
)
