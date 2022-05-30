#!/usr/bin/python
# ‐*‐ encoding: utf‐8 ‐*‐

# I - Import and initialize
import random
import pygame
import shelve
# import pygame_textinput
from pygame import *
from pygame.sprite import *
from director.SceneDirector import SceneController

from sprites.Snake import Snake

pygame.init()

# D - Display configuration   -> DOne in SceneController
#
# size = (640, 480)
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("Python - The Snake Game")


# E - Entities   --> Initialized with Scenes
scene_controller = SceneController()

# snake1 = Snake(1)
#
# sprite_group = pygame.sprite.Group()
# sprite_group.add(snake1)
#
# bg = pygame.image.load("img/bg_lawn_centralPark.jpg")
# bg = pygame.transform.scale(bg, size)
#
# bg_red = pygame.Surface(size)
# bg_red.convert()
# bg_red.fill((255, 0, 0))
#
# bg_white = pygame.Surface(size)
# bg_white.convert()
# bg_white.fill('white')
#
# bg_green = pygame.Surface(size)
# bg_green.convert()
# bg_green.fill('white')

# textinput = pygame_textinput.TextInputVisualizer()

# d = shelve.open('score.txt')  # here you will save the score variable


# A - Action (broken into ALTER steps)
# A - Assign values to key variables
clock = pygame.time.Clock()
keepGoing = True
gameover = False
ctr = 0
pygame.time.set_timer(USEREVENT, 30)
countdown = 10  # game time in seconds
if not d:
    d['nobody'] = 0

score = list(d.values())[0]

# L - Set up main loop
while keepGoing:

    # T - Timer to set frame rate
    clock.tick(30)
    # E – Event handling
    events = pygame.event.get()

    # if not gameover:
    #     for event in events:
    #         if event.type == pygame.QUIT:
    #             keepGoing = False
    #         elif event.type == MOUSEBUTTONDOWN:
    #             if mole.hit(mouse.get_pos()):
    #                 mole.cry()
    #                 ctr += 1
    #                 screen.blit(bg_red, (0, 0))
    #                 pygame.display.flip()
    #                 time.delay(250)
    #                 break
    #         elif event.type == USEREVENT:
    #             mole.flee()
    #             pygame.time.set_timer(USEREVENT, 1000)
    #             if countdown > 0:
    #                 countdown -= 1
    #             else:
    #                 gameover = True

        # R - Refresh display
        screen.blit(bg, (0, 0))
        text = font.render('Highscore: ' + str(list(d.keys())[0]) + " " + str(list(d.values())[0]), True,
                           Color('black'), Color('white'))
        screen.blit(text, (450, 10))
        text = font.render('Remaining time:' + str(countdown).rjust(3), True, Color('black'), Color('white'))
        screen.blit(text, (10, 10))
        text = font.render('Moles: ' + str(ctr), True, Color('black'), Color('white'))
        screen.blit(text, (10, 40))
        sprite_group.update()
        sprite_group.draw(screen)
        pygame.display.flip()

    if gameover:

        # Feed textinput with events every frame
        textinput.update(events)

        for event in events:

            screen.blit(bg_white, (0, 0))
            if ctr > int(str(score)):
                text = font.render("GAME OVER! You've hit: " + str(ctr) + " moles. New highscore!", True,
                                   Color('black'))
                text1 = font.render("Highscore-Alias: ", True, Color('black'))
                screen.blit(text1, (50, 150))
                screen.blit(textinput.surface, (50, 200))

                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    del d[list(d.keys())[0]]
                    d[textinput.value] = str(ctr)
                    keepGoing = 0
            else:
                text = font.render("GAME OVER! You've hit: " + str(ctr) + " moles. Not enough for the highscore!", True,
                                   Color('black'))
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    keepGoing = 0

            screen.blit(text, (50, 100))
            pygame.display.flip()

d.close()
