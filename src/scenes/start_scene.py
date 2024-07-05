"""
Defines StartScene class.
"""
import pygame

from src.gui.button import Button
from src.gui.fonts import fonts
from src.gui.text import Text
from src.scenes.scene import Scene


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
        self.title = Text(
            "Gaze Cueing Experiment", fonts["title"], (x_centre, 200), is_centred=True
        )
        self.text = Text(
            (
                "In this experiment you will be responding to letters appearing to the left or right of a central face."
                "\nIf the letter is an L, press the SPACE bar. If the letter is a T, press the H key."
                "\nIt is important that you respond as quickly and accurately as you can."
                "\nOnce the experiment begins, it will take 25 - 30 minutes to complete."
                "\nYou may terminate the experiment at any time by pressing the ESCAPE key."
                "\nPress ENTER when you are ready to begin the experiment."
            ),
            fonts["text"],
            (x_centre, 400),
            is_centred=True,
        )
        self.button = Button(
            text="Options", font=fonts["button"], pos=(x_centre, 800), is_centred=True
        )
        self.options = False

    def button_down(self, _: int, pos: tuple[int, int]) -> None:
        if self.button.is_clicked(pos):
            self.options = True
            self.progress = True

    def display(self) -> None:
        self.button.display(self.screen)
        self.text.display(self.screen)
        self.title.display(self.screen)

    def key_down(self, key: int) -> None:
        if key == pygame.K_RETURN:
            self.progress = True
