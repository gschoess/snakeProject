#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import pygame
from pygame.sprite import *


class Snake(pygame.sprite.Sprite):
    def __init__(self, counter):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/snake_tile.png')
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect()
        self.rect.left = 300    # Startposition
        self.rect.top = 300
        self.dir_x = 0
        self.dir_y = 0

    def update(self):
        self.rect.left += self.dir_x
        self.rect.top += self.dir_y

