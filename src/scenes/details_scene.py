"""
Defines DetailsScene class.
"""

from pathlib import Path

import pygame

from src.components import Participant
from src.constants import (
    BG_GREY,
    DATA_PATH,
    ERROR_RED,
    SCREEN_DIMENSIONS,
    TEXT_AGE,
    TEXT_AGE_INFO,
    TEXT_CONTINUE,
    TEXT_CULTURE,
    TEXT_CULTURE_INFO,
    TEXT_GENDER,
    TEXT_GENDER_INFO,
    TEXT_ID,
    TEXT_ID_INFO,
    TEXT_INSTRUCTIONS_DETAILS,
    TEXT_TITLE,
)
from src.gui import Button, InputBox
from src.scenes.scene import Scene
from src.visuals import MultilineText, Text, fonts


class DetailsScene(Scene):
    """
    Collects the detials of the participant.
    Attributes
    ----------
    screen: pygame.Surface
        The main window displaying the experiment.
    Methods
    -------
    display()
        Displays the scene on the main window.
    update_state()
        Communicates to the SceneManager when to trasition from this scene to the next.
    key_down()
        Handles key down events.
    button_down()
        Handles mouse button down events.
    mouse_motion()
        Handles mouse motion events.
    """

    def __init__(self, screen: pygame.Surface) -> None:
        super().__init__(screen)

        id = 1
        for file in Path(DATA_PATH).rglob("*.xlsx"):
            if file.stem.isnumeric():
                num = int(file.stem)
                id = num if num > id else id
        centre_x = SCREEN_DIMENSIONS["centre"][0]

        self.participant = None
        self.elements = [
            Text(
                string=TEXT_TITLE,
                font=fonts["title"],
                position=(centre_x, 150),
            ),
            Text(
                string=TEXT_INSTRUCTIONS_DETAILS,
                font=fonts["text"],
                position=(centre_x, 280),
            ),
            Text(
                string=TEXT_ID,
                font=fonts["heading"],
                position=(centre_x, 350),
            ),
            Text(
                string=TEXT_AGE,
                font=fonts["heading"],
                position=(centre_x, 450),
            ),
            Text(
                string=TEXT_GENDER,
                font=fonts["heading"],
                position=(centre_x, 550),
            ),
            Text(
                string=TEXT_CULTURE,
                font=fonts["heading"],
                position=(centre_x, 650),
            ),
            Text(
                string=TEXT_ID_INFO,
                font=fonts["text"],
                position=(centre_x, 850),
                name=TEXT_ID,
                is_enabled=False,
            ),
            Text(
                string=TEXT_AGE_INFO,
                font=fonts["text"],
                position=(centre_x, 850),
                name=TEXT_AGE,
                is_enabled=False,
            ),
            MultilineText(
                string=TEXT_GENDER_INFO,
                font=fonts["text"],
                position=(centre_x, 850),
                name=TEXT_GENDER,
                is_enabled=False,
            ),
            MultilineText(
                string=TEXT_CULTURE_INFO,
                font=fonts["small"],
                position=(centre_x, 850),
                name=TEXT_CULTURE,
                is_enabled=False,
            ),
        ]
        self.interactables = [
            Button(
                Text(
                    string=TEXT_CONTINUE,
                    font=fonts["button"],
                    text_colour=BG_GREY,
                ),
                position=(centre_x, 780),
                name=TEXT_CONTINUE,
            ),
            InputBox(
                text=Text(string=str(id), font=fonts["text"]),
                name=TEXT_ID,
                position=(centre_x, 400),
                is_numeric=True,
                char_limit=6,
            ),
            InputBox(
                text=Text("", font=fonts["text"]),
                name=TEXT_AGE,
                position=(centre_x, 500),
                is_numeric=True,
                char_limit=3,
            ),
            InputBox(
                text=Text("", font=fonts["text"]),
                name=TEXT_GENDER,
                position=(centre_x, 600),
                is_numeric=True,
                char_limit=1,
            ),
            InputBox(
                text=Text("", font=fonts["text"]),
                name=TEXT_CULTURE,
                position=(centre_x, 700),
                is_numeric=True,
                char_limit=1,
            ),
        ]

    def key_down(self, key: int) -> None:
        for interactable in self.interactables:
            if interactable.is_active:
                if not isinstance(interactable, InputBox):
                    continue
                interactable.key_down(key)
                return

    def button_down(self, _: int, pos: tuple[int, int]) -> None:
        participant_details: dict[str, int] = {}
        for interactable in self.interactables:
            is_clicked = interactable.is_clicked(pos)
            for element in self.elements:
                if element.name == "":
                    continue
                if element.name != interactable.name:
                    continue
                element.is_enabled = is_clicked
            if not is_clicked:
                continue
            if interactable.name != TEXT_CONTINUE:
                continue
            for box in self.interactables:
                if not isinstance(box, InputBox):
                    continue
                title = box.name
                if box.text.string == "":
                    box.background_colour = ERROR_RED
                    return
                val = int(box.text.string)
                if title == TEXT_AGE:
                    if val < 18 or val > 120:
                        box.text.string = ""
                        box.background_colour = ERROR_RED
                        return
                elif title == TEXT_GENDER:
                    if val not in (1, 2, 3):
                        box.text.string = ""
                        box.background_colour = ERROR_RED
                        return
                elif title == TEXT_CULTURE:
                    if val not in range(1, 10):
                        box.text.string = ""
                        box.background_colour = ERROR_RED
                        return
                participant_details[title.lower()] = int(box.text.string)
            self.participant = Participant(**participant_details)
            self.progress = True
            return
