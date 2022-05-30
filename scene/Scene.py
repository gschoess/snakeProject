#!/usr/bin/python
# ‐*‐ encoding: utf‐8 ‐*‐
from abc import ABC, abstractmethod


class Scene(ABC):

    def __init__(self, display):
        self.display = display
        self.bg_surface = None
        self.sprite_groups = None

    @abstractmethod
    def load_scene(self):
        pass

    @abstractmethod
    def unload_scene(self):
        pass

    @abstractmethod
    def handle_events(self):
        pass

    @abstractmethod
    def refresh_display(self):
        pass
