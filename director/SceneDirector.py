#!/usr/bin/python
# ‐*‐ encoding: utf‐8 ‐*‐
import pygame

from scene.Game import Game
from scene.Highscore import Highscore
from scene.HowTo import HowTo
from scene.MainMenu import MainMenu





class SceneDirector:
    """
    Properties:
    - knows the current active scene and music

    Methods:
    - hands over events to current scene
    - switches scenes and music
    - refreshes the current display
    """

    def __init__(self):
        # I - Initialize
        pygame.init()
        # D - Display configuration
        self.screensize = (640, 480)
        self.window = pygame.display.set_mode(self.screensize)
        pygame.display.set_caption("The PySnakeProject")

        # Sound
        self.music_mixer = pygame.mixer

        # Precreate Scenes
        self.main_menu = MainMenu(self)
        self.game = Game(self)
        self.highscore = Highscore(self)
        self.how_to = HowTo(self)

        # TODO: Update Current Scene MAIN MENU!
        self.current_scene = self.main_menu

        # Clock
        self.clock = pygame.time.Clock()

        # Events
        self.keepGoing = False  # flag for ending main loop
        self.events = pygame.event.get()

        # Start Game
        self.run_game()

    def run_game(self):
        # A - Action (broken into ALTER steps)
        # A - Assign values to key variables
        self.keepGoing = True

        # L - Set up main loop
        while self.keepGoing:
            # T - Timer to set frame rate
            self.clock.tick(10)

            # E – Event handling & Prebuilding new scene
            self.events_to_current_scene()

            # R - Refresh display
            refresh_display()

    # TODO
    def load_scene(self):
        pass

    # TODO
    def switch_scene(self):
        pass

    # TODO
    def set_difficulty(self):
        pass

    def events_to_current_scene(self):
        # E – Event handling - get Current
        self.events = pygame.event.get()
        # Handover to current scene
        self.current_scene.handle_events(self.events)
        # prebuild new scene
        self.current_scene.prebuild()

    # TODO
    def switch_music(self):
        pass


# STATIC methods
def refresh_display():
    pygame.display.update()
    # pygame.display.flip()  ?? Notwendig
