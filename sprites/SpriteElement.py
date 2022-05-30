#!/usr/bin/python
# ‐*‐ encoding: utf‐8 ‐*‐
import pygame
from pygame.sprite import Sprite


class SpriteElement(pygame.sprite.Sprite):

    def __init__(self, x, y, dir_x, dir_y):
        Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.sound = None

    def update(self):
        self.rect.left += self.dir_x
        self.rect.top += self.dir_y

    def update_dir(self, dir_x, dir_y):
        self.dir_x = dir_x
        self.dir_y = dir_y
