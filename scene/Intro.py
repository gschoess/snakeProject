#!/usr/bin/python
# ‐*‐ encoding: utf‐8 ‐*‐
from random import randint

import pygame
import pygame_menu.font
from pygame.constants import *

from scene.Game import Game
from scene.Scene import Scene


class Intro(Scene):

    def __init__(self, scene_dir, game):
        super().__init__(scene_dir)
        self.game = game
        self.game.bg_surface.fill('white')
        # self.game.init_game()
        # self.game.mmgr.main_menu.disable()
        self.game.snake.immortal = True
        self.random_event_timer = randint(2, 6)
        self.animation_timer = 10
        self.game.snake.moving = True
        # Logo Font

        self.logo_font_height = 10
        self.logo_visibility = 0
        self.logo_font = pygame.font.Font(pygame_menu.font.FONT_8BIT, 1)
        self.logo_surface = self.logo_font.render('SNAKE', False,
                                                  'black', 'white')
        self.logo_surface_rect = self.logo_surface.get_rect(
            center=(self.scene_dir.SCREENSIZE[0]/2, 200))
        self.logo_surface.set_alpha(self.logo_visibility)

        self.logo_sub_font = pygame.font.Font(pygame_menu.font.FONT_8BIT,
                                              int(self.logo_font_height/4))
        self.logo_sub_surface = self.logo_font.render('The Mole Hole Edition',
                                                      False, 'black', 'white')
        self.logo_sub_surface_rect = self.logo_surface.get_rect(
            center=(self.scene_dir.SCREENSIZE[0]/2, 400))
        self.logo_sub_surface.set_alpha(self.logo_visibility)

        self.auto_events = \
            [pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT),
             pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT),
             pygame.event.Event(pygame.KEYDOWN, key=pygame.K_DOWN),
             pygame.event.Event(pygame.KEYDOWN, key=pygame.K_UP)]

    def handle_events(self, events):

        # Start Game on Enter
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_RETURN or event.key == K_ESCAPE:
                    self.game.bg_surface.fill('green')
                    self.scene_dir.start_menu()

        self.game.handle_events(events)

        self.random_event_timer -= 1
        if self.random_event_timer == 0:
            # Auto Move
            rand_event = self.auto_events[randint(0, 3)]
            pygame.event.post(rand_event)
            self.random_event_timer = randint(2, 6)

    def prebuild(self):
        self.game.prebuild()
        self.animation_timer -= 1

        if self.logo_font_height < 100:
            # Rerender logo
            if self.animation_timer == 0:
                # Game Title Logo appearing
                self.logo_visibility += 5
                self.logo_font_height += 1

                self.logo_font = pygame.font.Font(pygame_menu.font.FONT_8BIT,
                                                  self.logo_font_height)
                self.logo_surface = self.logo_font.render('SNAKE', False,
                                                          'black', 'white')
                # background transparency
                self.logo_surface.set_colorkey(pygame.Color("white"))

                self.logo_surface_rect = \
                    self.logo_surface.get_rect(
                        center=(self.scene_dir.SCREENSIZE[0]/2, 200))
                self.logo_surface.set_alpha(self.logo_visibility)

                self.logo_sub_font = \
                    pygame.font.Font(pygame_menu.font.FONT_8BIT,
                                     int(self.logo_font_height/6))
                self.logo_sub_surface = \
                    self.logo_sub_font.render('The Mole Hole Edition',
                                              False, 'black', 'white')

                # background transparency
                self.logo_sub_surface.set_colorkey(pygame.Color("white"))

                self.logo_sub_surface_rect = \
                    self.logo_sub_surface.get_rect(
                        center=(self.scene_dir.SCREENSIZE[0]/2, 400))
                self.logo_sub_surface.set_alpha(self.logo_visibility)

                self.animation_timer = 1

        # Blit Logo
        self.window.blit(self.logo_surface, self.logo_surface_rect)
        self.window.blit(self.logo_sub_surface, self.logo_sub_surface_rect)
