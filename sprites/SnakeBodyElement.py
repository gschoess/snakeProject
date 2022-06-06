#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from sprites.SpriteElement import SpriteElement


class SnakeBodyElement(SpriteElement):

    last_image_index = 0

    def __init__(self, x, y, dir_x, dir_y, size, game):
        self.image_list = ['media/images/snake_tile2.png', 'media/images/snake_tile3.png']
        self.game = game
        self.underground = False
        super().__init__(x, y, dir_x, dir_y, self.get_body_pic_by_order_in_list(), size, size, 'media/sounds/pain1.wav')

    """
    set_new_pos(). Notwendig da die Signatur der pygame.sprites.update()-Methode Sprites nicht geändert werden kann.
    Spricht keine Übergabe von Parametern möglich.
    """
    def set_new_pos(self, x, y):
        self.new_pos_x = x
        self.new_pos_y = y

    def update(self):

        self.rect.left = self.new_pos_x
        self.rect.top = self.new_pos_y

        if self.game.snake.underground:
            if self.rect.top == self.game.snake.entered_mole_hole.rect.top and self.rect.left == self.game.snake.entered_mole_hole.rect.left:
                self.image.set_alpha(0)
                self.underground = True

        if self.underground:
            if self.rect.top == self.game.snake.exit_mole_hole.rect.top and self.rect.left == self.game.snake.exit_mole_hole.rect.left:
                self.image.set_alpha(255)
                self.underground = False
                if self.game.snake.last_bel == self:
                    print("last element overground")
                    self.game.create_mole_hole_couple()

    """
    function to iterate the image_list in given order to create snakes with desired pattern
    """
    def get_body_pic_by_order_in_list(self):
        current_index = SnakeBodyElement.last_image_index
        SnakeBodyElement.last_image_index += 1
        # restart from beginning of list
        if SnakeBodyElement.last_image_index == len(self.image_list):
            SnakeBodyElement.last_image_index = 0

        return self.image_list[current_index]
