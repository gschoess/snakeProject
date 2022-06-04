#!/usr/bin/python
# ‐*‐ encoding: utf‐8 ‐*‐
import pygame
import pygame_menu
from pygame import *
from scene.Scene import Scene
from sprites.FoodElement import FoodElement
from sprites.Snake import Snake


class Game(Scene):

    def __init__(self, scene_dir):
        super().__init__(scene_dir)
        self.bg_surface.fill('green')
        self.text = self.font.render('Hello World', True, Color('black'), Color('white'))
        self.el_size = 30
        self.continue_menu = self.init_continue_menu()
        self.continue_menu.disable()
        self.continue_menu.full_reset()

        # Photo Background
        # self.bg_surface = pygame.image.load("images/bg_lawn_centralPark.jpg")
        # self.bg_surface = pygame.transform.scale(self.bg_surface, self.scene_dir.screensize)

        # Game Entities
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

    def handle_events(self, events):

        if self.continue_menu.is_enabled():
            self.continue_menu.update(events)

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
                        self.continue_menu.enable()
                        # self.scene_dir.continue_menu.mainloop(self.window, None, fps_limit=self.scene_dir.FPS)
                        # self.scene_dir.keepGoing = False

        # set new_pos(x,y) Snake head and set consequences (could stop snake moving)
        if self.snake.moving:
            self.snake.set_new_pos_head()

        # set new rect.top and bottom of all sprites
        if self.snake.moving:
            if self.sprite_groups:
                for sprite_group in self.sprite_groups:
                    pygame.sprite.Group.update(sprite_group)

    def prebuild(self):
        # Background Surfaces
        self.window.blit(self.bg_surface, (0, 0))
        self.window.blit(self.text, (450, 10))

        # Sprites in Spritegroups
        if self.sprite_groups:
            for sprite_group in self.sprite_groups:
                pygame.sprite.Group.draw(sprite_group, self.window)

        if self.continue_menu.is_enabled():
            self.continue_menu.draw(self.window)

    def create_food(self):
        random_food_element = FoodElement(self)
        self.food_sg.add(random_food_element)

    def init_continue_menu(self):
        # pygame_menu
        self.continue_menu = pygame_menu.Menu('Continue?', 400, 400, theme=self.scene_dir.mytheme)
        self.continue_menu.add.button('Continue', self.disable_menu)
        # self.continue_menu.add.button('Main Menu', self.scene_dir.main_menu.enable)
        self.continue_menu.add.button('Main Menu', self.back_to_main_menu)
        return self.continue_menu

    def disable_menu(self):
        self.continue_menu.disable()

    def back_to_main_menu(self):
        self.scene_dir.main_menu.enable()
