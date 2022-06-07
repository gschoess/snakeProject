#!/usr/bin/python
# ‐*‐ encoding: utf‐8 ‐*‐
from random import randint

import pygame
from pygame.sprite import Sprite


class SpriteElement(pygame.sprite.Sprite):

    def __init__(self, x, y, dir_x, dir_y, image, width, height, sound):
        Sprite.__init__(self)
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.sound = sound
        self.image = pygame.image.load(image)
        self.image = self.image.convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.sound = pygame.mixer.Sound(sound)
        self.new_pos_x = x
        self.new_pos_y = y
        self.new_dir_x = dir_x
        self.new_dir_y = dir_y

    def set_new_dir(self, new_dir_x, new_dir_y):
        self.new_dir_x = new_dir_x
        self.new_dir_y = new_dir_y

    def set_to_random_pos(self, surface):
        # set to random position on screen
        self.rect.top = randint(0, surface.get_rect().height - self.rect.height)
        self.rect.top -= self.rect.top % self.rect.height
        self.rect.left = randint(0, surface.get_rect().width - self.rect.width)
        self.rect.left -= self.rect.left % self.rect.width

    def update_position(self):
        self.rect.left = self.new_pos_x
        self.rect.top = self.new_pos_y

    def play_sound(self):
        self.sound.play()

    def update_image_rotation(self):
        if (self.dir_x == 1 and self.new_dir_y == 1) \
                or (self.dir_y == 1 and self.new_dir_x == -1) \
                or (self.dir_x == -1 and self.new_dir_y == -1) \
                or (self.dir_y == -1 and self.new_dir_x == 1):
            self.image = pygame.transform.rotate(self.image, -90)   # rotation angle must be counter-clockwise!
        elif self.dir_x == -self.new_dir_x and self.dir_y == -self.new_dir_y:  # for virtual going against direction underground
            self.image = pygame.transform.rotate(self.image, 180)
        elif self.dir_x == self.new_dir_x and self.dir_y == self.new_dir_y:
            pass  # start or straight on no turning needed
        else:
            self.image = pygame.transform.rotate(self.image, 90)

        # prevent endless rotation
        self.dir_x = self.new_dir_x
        self.dir_y = self.new_dir_y
