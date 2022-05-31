#!/usr/bin/python
# ‐*‐ encoding: utf‐8 ‐*‐
import pygame
from pygame import *
from scene.Scene import Scene


class HowTo(Scene):

    def __init__(self, scene_dir):
        super().__init__(scene_dir)
        self.bg_surface = pygame.Surface(self.scene_dir.screensize)
        self.bg_surface.convert()
        self.bg_surface.fill('white')

    def refresh_display(self):
        pass

    def handle_events(self, events):
        pass

    def unload_scene(self):
        pass

    def load_scene(self):
        pass
