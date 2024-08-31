"""
Defines StartScene class.
"""
import pygame

from src.constants import BG_GREY
from src.gui import Button
from src.scenes.scene import Scene
from src.visuals import MultilineText, Text, fonts


class StartScene(Scene):
    """
    The initial scene of the experiment. Displays instructions and begins experiment.
    Attributes
    ----------
    screen: pygame.Surface
        The main window displaying the experiment.
    Methods
    -------
    display()
        Display the scene on the main window.
    update_state()
        Communicates to the SceneManager when to trasition from this scene to the next.
    key_down()
        Handles key down events.
    """

    def __init__(self, screen: pygame.Surface) -> None:
        super().__init__(screen)
        x_centre = self.screen.get_width() // 2
        title = Text("Gaze Cueing Experiment", fonts["title"], (x_centre, 200))
        instructions = MultilineText(
            (
                "In this experiment you will be responding to letters appearing to the left or right of a central face."
                "\nIf the letter is an L, press the SPACE bar. If the letter is a T, press the H key."
                "\nIt is important that you respond as quickly and accurately as you can."
                "\nOnce the experiment begins, it will take 25 - 30 minutes to complete."
                "\nYou may terminate the experiment at any time by pressing the ESCAPE key."
                "\nClick the 'Next' button when you are ready to progress."
            ),
            fonts["text"],
            (x_centre, 400),
        )
        next_button = Button(
            Text("Next", font=fonts["button"], text_colour=BG_GREY),
            position=(x_centre, 700),
            name="next",
        )
        self.elements.append(title)
        self.elements.append(instructions)

        self.interactables.append(next_button)

    def button_down(self, _: int, pos: tuple[int, int]) -> None:
        for interactable in self.interactables:
            if not interactable.is_clicked(pos):
                continue
            if interactable.name == "next":
                self.progress = True
