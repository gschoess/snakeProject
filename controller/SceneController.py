#!/usr/bin/python
# ‐*‐ encoding: utf‐8 ‐*‐
import pygame

import scene.MainMenu
import scene.Game
import scene.Highscore
import scene.HowTo


class SceneController:
    """
    Knows the current active Scene -> can call .update() method of Scene
    """

    def __init__(self):
        # D - Display configuration
        self.screensize = (640, 480)
        self.screen = pygame.display.set_mode(self.screensize)
        pygame.display.set_caption("Python - The Snake Game")

        self.font = pygame.font.Font(None, 25)
