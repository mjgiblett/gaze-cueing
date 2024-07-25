"""
Defines DetailsScene class.
"""
import pygame

from src.constants import BG_GREY, ERROR_RED
from src.gui.button import Button
from src.gui.input_box import InputBox
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
        self.participant_details: dict[str, int] = {}
        x_centre = self.screen.get_size()[0] // 2

        title = Text("Participant Details", fonts["title"], (x_centre, 200))
        heading_number = Text("NUMBER", fonts["heading"], (x_centre, 350))
        heading_age = Text("AGE", fonts["heading"], (x_centre, 450))
        heading_gender = Text("GENDER", fonts["heading"], (x_centre, 550))
        heading_culture = Text("CULTURE", fonts["heading"], (x_centre, 650))

        info_number = Text(
            "Please enter your participant number.",
            fonts["text"],
            (x_centre, 850),
            name="number",
            is_enabled=False,
        )
        info_age = Text(
            "Please enter your age in years. Minimum 18.",
            fonts["text"],
            (x_centre, 850),
            name="age",
            is_enabled=False,
        )
        info_gender = MultilineText(
            (
                "Please indicate the category that best describes your gender:"
                "\n1 - male"
                "\n2 - female"
                "\n3 - unspecified"
            ),
            fonts["text"],
            (x_centre, 850),
            name="gender",
            is_enabled=False,
        )
        info_culture = MultilineText(
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
            name="culture",
            is_enabled=False,
        )

        start_button = Button(
            Text("Start", fonts["button"], text_colour=BG_GREY),
            (x_centre, 780),
            name="start",
        )
        input_number = InputBox(
            text=Text(string="", font=fonts["text"]),
            name="number",
            position=(x_centre, 400),
            is_numeric=True,
            char_limit=300,
        )
        input_age = InputBox(
            text=Text("", font=fonts["text"]),
            name="age",
            position=(x_centre, 500),
            is_numeric=True,
            char_limit=3,
        )
        input_gender = InputBox(
            text=Text("", font=fonts["text"]),
            name="gender",
            position=(x_centre, 600),
            is_numeric=True,
            char_limit=1,
        )
        input_culture = InputBox(
            text=Text("", font=fonts["text"]),
            name="culture",
            position=(x_centre, 700),
            is_numeric=True,
            char_limit=1,
        )

        self.elements.append(title)
        self.elements.append(heading_number)
        self.elements.append(heading_age)
        self.elements.append(heading_gender)
        self.elements.append(heading_culture)
        self.elements.append(info_number)
        self.elements.append(info_age)
        self.elements.append(info_gender)
        self.elements.append(info_culture)

        self.interactables.append(start_button)
        self.interactables.append(input_number)
        self.interactables.append(input_age)
        self.interactables.append(input_gender)
        self.interactables.append(input_culture)

    def key_down(self, key: int) -> None:
        for interactable in self.interactables:
            if interactable.is_active:
                if not isinstance(interactable, InputBox):
                    continue
                interactable.key_down(key)
                return

    def button_down(self, _: int, pos: tuple[int, int]) -> None:
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
            if interactable.name != "start":
                continue
            for box in self.interactables:
                if not isinstance(box, InputBox):
                    continue
                title = box.name
                if box.text.string == "":
                    return
                val = int(box.text.string)
                if title == "age":
                    if val < 18 or val > 120:
                        box.text.string = ""
                        box.background_colour = ERROR_RED
                        return
                elif title == "gender":
                    if val not in (1, 2, 3):
                        box.text.string = ""
                        box.background_colour = ERROR_RED
                        return
                elif title == "culture":
                    if val not in range(1, 10):
                        box.text.string = ""
                        box.background_colour = ERROR_RED
                        return
                self.participant_details[title] = int(box.text.string)
            self.progress = True
            return
