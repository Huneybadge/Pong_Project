#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 17:56:28 2022

@author: patriciakolodziejski
"""

import pygame
bg_color = (0, 0, 0) # Black

class Paddle(pygame.sprite.Sprite):
    # This class makes the paddles for the game.
    
    def __init(self, color, width, height): # bg_color):
        # Initializes the class. 
        super().__init()
        
        # Set up the paddle with the color and size.
        self.image = pygame.Surface([width, height])
        self.image.fill(bg_color)
        self.image.set_colorkey(bg_color)
        
        # Drawing the paddle.
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        # Getting rectangle object.
        self.rect = self.image.get_rect()