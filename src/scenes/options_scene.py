"""
Defines OptionsScene class.
"""
import pygame

from src.gui.button import Button
from src.gui.checkbox import Checkbox
from src.gui.fonts import fonts
from src.gui.text import Text
from src.scenes.scene import Scene


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
        self.title = Text(
            "Gaze Cueing Experiment", fonts["title"], (x_centre, 200), is_centred=True
        )
        self.button = Button(
            text="Back",
            font=fonts["button"],
            pos=(x_centre, 400),
            is_centred=True,
        )
        self.test_checkbox = Checkbox(25, (x_centre, self.screen.get_height() // 2))

    def display(self) -> None:
        self.button.display(self.screen)
        self.title.display(self.screen)
        self.test_checkbox.display(self.screen)

    def button_down(self, _: int, pos: tuple[int, int]) -> None:
        self.test_checkbox.is_clicked(pos)
        if self.button.is_clicked(pos):
            self.progress = True
