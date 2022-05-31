#!/usr/bin/python
# ‐*‐ encoding: utf‐8 ‐*‐
import pygame
from pygame.sprite import Sprite


class SpriteElement(pygame.sprite.Sprite):

    def __init__(self, x, y, dir_x, dir_y, image, scale_x, scale_y, sound):
        Sprite.__init__(self)
        self.sound = sound
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (scale_x, scale_y))
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.sound = pygame.mixer.Sound(sound)
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.new_pos_x = x
        self.new_pos_y = y

    def set_dir(self, dir_x, dir_y):
        self.dir_x = dir_x
        self.dir_y = dir_y
