#!/usr/bin/python
# ‐*‐ encoding: utf‐8 ‐*‐
import pygame
from pygame import *
from scene.Scene import Scene
from sprites.FoodElement import FoodElement
from sprites.Snake import Snake


class Game(Scene):

    def __init__(self, scene_dir):
        super().__init__(scene_dir)
        self.bg_surface.fill('green')

        # Photo Background
        # self.bg_surface = pygame.image.load("images/bg_lawn_centralPark.jpg")
        # self.bg_surface = pygame.transform.scale(self.bg_surface, self.scene_dir.screensize)

        # Game Entities
        self.snake = Snake(self.window)
        self.snake_sg = self.snake.get_spritegroup()  # Snake Body

        self.food_sg = pygame.sprite.Group()
        self.apple = FoodElement(self.window)
        self.food_sg.add(self.apple)

        # Collect all SpriteGroups for .update() with every tick
        self.sprite_groups.append(self.snake_sg)
        self.sprite_groups.append(self.food_sg)

    def handle_events(self, events):

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

                elif gevent.key == K_ESCAPE:
                    self.scene_dir.keepGoing = False

        # Calculate new pos Snake head
        if self.snake.moving:
            self.snake.set_new_pos_head()

        # Sprites in Spritegroups neu berechnen
        if self.sprite_groups:
            for sprite_group in self.sprite_groups:
                pygame.sprite.Group.update(sprite_group)

    def prebuild(self):
        # Background Surfaces
        self.window.blit(self.bg_surface, (0, 0))
        text = self.scene_dir.font.render('Hello World', True,
                                          Color('black'), Color('white'))
        self.window.blit(text, (450, 10))

        # Sprites in Spritegroups
        if self.sprite_groups:
            for sprite_group in self.sprite_groups:
                pygame.sprite.Group.draw(sprite_group, self.window)
