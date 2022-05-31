#!/usr/bin/python
# ‐*‐ encoding: utf‐8 ‐*‐
from abc import ABC, abstractmethod


class Scene(ABC):

    def __init__(self, scene_dir):
        self.scene_dir = scene_dir
        self.display = scene_dir.display
        self.bg_surface = None
        self.sprite_groups = []

    @abstractmethod
    def load_scene(self):
        pass

    @abstractmethod
    def unload_scene(self):
        pass

    @abstractmethod
    def handle_events(self, events):
        pass

    @abstractmethod
    def refresh_display(self):
        pass
