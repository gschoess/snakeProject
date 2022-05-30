#!/usr/bin/python
# ‐*‐ encoding: utf‐8 ‐*‐
import pygame

from scene.Game import Game
from scene.Highscore import Highscore
from scene.HowTo import HowTo
from scene.MainMenu import MainMenu


class SceneController:
    """
    Properties:
    - knows the current active scene and music

    Methods:
    - hands over events to current scene
    - switches scenes and music
    - refreshes the current display
    """

    def __init__(self):
        # D - Display configuration
        self.screensize = (640, 480)
        self.display = pygame.display.set_mode(self.screensize)
        pygame.display.set_caption("Python - The Snake Game")

        self.font = pygame.font.Font(None, 25)

        # Sound
        self.music_mixer = pygame.mixer

        # Precreate Scenes
        self.main_menu = MainMenu(self.display)
        self.game = Game(self.display)
        self.highscore = Highscore(self.display)
        self.how_to = HowTo(self.display)

    def switch_scene(self):
        pass

    def hand_over_events_to_current_scene(self):
        pass

    def refresh_current_display(self):
        pass

    def switch_music(self):
        pass
