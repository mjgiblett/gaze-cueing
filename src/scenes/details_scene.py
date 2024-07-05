"""
Defines DetailsScene class.
"""
import pygame

from src.constants import ERROR_RED
from src.gui.button import Button
from src.gui.fonts import fonts
from src.gui.input_box import InputBox
from src.gui.text import Text
from src.scenes.scene import Scene


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
        self.participant_details: dict[str, int] = {}
        x_centre = self.screen.get_size()[0] // 2

        self.title = Text(
            "Participant Details", fonts["title"], (x_centre, 200), is_centred=True
        )
        self.button = Button("Start", fonts["button"], (x_centre, 780), is_centred=True)
        self.headings = [
            Text("NUMBER", fonts["heading"], (x_centre, 350), is_centred=True),
            Text("AGE", fonts["heading"], (x_centre, 450), is_centred=True),
            Text("GENDER", fonts["heading"], (x_centre, 550), is_centred=True),
            Text("CULTURE", fonts["heading"], (x_centre, 650), is_centred=True),
        ]
        self.input_boxes = [
            InputBox(
                "participant_number",
                fonts["text"],
                (x_centre, 400),
                is_numeric=True,
                is_centred=True,
                char_limit=3,
            ),
            InputBox(
                "age",
                fonts["text"],
                (x_centre, 500),
                is_numeric=True,
                is_centred=True,
                char_limit=3,
            ),
            InputBox(
                "gender",
                fonts["text"],
                (x_centre, 600),
                is_numeric=True,
                is_centred=True,
                char_limit=1,
            ),
            InputBox(
                "culture",
                fonts["text"],
                (x_centre, 700),
                is_numeric=True,
                is_centred=True,
                char_limit=1,
            ),
        ]
        self.info_texts = {
            "participant_number": Text(
                "Please enter your participant number.",
                fonts["text"],
                (x_centre, 850),
                is_centred=True,
            ),
            "age": Text(
                "Please enter your age in years. Minimum 18.",
                fonts["text"],
                (x_centre, 850),
                is_centred=True,
            ),
            "gender": Text(
                (
                    "Please indicate the category that best describes your gender:"
                    "\n1 - male"
                    "\n2 - female"
                    "\n3 - unspecified"
                ),
                fonts["text"],
                (x_centre, 850),
                is_centred=True,
            ),
            "culture": Text(
                (
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
                ),
                fonts["small"],
                (x_centre, 850),
                is_centred=True,
            ),
        }

    def display(self) -> None:
        self.title.display(self.screen)
        self.button.display(self.screen)
        for heading in self.headings:
            heading.display(self.screen)
        for box in self.input_boxes:
            box.display(self.screen)
            info_text = self.info_texts[box.title]
            info_text.is_enabled = box.is_active
            if box.is_active:
                info_text.display(self.screen)

    def key_down(self, key: int) -> None:
        for box in self.input_boxes:
            if box.is_active:
                box.edit_text(key)
                return

    def button_down(self, _: int, pos: tuple[int, int]) -> None:
        if self.button.is_clicked(pos):
            for box in self.input_boxes:
                title = box.title
                if box.text == "":
                    return
                val = int(box.text)
                if title == "age":
                    if val < 18 or val > 120:
                        box.text = ""
                        box.bg_colour = ERROR_RED
                        return
                elif title == "gender":
                    if val not in (1, 2, 3):
                        box.text = ""
                        box.bg_colour = ERROR_RED
                        return
                elif title == "culture":
                    if val not in range(1, 10):
                        box.text = ""
                        box.bg_colour = ERROR_RED
                        return
                self.participant_details[title] = int(box.text)
            self.progress = True
            return

        for box in self.input_boxes:
            box.is_clicked(pos)
