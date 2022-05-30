#! /usr/bin/env python
# -*- coding: UTF-8 -*-

# Import and Initialization
import pygame
from pygame.locals import *
from snake import Snake

black = (0, 0, 0)


def main():
    pygame.init()
    # Display configuration
    size = (640, 480)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Python - The Snake Game')


    # Entities
    tile_counter = 1
    snake1 = Snake(tile_counter)
    tile_counter += 1
    snake2 = Snake(tile_counter)
    tile_counter += 1
    snake3 = Snake(tile_counter)

    # sprite Group erstellen
    sprite_group = pygame.sprite.Group()
    sprite_group.add(snake1)
    sprite_group.add(snake2)
    sprite_group.add(snake3)
    # Action --> ALTER
    # Assign Variables
    running = True
    clock = pygame.time.Clock()

    # Loop
    while running:
        # Timer
        clock.tick(30)
        # Event Handling
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                break

            if event.type == KEYDOWN:
                if event.key == pygame.K_DOWN:
                    for snake in sprite_group:
                        if snake.dir_y == 0:
                            snake.dir_x = 0
                            snake.dir_y = 3
    #              if snake1.dir_y == 0:
    #                 snake1.dir_x = 0
    #                 snake1.dir_y = 3
                if event.key == pygame.K_UP:
                    for snake in sprite_group:
                        if snake.dir_y == 0:
                            snake.dir_x = 0
                            snake.dir_y = -3
            #        if snake1.dir_y == 0:
            #           snake1.dir_x = 0
            #           snake1.dir_y = -3
                if event.key == pygame.K_LEFT:
                    for snake in sprite_group:
                        if snake.dir_x == 0:
                            snake.dir_x = -3
                            snake.dir_y = 0
            #       if snake1.dir_x == 0:
            #          snake1.dir_y = 0
            #          snake1.dir_x = -3
                if event.key == pygame.K_RIGHT:
                    for snake in sprite_group:
                        if snake.dir_x == 0:
                            snake.dir_x = 3
                            snake.dir_y = 0
            #        if snake1.dir_x == 0:
            #           snake1.dir_y = 0
            #           snake1.dir_x = 3
                # QUIT event, if Esc key pressed
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
        # Redisplay
        # pygame.display.update()
        # snake.move()
        sprite_group.update()
        screen.fill(black)
        sprite_group.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()
