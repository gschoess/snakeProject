#!/usr/bin/python
# ‐*‐ encoding: utf‐8 ‐*‐
import pygame
import pygame_menu
from pygame.constants import USEREVENT

from scene.Game import Game


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
        self.SCREENSIZE = (640, 480)
        self.FPS = 10
        self.window = pygame.display.set_mode(self.SCREENSIZE)
        pygame.display.set_caption("The PySnakeProject")

        # E - Entities
        # Sound
        self.music_mixer = pygame.mixer

        #  Precreate Game Scene
        self.game = Game(self)
        self.current_scene = self.game

        # Clock
        self.clock = pygame.time.Clock()

        # Events
        self.keepGoing = False  # flag for ending main loop

        # Start Game
        self.run_game()

    def run_game(self):
        # A - Action (broken into ALTER steps)
        # A - Assign values to key variables
        self.keepGoing = True

        # L - Set up main loop
        while self.keepGoing:
            # T - Timer to set frame rate
            self.clock.tick(self.FPS)

            # E – Event handling & Prebuilding new scene
            events = pygame.event.get()
            self.current_scene.handle_events(events)
            self.current_scene.prebuild()

            # R - Refresh display
            pygame.display.update()

    # TODO
    def switch_music(self):
        pass
