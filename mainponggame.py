#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 17:18:23 2022
@author: patriciakolodziejski
"""

import pygame 
from paddle import Paddle
from ball import Ball

pygame.init()

# Defining board colors.
bg_color = (0, 0, 0) # Black
object_color = (255, 255, 255) #White 

# Displaying the game
table_size = (900, 600)
board = pygame.display.set_mode(table_size)
pygame.display.set_caption("Pong")

# Clock used to update the game
clock = pygame.time.Clock()

# Paddle 1.
paddle_1 = Paddle(object_color, 10, 100)# bg_color)
paddle_1.rect.x = 20
paddle_1.rect.y = 200

# Paddle 2.
paddle_2 = Paddle(object_color, 10, 100) #bg_color)
paddle_2.rect.x = 870
paddle_2.rect.y = 200

ball = Ball(object_color, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

# List of sprites (game objects)
all_sprites = pygame.sprite.Group()

# Adding paddles
all_sprites.add(paddle_1)
all_sprites.add(paddle_2)
all_sprites.add(ball)
# Game loop until player exits.
game_on = True

# Main Game Loop 
while game_on: 
    # Gets events from the queue.
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # User exits game.
            game_on = False #Exits loop.
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x: # Pressing the x key will quit the game
                game_on = False
    
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        paddle_1.moveUp(5)
    if key[pygame.K_s]:
        paddle_1.moveDown(5)
    if key[pygame.K_UP]:
        paddle_2.moveUp(5)
    if key[pygame.K_DOWN]:
        paddle_2.moveDown(5)
        
    # Game Logic.
    all_sprites.update()
    
    # Check if the ball is bouncing against any wall (including paddles)
    if ball.rect.x >= 890:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 590:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]
        
    # Hitting the paddle.
    if pygame.sprite.collide_mask(ball, paddle_1) or pygame.sprite.collide_mask(ball, paddle_2):
        ball.bounce()
        
    # Clearing screen to background color.
    board.fill(bg_color)
    
    # Drawing the net or half court.
    pygame.draw.line(board, object_color, [450, 0], [450, 600], 5)
    
    #Drawing the sprites (grame objects).
    all_sprites.draw(board)
    
    # Updating screen.
    pygame.display.flip()
    
    # Setting frames per second.
    clock.tick(60)

pygame.quit()
