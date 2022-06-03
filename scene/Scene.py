#!/usr/bin/python
# ‐*‐ encoding: utf‐8 ‐*‐
from abc import ABC, abstractmethod
import pygame


class Scene(ABC):

    def __init__(self, scene_dir):
        self.scene_dir = scene_dir
        self.window = scene_dir.window
        self.bg_surface = pygame.Surface(self.scene_dir.screensize)
        self.bg_surface.convert()
        self.bg_surface.fill('white')
        self.sprite_groups = []
        self.font = pygame.font.Font(None, 25)

    @abstractmethod
    def handle_events(self, events):
        pass

    @abstractmethod
    def prebuild(self):
        pass
