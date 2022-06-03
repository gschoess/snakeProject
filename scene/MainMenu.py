#!/usr/bin/python
# ‐*‐ encoding: utf‐8 ‐*‐
import pygame
from pygame import *
from scene.Scene import Scene


class MainMenu(Scene):

    def __init__(self, scene_dir):
        super().__init__(scene_dir)
        self.menu_entries = []
        self.font = pygame.font.Font(None, 35)
        self.headline = self.font.render('Main Menu', True, Color('black'), Color('white'))
        self.headline_rect = self.headline.get_rect(center=(self.window.get_width() // 2, 120))
        self.menu_entries.append((self.headline, self.headline_rect))
        self.create_menu_entries('Play', 'Highscore', 'HowTo', 'Exit')

    def create_menu_entries(self, *args):
        for i in range(len(args)):
            self.font = pygame.font.Font(None, 30)
            text = self.font.render(args[i], True, Color('black'), Color('white'))  # type(text) = Surface
            text_rect = text.get_rect(center=(self.window.get_width() // 2, 170 + i * 30))
            self.menu_entries.append((text, text_rect))

    def handle_events(self, events):
        pass

    def prebuild(self):
        # Background Surfaces
        self.window.blit(self.bg_surface, (0, 0))
        # Text
        for entry in self.menu_entries:
            self.window.blit(entry[0], entry[1])

        # Sprites in Spritegroups
        if self.sprite_groups:
            for sprite_group in self.sprite_groups:
                pygame.sprite.Group.draw(sprite_group, self.window)
