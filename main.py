"""
Entry point to the experiment. Initiates pygame, fonts, main window, and game loop. 
"""
import pygame

from src.services.scene_manager import QuitActionType, SceneManager
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

    from src.components.stimuli import init_stimuli
    from src.components.targets import init_targets
    from src.constants import (
        BG_GREY,
        DISPLAY_HEIGHT,
        DISPLAY_WIDTH,
        FRAMERATE,
        IS_FULLSCREEN,
        SHOW_FRAMERATE,
    )
    from src.visuals import fonts, init_fonts

    pygame.init()
    init_fonts()

    flags = 0
    size = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
    if IS_FULLSCREEN:
        size = (0, 0)
        flags = pygame.FULLSCREEN
    pygame.display.set_caption("Gaze Cueing Experiment")
    screen = pygame.display.set_mode(size, flags)

    init_stimuli(screen)
    init_targets(screen)

    scene_manager = SceneManager(screen)
    quit_action = main(scene_manager, screen, pygame.time.Clock())
    pygame.quit()

    if quit_action == QuitActionType.RESTART:
        subprocess.Popen([sys.executable, "main.py"]).wait()
