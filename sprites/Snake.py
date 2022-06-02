#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import pygame.sprite

from sprites.SnakeBodyElement import SnakeBodyElement
from sprites.SpriteElement import SpriteElement


class Snake(SpriteElement):
    def __init__(self, window):
        self.window = window
        self.moving = False  # necessary attribut to disallow start moving against direction when snake at rest
        # TODO alle x,y Tupel in 2D-Vektor packen, standard Tupel mit DOWN, LEFT, RIGHT, UP ersetzen
        self.start_dir_x = 1
        self.start_dir_y = 0
        self.body_el_size = 10
        super().__init__(300, 300, self.start_dir_x, self.start_dir_y, 'media/images/snake_head.png', self.body_el_size,
                         self.body_el_size, 'media/sounds/pain.wav')
        self.spritegroup = pygame.sprite.Group()
        self.spritegroup.add(self)

        # TODO No Hardcode Snake - Automatisiert verzweigte Random Snake mit variabler Länge bei Beginn erzeugen
        # BODY
        self.body_elements = []
        self.body_elements.append(SnakeBodyElement(290, 300, 1, 0, self.body_el_size))
        self.body_elements.append(SnakeBodyElement(280, 300, 1, 0, self.body_el_size))
        self.body_elements.append(SnakeBodyElement(270, 300, 1, 0, self.body_el_size))
        self.body_elements.append(SnakeBodyElement(260, 300, 1, 0, self.body_el_size))

        # Add body elements to sprite group (Snake) for c
        for sprite in self.body_elements:
            self.spritegroup.add(sprite)

    """
    Move the BodyElement to the Place of its Predecessor
    """

    def turn(self, dir_x, dir_y):
        self.set_dir(dir_x, dir_y)
        self.moving = True

    def update(self):
        self.rect.left = self.new_pos_x
        self.rect.top = self.new_pos_y

    def set_new_pos_head(self):
        if self.moving:
            self.new_pos_x += self.dir_x * self.rect.width
            self.new_pos_y += self.dir_y * self.rect.height
            self.handle_out_of_window()
            self.body_follow_head()

    """
    If snake collides with window she returns on the opposite side of the screen.
    """
    def handle_out_of_window(self):
        if self.new_pos_x < 0:
            print("left end of screen")
            self.new_pos_x = self.window.get_rect().width - self.rect.width
        if (self.new_pos_x + self.rect.width) > self.window.get_rect().width:
            print("right end of screen")
            self.new_pos_x = 0
        if self.new_pos_y < 0:
            print("upper end of screen")
            self.new_pos_y = self.window.get_rect().height - self.rect.height
        if (self.new_pos_y + self.rect.height) > self.window.get_rect().height:
            print("lower end of screen")
            self.new_pos_y = 0


    def body_follow_head(self):
        self.body_elements[0].set_new_pos(self.rect.left, self.rect.top)
        for i in range(1, len(self.body_elements)):
            self.body_elements[i].set_new_pos(self.body_elements[i - 1].rect.left, self.body_elements[i - 1].rect.top)


    def get_spritegroup(self):
        return self.spritegroup

    def add_element(self):
        pass

    def grow(self):
        pass

    def detect_collission(self):
        pass
