#!/usr/bin/python
# ‐*‐ encoding: utf‐8 ‐*‐
import pygame
from pygame import *
from scene.Scene import Scene


class Highscore(Scene):

    def __init__(self, scene_dir):
        super().__init__(scene_dir)
        self.font = pygame.font.Font(None, 35)
        self.text = self.font.render('Highscore', True, Color('black'), Color('white'))
        self.text_rect = self.text.get_rect(center=(self.window.get_width()//2, 100))

    def handle_events(self, events):
        pass

    def prebuild(self):
        # Background Surfaces
        self.window.blit(self.bg_surface, (0, 0))
        self.window.blit(self.text, self.text_rect)

        # Sprites in Spritegroups
        if self.sprite_groups:
            for sprite_group in self.sprite_groups:
                pygame.sprite.Group.draw(sprite_group, self.window)

    def create_highscore_entries(self):
        for i in range(5):
            self.font = pygame.font.Font(None, 30)
            self.text = self.font.render(str(i) + '. Hubert', True, Color('black'), Color('white'))
            self.text_rect = self.text.get_rect(center=(self.window.get_width()//2, 110 + i * 10))
