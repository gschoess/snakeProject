#!/usr/bin/python
# ‐*‐ encoding: utf‐8 ‐*‐
import pygame_menu
from scene.Scene import Scene


class HowTo(Scene):

    def __init__(self, scene_dir):
        super().__init__(scene_dir)

        # pygame_menu
        self.mytheme = pygame_menu.themes.THEME_SOLARIZED.copy()
        self.mytheme.title_font = pygame_menu.font.FONT_8BIT

        self.menu = pygame_menu.Menu('How To Play', 400, 400, theme=self.mytheme)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)


    def handle_events(self, events):
        pass

    def prebuild(self):
        pass
