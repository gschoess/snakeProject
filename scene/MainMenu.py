#!/usr/bin/python
# ‐*‐ encoding: utf‐8 ‐*‐
import pygame
from pygame import *
from scene.Scene import Scene


class MainMenu(Scene):

    def __init__(self, scene_dir):
        super().__init__(scene_dir)

    def handle_events(self, events):
        pass

    def prebuild(self):
        pass


