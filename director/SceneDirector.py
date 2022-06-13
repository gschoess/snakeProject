#!/usr/bin/python
# ‐*‐ encoding: utf‐8 ‐*‐
from datetime import datetime

import pygame
import threading
import time

from scene.Intro import Intro
from scene.Game import Game


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

        # Precreate Game Scene
        self.intro = Intro(self)
        self.game = Game(self)
        self.current_scene = self.intro

        # Clock
        self.clock = pygame.time.Clock()

        # Events
        self.keepGoing = False  # flag for ending main loop

        # Threads
        self.thread_started = False

        # Start Game
        self.run_game()

    def run_game(self):
        # A - Action (broken into ALTER steps)
        # A - Assign values to key variables
        self.keepGoing = True

        # L - Set up main loop
        while self.keepGoing:
            # T - Timer to set frame rate
            if self.game.speed_up:
                self.clock.tick(int(self.FPS * 1.5))
                if not self.thread_started:
                    self.thread_started = True
                    thread = threading.Thread(target=self.wait_for_it)
                    thread.start()
            else:
                self.clock.tick(self.FPS)

            # E – Event handling & Prebuilding new scene
            events = pygame.event.get()
            self.current_scene.handle_events(events)
            self.current_scene.prebuild()

            # R - Refresh display
            pygame.display.update()

    def wait_for_it(self):
        start = datetime.now()
        time.sleep(5)
        end = datetime.now()
        delta = (end - start)
        print('HE SLEPT', delta)
        self.game.decrease_speed()
        self.thread_started = False

    def start_menu(self):
        self.game.mmgr.main_menu.enable()
        self.game.mmgr.engine.play_event()
        self.current_scene = self.game
