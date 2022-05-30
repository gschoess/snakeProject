#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import pygame
from pygame.sprite import *


class Snake(pygame.sprite.Sprite):
    def __init__(self, counter):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/snake_tile.png')
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.sound = pygame.mixer.Sound("sound/pain.wav")
        self.rect = self.image.get_rect()
        self.rect.left = 300 - counter * 10
        self.rect.top = 240
        self.dir_x = 0
        self.dir_y = 0

    def update(self):
        self.rect.left += self.dir_x
        self.rect.top += self.dir_y


class Shovel(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("img/schaufel.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.midleft = mouse.get_pos()

    def update(self):
        self.rect.midleft = mouse.get_pos()


class Mole(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("img/mole.png")
        self.image_orig = self.image
        self.rect = self.image.get_rect()
        self.sound = pygame.mixer.Sound("sound/pain.wav")
        self.rect.left = random.randint(0, 600)
        pos_y = random.randint(300, 440)
        scale_mole = (140 - (440 - pos_y))
        self.image = pygame.transform.scale(self.image_orig, (scale_mole, scale_mole))
        self.rect.top = pos_y

    def flee(self):
        self.rect.left = random.randint(0, 600)
        pos_y = random.randint(300, 440)
        scale_mole = (140 - (440 - pos_y))
        self.image = pygame.transform.scale(self.image_orig, (scale_mole, scale_mole))
        self.rect.top = pos_y

    def cry(self):
        self.sound.play()

    def hit(self, pos):
        return self.rect.collidepoint(pos)
