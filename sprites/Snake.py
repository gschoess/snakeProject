#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from typing import cast
import pygame.sprite
from sprites.FoodElement import FoodElement
from sprites.PowerFoodElement import PowerFoodElement
from sprites.MoleHole import MoleHole
from sprites.SnakeBodyElement import SnakeBodyElement
from sprites.SpriteElement import SpriteElement


def signum(number):
    if number < 0:
        return -1
    else:
        return 1


class Snake(SpriteElement):

    def __init__(self, game):
        self.game = game
        self.window = self.game.window
        self.lives = 2
        self.moving = False  # necessary attribut to disallow start moving against direction when snake at rest
        # TODO alle x,y Tupel in 2D-Vektor packen, standard Tupel mit DOWN, LEFT, RIGHT, UP ersetzen
        self.start_dir_x = 1
        self.start_dir_y = 0
        self.el_size = self.game.el_size
        super().__init__(320, 320, self.start_dir_x, self.start_dir_y, 'media/images/snake_head.png', self.el_size,
                         self.el_size, 'media/sounds/pain1.wav')

        # TODO No Hardcode Snake - Automatisiert verzweigte Random Snake mit variabler Länge bei Beginn erzeugen

        self.body_element_list = []
        self.body_element_list.append(SnakeBodyElement(280, 320, 1, 0, self.el_size, self.game))
        self.body_element_list.append(SnakeBodyElement(240, 320, 1, 0, self.el_size, self.game))
        self.body_element_list.append(SnakeBodyElement(200, 320, 1, 0, self.el_size, self.game))
        self.last_bel = SnakeBodyElement(160, 320, 1, 0, self.el_size, self.game)
        self.body_element_list.append(self.last_bel)

        # BODY - sprite group - for use with pygame.sprite.Group methods
        self.body_sprite_group = pygame.sprite.Group()
        for i in range(len(self.body_element_list)):
            self.body_sprite_group.add(self.body_element_list[i])
            # print("index:", i, ": = ID", self.body_element_list[i].id)

        # for j in range(len(self.get_body_elements())):
        #     print("index:", j, ": = ID", self.get_body_elements()[j].id)

        self.last_bel_sg = pygame.sprite.GroupSingle()
        self.last_bel_sg.add(self.last_bel)

        # MOVING UNDERGROUND
        self.head_underground = False
        self.entered_mole_hole = None
        self.exit_mole_hole = None

    """
    Move the BodyElement to the Place of its Predecessor
    """

    def turn(self, new_dir_x, new_dir_y):
        self.set_new_dir(new_dir_x, new_dir_y)
        self.moving = True

    def set_new_pos_head(self):
        if self.moving:
            if self.head_underground:
                self.moving_underground()
            else:
                self.new_pos_x += self.new_dir_x * self.rect.width
                self.new_pos_y += self.new_dir_y * self.rect.height
            self.handle_out_of_window()
            self.body_follow_head()

    def update(self):
        self.update_position()
        self.update_image_rotation()
        self.handle_collision()

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

    """
    Every SnakeElement takes the properties of his predecessor while moving forward
    """

    def body_follow_head(self):
        bel_list = self.get_body_elements()
        bel_list[0].set_new_pos(self.rect.left, self.rect.top)
        # bel_list[0].set_new_image_alpha(self.image.get_alpha())
        for i in range(1, len(bel_list)):
            # print("index:", i, ": = ID", self.body_element_list[i].id)
            bel_list[i].set_new_pos(bel_list[i - 1].rect.left, bel_list[i - 1].rect.top)
            # bel_list[i].set_new_image_alpha(bel_list[i-1].image.get_alpha())
            # input("Press Enter to continue...")

    def moving_underground(self):
        diff_x = self.exit_mole_hole.rect.left - self.rect.left
        diff_y = self.exit_mole_hole.rect.top - self.rect.top
        dir_x = signum(diff_x)
        dir_y = signum(diff_y)

        if diff_x != 0:
            self.set_new_dir(dir_x, 0)
            self.new_pos_x += dir_x * self.el_size
            diff_x += self.dir_x * self.el_size

        if diff_x == 0 and diff_y != 0:
            self.set_new_dir(0, dir_y)
            self.new_pos_y += dir_y * self.el_size
            diff_y += self.dir_y * self.el_size

    """
    spritecollide() refers to rect.top and rect.left position after update()
    """

    def handle_collision(self):

        # BODY ELEMENTS HANDLE THEMSELF
        for i in range(len(self.body_element_list)):
            self.body_element_list[i].handle_collision()

        # LAST BODY ELEMENT ENTER OR EXIT MOLE HOLE - The last one closes the Hole
        if pygame.sprite.spritecollide(self.last_bel, self.game.mole_hole_sg, True):
            print("Last Element closed the hole")
            if not self.game.mole_hole_sg.sprites():
                self.game.create_mole_hole_couple()

        # EXIT Mole Hole
        if self.head_underground:
            if pygame.sprite.spritecollide(self, self.game.mole_hole_sg, False):
                print("SnakeHead is overground again")
                self.go_overground()

        #  If Overground eat and collide with self
        else:
            # ENTER MOLE HOLE
            mole_hole_list = pygame.sprite.spritecollide(self, self.game.mole_hole_sg, False)
            if mole_hole_list:
                self.entered_mole_hole = cast(MoleHole, mole_hole_list[0])
                self.entered_mole_hole.play_sound()
                self.exit_mole_hole = self.entered_mole_hole.connected_hole
                self.go_underground()

            # FOOD
            food_collision_sprite_list = pygame.sprite.spritecollide(self, self.game.food_sg, True)
            if food_collision_sprite_list:
                if type(food_collision_sprite_list[0]).__name__ == 'PowerFoodElement':
                    food_element = cast(PowerFoodElement,
                                        food_collision_sprite_list[0])
                    self.game.increase_speed()
                else:
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

    def go_underground(self):
        self.image.set_alpha(100)
        print("The SnakeHead is underground")
        self.head_underground = True

    def go_overground(self):
        self.image.set_alpha(255)
        print("The SnakeHead is back overground")
        self.head_underground = False

    def grow(self):
        new_bel = SnakeBodyElement(self.last_bel.rect.x, self.last_bel.rect.y, self.last_bel.dir_x, self.last_bel.dir_y,
                                   self.el_size, self.game)
        self.body_sprite_group.add(new_bel)
        self.body_element_list.append(new_bel)
        self.last_bel = new_bel

    def get_body_elements(self):
        return cast([SnakeBodyElement], self.body_sprite_group.sprites())

    def get_body_sprite_group(self):
        return self.body_sprite_group
