#!/usr/bin/python
# ‐*‐ encoding: utf‐8 ‐*‐
import pygame
import pygame_menu
from pygame import *

from scene.Scene import Scene
from sprites.FoodElement import FoodElement
from sprites.Snake import Snake

# Custom Event to get back to Main Menu from Highscore
BACKTOMAIN = USEREVENT + 1
back_to_main_event = pygame.event.Event(BACKTOMAIN, message="Return to main Menu!")


# STATIC methods
def init_my_theme():
    mytheme = pygame_menu.themes.THEME_SOLARIZED.copy()
    mytheme.title_font = pygame_menu.font.FONT_8BIT
    return mytheme


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

        # Photo Background
        # self.bg_surface = pygame.image.load("images/bg_lawn_centralPark.jpg")
        # self.bg_surface = pygame.transform.scale(self.bg_surface, self.scene_dir.screensize)

        # Menus  !!! Order important (From leaves to root) for initializing, references not updated after initializing the menu !!!
        self.mytheme = init_my_theme()
        self.continue_menu = self.init_continue_menu()
        self.continue_menu.disable()
        self.continue_menu.full_reset()

        # Create menu objects ! Order important (from root to top), initialized menus can not be updated after linking
        self.how_to_menu = self.init_how_to_menu()
        self.highscore_menu = self.init_highscore_menu()
        self.main_menu = self.init_main_menu()

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

    def handle_events(self, events):

        if self.main_menu.is_enabled():
            self.main_menu.update(events)

        else:
            print("events are handled")
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
                        self.main_menu._current = self.continue_menu
                        self.main_menu.enable()

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
            self.main_menu._current = self.highscore_menu

            self.main_menu.enable()
            # self.activate_menu(self.highscore_menu)

    def prebuild(self):
        # Rerender text
        self.text = self.font.render('lives: ' + str(self.snake.lives), True, Color('black'), Color('white'))

        # Background Surfaces
        self.window.blit(self.bg_surface, (0, 0))
        self.window.blit(self.text, (450, 10))

        # Sprites in Spritegroups
        if self.sprite_groups:
            for sprite_group in self.sprite_groups:
                pygame.sprite.Group.draw(sprite_group, self.window)

        if self.main_menu.is_enabled():
            self.main_menu.draw(self.window)

    def create_food(self):
        random_food_element = FoodElement(self)
        self.food_sg.add(random_food_element)

    def start_game(self):
        self.init_game()
        self.main_menu.disable()

    # TODO Menu Design!!
    def init_continue_menu(self):
        # pygame_menu
        self.continue_menu = pygame_menu.Menu('Continue?', 400, 400, theme=self.mytheme)
        self.continue_menu.add.button('Continue', self.disable_menu)
        self.continue_menu.add.button('Main Menu', self.back_to_main)
        return self.continue_menu

    def init_main_menu(self):
        # pygame_menu
        self.main_menu = pygame_menu.Menu('Main Menu', 400, 400, theme=self.mytheme)
        self.main_menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=self.set_difficulty())
        self.main_menu.add.button('Play', self.start_game)
        self.main_menu.add.button('Highscore', self.highscore_menu)
        self.main_menu.add.button('How To Play', self.how_to_menu)
        self.main_menu.add.button('Quit', pygame_menu.events.EXIT)
        return self.main_menu

    def init_highscore_menu(self):
        # pygame_menu
        self.highscore_menu = pygame_menu.Menu('Highscore', 400, 400, theme=self.mytheme)
        # self.highscore_menu.add.button('Main Menu', self.back_to_main_event())
        self.highscore_menu.add.button('Main Menu', self.back_to_main)
        return self.highscore_menu

    def init_how_to_menu(self):
        # pygame_menu
        self.how_to_menu = pygame_menu.Menu('How To Play', 400, 400, theme=self.mytheme)
        self.how_to_menu.add.button('Main Menu', pygame_menu.events.BACK)
        return self.how_to_menu

    def back_to_main(self):
        self.main_menu._current = self.main_menu

    def disable_menu(self):
        self.main_menu.disable()

    def set_difficulty(self):
        pass
