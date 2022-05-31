#!/usr/bin/python
# ‐*‐ encoding: utf‐8 ‐*‐
import pygame
from pygame import *
from scene.Scene import Scene
from sprites.Snake import Snake


class Game(Scene):

    def __init__(self, scene_dir):
        super().__init__(scene_dir)
        self.bg_surface.fill('green')

        # Photo Background
        # self.bg_surface = pygame.image.load("images/bg_lawn_centralPark.jpg")
        # self.bg_surface = pygame.transform.scale(self.bg_surface, self.scene_dir.screensize)

        # Game Entities
        self.snake = Snake()  # vom Typ pygame.sprite.Group
        self.sprite_groups.append(self.snake)

    def handle_events(self, events):

        for game_event in events:
            if game_event.type == pygame.QUIT:
                self.scene_dir.keepGoing = False
            elif game_event.type == MOUSEBUTTONDOWN:
                pass
            elif game_event.type == USEREVENT:
                pass

    def refresh(self):
        # Background Surfaces
        self.window.blit(self.bg_surface, (0, 0))
        text = self.scene_dir.font.render('Hello World', True,
                                          Color('black'), Color('white'))
        self.window.blit(text, (450, 10))

        # Sprites in Spritegroups
        if self.sprite_groups:
            for sprite_group in self.sprite_groups:
                pygame.sprite.Group.update(sprite_group)
                pygame.sprite.Group.draw(sprite_group, self.window)

