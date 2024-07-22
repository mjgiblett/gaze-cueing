"""
Defines OptionsScene class.
"""
import pygame

from src.constants import BG_GREY
from src.gui.button import Button
from src.gui.checkbox import Checkbox
from src.scenes.scene import Scene
from src.visuals.fonts import fonts
from src.visuals.text import Text


class OptionsScene(Scene):
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
        back_button = Button(
            text=Text("Back", fonts["button"], text_colour=BG_GREY),
            position=(x_centre, 400),
            name="back",
        )

        checkbox = Checkbox((x_centre, self.screen.get_height() // 2), (25, 25))

        self.elements.append(title)

        self.interactables.append(back_button)
        self.interactables.append(checkbox)

    def button_down(self, _: int, pos: tuple[int, int]) -> None:
        for interactable in self.interactables:
            if not interactable.is_clicked(pos):
                continue
            if interactable.name == "back":
                self.progress = True
