#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import pygame.sprite
from random import randint


class FoodElement(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("media/images/apple.png")
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.sound = pygame.mixer.Sound("media/sounds/apple_bite.ogg")
        self.alive = False

    def create_food(self, screen):
        if not self.alive:
            self.rect.top = randint(0, screen.get_rect().height -
                                    self.rect.height)
            self.rect.top -= self.rect.top % self.rect.height
            self.rect.left = randint(0, screen.get_rect().width -
                                     self.rect.width)
            self.rect.left -= self.rect.left % self.rect.width
            self.alive = True

    def delete_food(self):
        self.sound.play()
        self.alive = False
