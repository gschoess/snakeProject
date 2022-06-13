#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from sprites.SpriteElement import SpriteElement


class SnakeBodyElement(SpriteElement):

    last_image_index = 0
    count_body_elements = 0

    def __init__(self, x, y, dir_x, dir_y, size, game):
        self.image_list = ['media/images/snake_tile2.png',
                           'media/images/snake_tile3.png']
        self.game = game
        self.underground = False
        SnakeBodyElement.count_body_elements += 1
        self.id = SnakeBodyElement.count_body_elements
        super().__init__(x, y, dir_x, dir_y,
                         self.get_body_pic_by_order_in_list(), size, size,
                         'media/sounds/pain1.wav')

    def update(self):
        self.rect.left = self.new_pos_x
        self.rect.top = self.new_pos_y
        self.image.set_alpha(self.new_alpha)

    """
    function to iterate the image_list in given order to create snakes 
    with desired pattern
    """
    def get_body_pic_by_order_in_list(self):
        current_index = SnakeBodyElement.last_image_index
        SnakeBodyElement.last_image_index += 1
        # restart from beginning of list
        if SnakeBodyElement.last_image_index == len(self.image_list):
            SnakeBodyElement.last_image_index = 0

        return self.image_list[current_index]
