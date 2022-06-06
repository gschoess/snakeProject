#!/usr/bin/python
# ‐*‐ encoding: utf‐8 ‐*‐
import pygame
from pygame import *

from director.GameMenuManager import MenuManager
from scene.Scene import Scene
from sprites.FoodElement import FoodElement
from sprites.Snake import Snake


class Game(Scene):

    def __init__(self, scene_dir):
        super().__init__(scene_dir)
        self.text = None
        self.food_sg = None
        self.body_sg = None
        self.head_sg = None
        self.snake = None
        self.bg_surface.fill('green')
        self.el_size = 30
        self.score_surface = None
        self.score = 0

        # Photo Background
        # self.bg_surface = pygame.image.load("images/bg_lawn_centralPark.jpg")
        # self.bg_surface = pygame.transform.scale(self.bg_surface, self.scene_dir.screensize)

        # Menu Manager
        self.mmgr = MenuManager(self)

        # Game Entities
        self.init_game()

    def init_game(self):
        self.sprite_groups.clear()

        self.snake = Snake(self)  # snake head
        self.head_sg = pygame.sprite.GroupSingle()
        self.head_sg.add(self.snake)
        self.body_sg = self.snake.get_body_sprite_group()  # Snake Body
        self.body_sg.add(self.body_sg)
        self.food_sg = pygame.sprite.Group()
        self.create_food()  # initial food

        # Collect all SpriteGroups for .update() with every tick
        # Order determines layer of Scene, last appended SpriteGroup is drawn on top
        self.sprite_groups.append(self.food_sg)
        self.sprite_groups.append(self.body_sg)
        self.sprite_groups.append(self.head_sg)

        # Text
        self.text = self.font.render('lives: ' + str(self.snake.lives), True, Color('black'), Color('white'))
        # Score
        self.score_surface = self.font.render('Score: ' + str(self.score),
                                              False, 'black', 'white')

    def handle_events(self, events):

        if self.mmgr.main_menu.is_enabled():
            self.mmgr.main_menu.update(events)

        else:
            for gevent in events:
                if gevent.type == QUIT:
                    self.scene_dir.keepGoing = False

                if gevent.type == KEYDOWN:
                    if gevent.key == pygame.K_LEFT:
                        if self.snake.dir_x != 1:
                            self.snake.turn(-1, 0)

                    elif gevent.key == K_RIGHT:
                        if self.snake.dir_x != -1:
                            self.snake.turn(1, 0)

                    elif gevent.key == K_UP:
                        if self.snake.dir_y != -1:
                            self.snake.turn(0, -1)

                    elif gevent.key == K_DOWN:
                        if self.snake.dir_y != 1:
                            self.snake.turn(0, 1)

                    elif gevent.key == K_SPACE:
                        self.snake.moving = False if self.snake.moving else True  # ternärer bedingter Operator
                        print("PAUSE - continue with Arrow-Keys or SPACE")

                    elif gevent.key == K_ESCAPE:
                        self.snake.moving = False
                        self.mmgr.main_menu._current = self.mmgr.continue_menu
                        self.mmgr.engine.play_event()
                        self.mmgr.main_menu.enable()

        # set new_pos(x,y) Snake head and set consequences (could stop snake moving)
        if self.snake.moving:
            self.snake.set_new_pos_head()

        # set new rect.top and bottom of all sprites
        if self.snake.moving:
            if self.sprite_groups:
                for sprite_group in self.sprite_groups:
                    pygame.sprite.Group.update(sprite_group)

        # game over
        if self.snake.lives == 0:
            self.snake.lives = "dead"
            # call the init function to update the score
            self.mmgr.main_menu._current = self.mmgr.init_your_score_menu()
            self.mmgr.engine.play_event()
            self.mmgr.main_menu.enable()

    def prebuild(self):
        # Rerender text
        self.text = self.font.render('lives: ' + str(self.snake.lives), True, Color('black'), Color('white'))
        self.score_surface = self.font.render('Score: ' + str(self.score),
                                              False, 'black', 'white')

        # Background Surfaces
        self.window.blit(self.bg_surface, (0, 0))
        self.window.blit(self.text, (450, 10))
        self.window.blit(self.score_surface, (10, 10))

        # Sprites in Spritegroups
        if self.sprite_groups:
            for sprite_group in self.sprite_groups:
                pygame.sprite.Group.draw(sprite_group, self.window)

        if self.mmgr.main_menu.is_enabled():
            self.mmgr.main_menu.draw(self.window)

    def create_food(self):
        random_food_element = FoodElement(self)
        self.food_sg.add(random_food_element)

    def start_game(self):
        self.init_game()
        self.mmgr.engine.play_close_menu()
        self.mmgr.main_menu.disable()

    def set_difficulty(self):
        pass

    def add_score(self):
        self.score += 10
