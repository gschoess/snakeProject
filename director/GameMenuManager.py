#!/usr/bin/python
# ‐*‐ encoding: utf‐8 ‐*‐

# STATIC methods
import pygame_menu
from pygame_menu import sound
from db.HighscoreDB import HighscoreDB


def init_my_theme():
    mytheme = pygame_menu.themes.THEME_SOLARIZED.copy()
    mytheme.title_font = pygame_menu.font.FONT_8BIT
    return mytheme


class MenuManager:
    def __init__(self, game):
        # Menus  !!! Order important (From leaves to root) for initializing, references not updated after initializing the menu !!!
        self.game = game
        self.db = HighscoreDB()
        self.table = None
        self.mytheme = init_my_theme()
        self.engine = self.init_sound_engine()
        self.how_to_menu = self.init_how_to_menu()
        self.highscore_menu = self.init_highscore_menu(self.db)
        self.main_menu = self.init_main_menu()
        self.continue_menu = self.init_continue_menu()
        self.end_menu = None

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
        self.main_menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=self.game.set_difficulty())
        self.main_menu.add.button('Play', self.game.start_game)
        self.main_menu.add.button('Highscore', self.highscore_menu)
        self.main_menu.add.button('How To Play', self.how_to_menu)
        self.main_menu.add.button('Quit', pygame_menu.events.EXIT)
        self.main_menu.set_sound(self.engine, recursive=True)  # Apply on menu and all sub-menus
        return self.main_menu

    def init_sound_engine(self):
        self.engine = sound.Sound()
        self.engine.set_sound(sound.SOUND_TYPE_CLOSE_MENU, 'media/music/Inept-70s-Crooks_Looping.mp3', loops=10,
                              fade_ms=5)
        self.engine.set_sound(sound.SOUND_TYPE_EVENT, 'media/music/The-Hard-Luck-Gang.mp3', loops=10, fade_ms=5)
        return self.engine

    def init_highscore_menu(self, db):
        # pygame_menu
        self.highscore_menu = pygame_menu.Menu('Highscore', 400, 400,
                                               theme=self.mytheme)
        self.table = self.highscore_menu.add.table()
        self.table.default_cell_padding = 5
        self.table.default_cell_align = pygame_menu.locals.ALIGN_CENTER
        self.table.add_row(['Place', 'Name', 'Score'],
                           cell_font=pygame_menu.font.FONT_FIRACODE_BOLD)

        highscores = db.get_highscores()
        for place, player in enumerate(highscores, start=1):
            self.table.add_row([place, player[0], player[1]])

        self.highscore_menu.add.button('Main Menu', self.back_to_main)

        return self.highscore_menu

    def init_how_to_menu(self):
        # pygame_menu
        self.how_to_menu = pygame_menu.Menu('How To Play', 400, 400, theme=self.mytheme)
        self.how_to_menu.add.button('Main Menu', self.back_to_main)
        return self.how_to_menu

    def back_to_main(self):
        self.main_menu._current = self.main_menu

    def disable_menu(self):
        self.main_menu.close()

    def init_end_menu(self):
        # pygame_menu
        self.end_menu = pygame_menu.Menu('Your Score', 400, 400,
                                         theme=self.mytheme)
        self.end_menu.add.label('You reached: ' + str(self.game.score) +
                                'points')
        self.end_menu.add.label('Enter your name:')
        name_input = self.end_menu.add.text_input('', default='Player')
        self.end_menu.add.button('Add me!', lambda:
                                 self.show_new_highscore(name_input))
        self.end_menu.add.button('Main Menu', self.back_to_main)

        return self.end_menu

    def show_new_highscore(self, name_input):
        name = name_input.get_value()
        self.db.add_to_highscore(name, self.game.score)
        self.main_menu._current = self.init_highscore_menu(self.db)
