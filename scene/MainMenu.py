#!/usr/bin/python
# ‐*‐ encoding: utf‐8 ‐*‐
import pygame
import pygame_menu
from pygame import *
from scene.Scene import Scene


class MainMenu(Scene):

    def __init__(self, scene_dir):
        super().__init__(scene_dir)

        # pygame_menu
        self.mytheme = pygame_menu.themes.THEME_SOLARIZED.copy()
        self.mytheme.title_font = pygame_menu.font.FONT_8BIT

        self.menu = pygame_menu.Menu('Welcome', 400, 400, theme=self.mytheme)
        self.menu.add.text_input('Name :', default='John Doe')
        self.menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=self.scene_dir.set_difficulty())
        self.menu.add.button('Play', self.scene_dir.switch_scene())
        self.menu.add.button('Highscore', self.scene_dir.switch_scene())
        self.menu.add.button('HowTo', self.scene_dir.switch_scene())
        self.menu.add.button('Quit', pygame_menu.events.EXIT)

    #     self.selected_entry = 1
    #     self.rendered_text = []
    #     self.entries = []
    #     self.font = pygame.font.Font(None, 35)
    #     self.headline = self.font.render('Main Menu', True, Color('black'), Color('white'))
    #     self.headline_rect = self.headline.get_rect(center=(self.window.get_width() // 2, 120))
    #     self.rendered_text.append((self.headline, self.headline_rect))
    #     self.render_entries('Play', 'Highscore', 'HowTo', 'Exit')
    #     self.select_entry(1, 2)
    #
    # def render_entries(self, *args):
    #     for i in range(len(args)):
    #         self.entries.append((args[i], 'black', 'white', self.window.get_width() // 2, 170 + i * 30))
    #         self.font = pygame.font.Font(None, 30)
    #         text = self.font.render(args[i], True, Color('black'), Color('white'))  # type(text) = Surface
    #         text_rect = text.get_rect(center=(self.entries[i][3], self.entries[i][4]))
    #         self.rendered_text.append((text, text_rect))
    #
    # def select_entry(self, prev_i, i):
    #     # unselect previous
    #     self.set_entry_background(prev_i, Color('white'))
    #     # select current
    #     self.set_entry_background(i, Color('green'))
    #     self.selected_entry = i
    #
    # def set_entry_background(self, i, bg_color):
    #     text = self.font.render(self.entries[i-1][0], True, self.entries[i-1][1], bg_color)
    #     self.rendered_text[i] = (text, text.get_rect(center=(self.entries[i-1][3], self.entries[i-1][4])))

    def handle_events(self, events):
        for gevent in events:
            if gevent.type == QUIT:
                self.scene_dir.keepGoing = False

            if gevent.type == KEYDOWN:
                #     if gevent.key == K_UP:
                #         if self.selected_entry > 1:
                #             self.select_entry(self.selected_entry - 1, self.selected_entry)
                #
                #     elif gevent.key == K_DOWN:
                #         if self.selected_entry < len(self.entries):
                #             self.select_entry(self.selected_entry + 1, self.selected_entry)

                if gevent.key == K_ESCAPE:
                    self.scene_dir.keepGoing = False

    def prebuild(self):
        # # Background Surfaces
        # self.window.blit(self.bg_surface, (0, 0))
        # # Text
        # # for entry in self.rendered_text:
        # #     self.window.blit(entry[0], entry[1])
        #
        # # Sprites in Spritegroups
        # if self.sprite_groups:
        #     for sprite_group in self.sprite_groups:
        #         pygame.sprite.Group.draw(sprite_group, self.window)
        self.menu.mainloop(self.scene_dir.window)
