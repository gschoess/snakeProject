#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from typing import cast
import pygame.sprite
from sprites.FoodElement import FoodElement
from sprites.SnakeBodyElement import SnakeBodyElement
from sprites.SpriteElement import SpriteElement


class Snake(SpriteElement):

    def __init__(self, game):
        self.game = game
        self.window = self.game.window
        self.lives = 1
        self.moving = False  # necessary attribut to disallow start moving against direction when snake at rest
        # TODO alle x,y Tupel in 2D-Vektor packen, standard Tupel mit DOWN, LEFT, RIGHT, UP ersetzen
        self.start_dir_x = 1
        self.start_dir_y = 0
        self.el_size = self.game.el_size
        super().__init__(300, 300, self.start_dir_x, self.start_dir_y, 'media/images/snake_head.png', self.el_size,
                         self.el_size, 'media/sounds/pain.wav')

        # TODO No Hardcode Snake - Automatisiert verzweigte Random Snake mit variabler Länge bei Beginn erzeugen
        # BODY - sprite group - for use with pygame.sprite.Group methods
        self.body_sprite_group = pygame.sprite.Group()
        self.body_sprite_group.add(SnakeBodyElement(270, 300, 1, 0, self.el_size))
        self.body_sprite_group.add(SnakeBodyElement(240, 300, 1, 0, self.el_size))
        self.body_sprite_group.add(SnakeBodyElement(210, 300, 1, 0, self.el_size))
        self.body_sprite_group.add(SnakeBodyElement(180, 300, 1, 0, self.el_size))

    """
    Move the BodyElement to the Place of its Predecessor
    """
    def turn(self, new_dir_x, new_dir_y):
        self.set_new_dir(new_dir_x, new_dir_y)
        self.moving = True

    def set_new_pos_head(self):
        if self.moving:
            self.new_pos_x += self.new_dir_x * self.rect.width
            self.new_pos_y += self.new_dir_y * self.rect.height
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
        bel_list = self.get_body_elements()
        bel_list[0].set_new_pos(self.rect.left, self.rect.top)
        for i in range(1, len(bel_list)):
            bel_list[i].set_new_pos(bel_list[i - 1].rect.left, bel_list[i - 1].rect.top)

    def update(self):
        self.rect.left = self.new_pos_x
        self.rect.top = self.new_pos_y
        self.update_image_rotation()
        self.handle_collision()

    def handle_collision(self):
        # FOOD
        food_collision_sprite_list = pygame.sprite.spritecollide(self, self.game.food_sg, True)
        if food_collision_sprite_list:
            food_element = cast(FoodElement, food_collision_sprite_list[0])
            food_element.play_sound()
            print("The snake ate an apple and grew.")
            self.grow()
            self.game.create_food()
            self.game.add_score()

        # LOSE LIFE
        if pygame.sprite.spritecollide(self, self.body_sprite_group, False):
            print("Collision with self. You lost one life.")
            print("PAUSE - press SPACE to continue")
            self.play_sound()
            self.moving = False
            if self.lives > 0:
                self.lives -= 1

    def grow(self):
        bel_list = self.get_body_elements()
        last_bel = bel_list[len(bel_list)-1]
        new_bel = SnakeBodyElement(last_bel.rect.x, last_bel.rect.y, last_bel.dir_x, last_bel.dir_y, self.el_size)
        self.body_sprite_group.add(new_bel)

    def get_body_elements(self):
        return cast([SnakeBodyElement], self.body_sprite_group.sprites())

    def get_body_sprite_group(self):
        return self.body_sprite_group
