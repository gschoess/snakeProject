#! /usr/bin/env python
# -*- coding: UTF-8 -*-

# Import and Initialization
import pygame
from pygame.locals import *
from snake2 import Snake
from FoodElement import FoodElement

black = (0, 0, 0)
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'


def main():
    pygame.init()
    # Display configuration
    size = (400, 400)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Python - The Snake Game')

    # Entities
    snake = Snake(screen)
    sprite_group = pygame.sprite.Group()
    sprite_group.add(snake)

    food = FoodElement()
    food_group = pygame.sprite.GroupSingle()
    food_group.add(food)
    # Action --> ALTER
    # Assign Variables
    global running
    running = True
    clock = pygame.time.Clock()

    # Loop
    while running:
        # Timer
        clock.tick(10)
        # Event Handling
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                break

            if event.type == KEYDOWN:
                if event.key == pygame.K_UP:
                    if snake.direction != DOWN:
                        snake.direction = UP
                if event.key == pygame.K_DOWN:
                    if snake.direction != UP:
                        snake.direction = DOWN
                if event.key == pygame.K_LEFT:
                    if snake.direction != RIGHT:
                        snake.direction = LEFT
                if event.key == pygame.K_RIGHT:
                    if snake.direction != LEFT:
                        snake.direction = RIGHT
                # QUIT event, if Esc key pressed
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
        # Redisplay
        if pygame.sprite.collide_rect(snake, food):
            snake.update_snake(True)
            food.delete_food()
        else:
            snake.update_snake(False)
        screen.fill(black)
        snake.collide_screen(screen)
        snake.draw_snake(sprite_group, screen)
        food.create_food(screen)
        food_group.draw(screen)
        pygame.display.update()


if __name__ == '__main__':
    main()
