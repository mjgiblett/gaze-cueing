"""
Entry point to the experiment. Initiates pygame, fonts, main window, and game loop.
"""

import pygame

from src.services.scene_manager import QuitActionType, SceneManager
from src.services.screen import init_screen
from src.visuals.tools import show_fps


def main(
    controller: SceneManager, screen: pygame.Surface, clock: pygame.time.Clock
) -> QuitActionType:
    """
    Main game loop.
    Parameters
    ----------
    controller: SceneManager
        Processes all pygame events and experiment scenes.
    screen: pygame.Surface
        The main window displaying the experiment.
    clock: pygame.time.Clock
        Regulates the game's framerate.
    Returns
    -------
    QuitActionType
        Program quit or restart.
    """
    action = QuitActionType.CONTINUE
    while action == QuitActionType.CONTINUE:
        screen.fill(BG_GREY)
        action = controller.process_game_events()
        if SHOW_FRAMERATE:
            show_fps(screen, clock, fonts["text"])
        pygame.display.update()
        clock.tick(FRAMERATE)
    return action


if __name__ == "__main__":
    import subprocess
    import sys

    from src.constants import BG_GREY, FRAMERATE, SHOW_FRAMERATE
    from src.visuals import fonts, init_fonts

    pygame.init()
    init_fonts()

    screen = init_screen()

    scene_manager = SceneManager(screen)
    quit_action = main(scene_manager, screen, pygame.time.Clock())
    pygame.quit()

    if quit_action == QuitActionType.RESTART:
        subprocess.Popen([sys.executable, "main.py"]).wait()
