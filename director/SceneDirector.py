#!/usr/bin/python
# ‐*‐ encoding: utf‐8 ‐*‐
import pygame
import pygame_menu
from pygame.constants import USEREVENT

from scene.Game import Game

# Custom Event to get back to Main Menu from Highscore
BACKTOMAIN = USEREVENT+1
back_to_main_event = pygame.event.Event(BACKTOMAIN, message="Return to main Menu!")


class SceneDirector:
    """
    Properties:
    - knows the current active scene and music

    Methods:
    - hands over events to current scene
    - switches scenes and music
    - refreshes the current display
    """

    def __init__(self):
        # I - Initialize
        pygame.init()

        # D - Display configuration
        self.SCREENSIZE = (640, 480)
        self.FPS = 10
        self.window = pygame.display.set_mode(self.SCREENSIZE)
        pygame.display.set_caption("The PySnakeProject")

        # E - Entities
        # Sound
        self.music_mixer = pygame.mixer

        # Menus  !!! Order important (From leaves to root) for initializing, references not updated after initializing the menu !!!
        self.mytheme = init_my_theme()

        # Create menu objects ! Order important (from root to top), initialized menus can not be updated after linking
        self.how_to_menu = self.init_how_to_menu()
        self.highscore_menu = self.init_highscore_menu()
        self.main_menu = self.init_main_menu()
        self.active_menu = self.main_menu

        #  Precreate Game Scene
        self.game = Game(self)
        self.current_scene = self.game

        # TODO: Update Current Scene MAIN MENU!
        # self.current_scene = self.game

        # Clock
        self.clock = pygame.time.Clock()

        # Events
        self.keepGoing = False  # flag for ending main loop

        # Start Game
        self.run_game()

    def run_game(self):
        # A - Action (broken into ALTER steps)
        # A - Assign values to key variables
        self.keepGoing = True

        # L - Set up main loop
        while self.keepGoing:
            # T - Timer to set frame rate
            self.clock.tick(self.FPS)

            # E – Event handling & Prebuilding new scene
            events = pygame.event.get()

            if self.active_menu.is_enabled():
                #test
                self.current_scene.handle_events(events)

                self.current_scene.prebuild()  # Spielfeld bleibt im Hintergrund sichtbar und loops werden aktualisiert
                self.active_menu.update(events)
                if self.active_menu.is_enabled():
                    self.active_menu.draw(self.window)
            else:
                self.current_scene.handle_events(events)
                self.current_scene.prebuild()

            # R - Refresh display
            pygame.display.update()

    # TODO Menu Design!!
    def init_main_menu(self):
        # pygame_menu
        self.main_menu = pygame_menu.Menu('Main Menu', 400, 400, theme=self.mytheme)
        self.main_menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=self.set_difficulty())
        self.main_menu.add.button('Play', self.main_menu.disable)
        self.main_menu.add.button('Highscore', self.highscore_menu)
        self.main_menu.add.button('How To Play', self.how_to_menu)
        self.main_menu.add.button('Quit', pygame_menu.events.EXIT)
        return self.main_menu

    def init_highscore_menu(self):
        # pygame_menu
        self.highscore_menu = pygame_menu.Menu('Highscore', 400, 400, theme=self.mytheme)
        self.highscore_menu.add.button('Main Menu', self.back_to_main)
        return self.highscore_menu

    def init_how_to_menu(self):
        # pygame_menu
        self.how_to_menu = pygame_menu.Menu('How To Play', 400, 400, theme=self.mytheme)
        self.how_to_menu.add.button('Main Menu', pygame_menu.events.BACK)
        return self.how_to_menu

    def activate_menu(self, menu):
        self.active_menu = menu
        self.active_menu.enable()

    def back_to_main(self):
        print("event fired")
        pygame.event.post(back_to_main_event)

    # TODO
    def set_difficulty(self):
        pass

    # TODO
    def switch_music(self):
        pass


# STATIC methods
def init_my_theme():
    mytheme = pygame_menu.themes.THEME_SOLARIZED.copy()
    mytheme.title_font = pygame_menu.font.FONT_8BIT
    return mytheme
