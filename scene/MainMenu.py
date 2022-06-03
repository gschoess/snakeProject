#!/usr/bin/python
# ‐*‐ encoding: utf‐8 ‐*‐
import pygame
import pygame_menu
from pygame import *
from scene.Scene import Scene


class MainMenu(Scene):

    def __init__(self, scene_dir):
        super().__init__(scene_dir)

        # pygame_menu
        self.mytheme = pygame_menu.themes.THEME_SOLARIZED.copy()
        self.mytheme.title_font = pygame_menu.font.FONT_8BIT

        self.menu = pygame_menu.Menu('Welcome', 400, 400, theme=self.mytheme)
        self.menu.add.text_input('Name :', default='John Doe')
        self.menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=self.scene_dir.set_difficulty())
        self.menu.add.button('Play', self.scene_dir.switch_scene())
        self.menu.add.button('Highscore', self.scene_dir.switch_scene())
        self.menu.add.button('HowTo', self.scene_dir.switch_scene())
        self.menu.add.button('Quit', pygame_menu.events.EXIT)

    def handle_events(self, events):
        pass

    def prebuild(self):
        pass
