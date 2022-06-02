#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from sprites.SpriteElement import SpriteElement


class SnakeHead(SpriteElement):
    def __init__(self, x, y, dir_x, dir_y, window, snake):
        super().__init__(x, y, dir_x, dir_y, 'media/images/snake_head.png', 10, 10, 'media/sounds/pain.wav')
        self.snake = snake
        self.window = window
        self.moving = False  # necessary attribut to disallow start moving against direction when snake at rest

    # def update(self):
    #     if self.moving:
    #         self.snake.body_follow_head()
    #         if not self.collide_window():
    #             self.rect.left += self.dir_x * self.rect.width
    #             self.rect.top += self.dir_y * self.rect.height

    def turn(self, dir_x, dir_y):
        self.set_dir(dir_x, dir_y)
        self.moving = True

    def set_new_pos(self):
        if self.moving:
            self.snake.body_follow_head()
            if not self.collide_window():
                self.new_pos_x += self.dir_x * self.rect.width
                self.new_pos_y += self.dir_y * self.rect.height

    def update(self):
        self.rect.left = self.new_pos_x
        self.rect.top = self.new_pos_y

    def collide_window(self):
        if self.rect.left < 0:
            print("left end of screen")
            self.rect.right = self.window.get_rect().width
            return True
        if self.rect.right > self.window.get_rect().width:
            print("right end of screen")
            self.rect.left = 0
            return True
        if self.rect.top < 0:
            print("upper end of screen")
            self.rect.bottom = self.window.get_rect().height
            return True
        if self.rect.bottom > self.window.get_rect().height:
            print("lower end of screen")
            self.rect.top = 0
            return True

    # def collide_window(self):
    #     if self.rect.left < 0:
    #         print("left end of screen")
    #         self.rect.right = self.window.get_rect().width
    #         return True
    #     if self.rect.right > self.window.get_rect().width:
    #         print("right end of screen")
    #         self.rect.left = 0
    #         return True
    #     if self.rect.top < 0:
    #         print("upper end of screen")
    #         self.rect.bottom = self.window.get_rect().height
    #         return True
    #     if self.rect.bottom > self.window.get_rect().height:
    #         print("lower end of screen")
    #         self.rect.top = 0
    #         return True
