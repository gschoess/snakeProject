#!/usr/bin/python
# ‐*‐ encoding: utf‐8 ‐*‐
import pygame
from pygame import *
import random
from director.GameMenuManager import MenuManager
from scene.Scene import Scene
from sprites.FoodElement import FoodElement
from sprites.PowerFoodElement import PowerFoodElement
from sprites.MoleHole import MoleHole
from sprites.Snake import Snake


class Game(Scene):

    def __init__(self, scene_dir):
        super().__init__(scene_dir)
        self.auto_mode = True
        self.hard_mode = True
        self.text = None
        self.lives_surface = None
        self.score_surface = None
        self.mh2 = None
        self.mh1 = None
        self.mole_hole_sg = None
        self.food_sg = None
        self.body_sg = None
        self.head_sg = None
        self.snake = None
        self.bg_surface.fill('green')
        self.el_size = 40

        self.score = 0
        self.speed_up = False

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
        self.food_sg = pygame.sprite.GroupSingle()
        self.mole_hole_sg = pygame.sprite.Group()
        self.create_food()  # initial food
        self.create_mole_hole_couple()

        # Collect all SpriteGroups for .update() with every tick
        # Order determines layer of Scene,
        # last appended SpriteGroup is drawn on top
        self.sprite_groups.append(self.mole_hole_sg)
        self.sprite_groups.append(self.food_sg)
        self.sprite_groups.append(self.body_sg)
        self.sprite_groups.append(self.head_sg)

        # Menu Manager
        self.mmgr.main_menu.disable()

        # Text
        self.text = self.font.render('lives: ' + str(self.snake.lives), True,
                                     Color('black'), Color('white'))
        # Score
        self.score = 0
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
                    if gevent.key == K_LEFT:
                        if self.snake.dir_x != 1:
                            self.snake.turn(-1, 0)

                    elif gevent.key == K_RIGHT:
                        if self.snake.dir_x != -1:
                            self.snake.turn(1, 0)

                    elif gevent.key == K_UP:
                        if self.snake.dir_y != 1:
                            self.snake.turn(0, -1)

                    elif gevent.key == K_DOWN:
                        if self.snake.dir_y != -1:
                            self.snake.turn(0, 1)

                    elif gevent.key == K_SPACE:
                        self.snake.moving = False if self.snake.moving \
                            else True  # ternärer bedingter Operator
                        print("PAUSE - continue with Arrow-Keys or SPACE")

                    elif gevent.key == K_ESCAPE:
                        if not self.auto_mode:  # Different ESC Action in Intro
                            self.snake.moving = False
                            self.mmgr.main_menu._current = \
                                self.mmgr.continue_menu
                            self.mmgr.engine.play_event()
                            self.mmgr.main_menu.enable()

        # set new_pos(x,y) Snake head and set consequences
        # (could stop snake moving)
        if self.snake.moving:
            self.snake.set_new_pos_head()

        # set new rect.top and bottom of all sprites
        if self.snake.moving:
            if self.sprite_groups:
                for sprite_group in self.sprite_groups:
                    pygame.sprite.Group.update(sprite_group)

        # game over
        if self.snake.lives == 0 and not self.snake.immortal:
            self.snake.lives = "-"
            # call the init function to update the score
            self.mmgr.main_menu._current = self.mmgr.init_end_menu()
            self.mmgr.engine.play_event()
            self.mmgr.main_menu.enable()

    def prebuild(self):
        # Rerender text
        self.lives_surface = self.font.render('lives: ' +
                                              str(self.snake.lives), True,
                                              'black', 'white')
        self.score_surface = self.font.render('Score: ' +
                                              str(self.score), False,
                                              'black', 'white')

        # Background Surfaces
        self.window.blit(self.bg_surface, (0, 0))
        self.window.blit(self.lives_surface, (570, 10))
        self.window.blit(self.score_surface, (10, 10))

        # Sprites in Spritegroups
        if self.sprite_groups:
            for sprite_group in self.sprite_groups:
                pygame.sprite.Group.draw(sprite_group, self.window)

        if self.mmgr.main_menu.is_enabled():
            self.mmgr.main_menu.draw(self.window)

    def create_food(self):
        if self.speed_up or not self.hard_mode:
            self.food_sg.add(FoodElement(self))
        else:
            if random.random() < 0.8:
                apple = FoodElement(self)
                self.food_sg.add(apple)
            else:
                banana = PowerFoodElement(self)
                self.food_sg.add(banana)
                banana.time = pygame.time.get_ticks()

        if pygame.sprite.groupcollide(self.food_sg, self.head_sg, True,
                                      False) or \
           pygame.sprite.groupcollide(self.food_sg, self.body_sg, True,
                                      False) or \
           pygame.sprite.groupcollide(self.food_sg, self.mole_hole_sg,
                                      True, False):
            self.create_food()

    def create_mole_hole_couple(self):
        if not self.mole_hole_sg.sprites() and self.hard_mode:
            self.mh1 = MoleHole(self)
            self.mh2 = MoleHole(self)
            self.mh1.set_connected_hole(self.mh2)
            self.mh2.set_connected_hole(self.mh1)
            self.mole_hole_sg.add(self.mh1)
            self.mole_hole_sg.add(self.mh2)

    def start_game(self):
        self.init_game()
        self.mmgr.engine.play_close_menu()
        self.mmgr.main_menu.disable()
        self.auto_mode = False

    def set_difficulty(self, _, index):
        if index == 1:
            self.hard_mode = True
        else:
            self.hard_mode = False

    def add_score(self):
        if self.speed_up:
            self.score += 20
        else:
            self.score += 10

    def increase_speed(self):
        self.speed_up = True

    def decrease_speed(self):
        self.speed_up = False

    def check_highscore(self, db):
        return True if self.score > db.get_tenth_highscore() else False
