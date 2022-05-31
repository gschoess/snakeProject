#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import pygame

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'


class Snake(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/snake_head.png")
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect()
        # display snake head in the middle of the screen (approx.)
        self.rect.top = screen.get_rect().height / 2 - self.rect.width
        self.rect.left = screen.get_rect().width / 2 - self.rect.width
        # body and direction for further calculations
        self.body = []
        self.direction = None

    def draw_snake(self, snake_group, screen):
        """Draws the snake head of the sprite element.
        Draws every snake element in the body list.
        """
        snake_group.draw(screen)
        grid_center = self.rect.width / 2
        for snake_element in self.body:
            pygame.draw.circle(screen, (10, 200, 10), (snake_element[0] +
                               grid_center, snake_element[1] + grid_center),
                               self.rect.width / 2, 5)

    def update_snake(self, eat):
        """Add body part with rect.left and rect.top of the snake head to
        the body list. Remove this body part, if the snake hasn't eaten.
        """
        self.body.append((self.rect.left, self.rect.top))
        self.move()
        if not eat:
            self.body.pop(0)

    def move(self):
        if self.direction == UP:
            self.rect.top -= self.rect.width
        if self.direction == DOWN:
            self.rect.top += self.rect.width
        if self.direction == LEFT:
            self.rect.left -= self.rect.width
        if self.direction == RIGHT:
            self.rect.left += self.rect.width



