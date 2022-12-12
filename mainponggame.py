#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 13:37:11 2022

@author: patriciakolodziejski
"""

import pygame 
from paddle import Paddle
from ball import Ball
#from button import Button


pygame.init()


# Defining board colors.
bg_color = (0, 0, 0) # Black
object_color = (255, 255, 255) #White 
text_color = (255,255,255)
color_light = (170,170,170)
color_dark = (100,100,100)

# Displaying the game
table_size = (900, 600)
board = pygame.display.set_mode(table_size)
width = board.get_width()
height = board.get_height()
pygame.display.set_caption("Pong")

# Clock used to update the game
clock = pygame.time.Clock()

# Initialing loops for the game.
main_game = True
intro = True
game_mode = False
infinite_game_on = False
best_10_on = False

def button(mouse, x1, y1, x2, y2, length, height):
    if x1 <= mouse[0] <= x2 and y1 <= mouse[1] <= y2:
              pygame.draw.rect(board,color_light, [x1, y1, length, height])
    else:
        pygame.draw.rect(board,color_dark,[x1, y1, length, height])
    

#Adding button
#button_1 = Button("Start", (450, 300), font=30, bg="navy", feedback="start game")
while main_game:
    
    while intro:
        # Storing mouse movemnt for intro.
        mouse = pygame.mouse.get_pos()
        
        # Events for the game.
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Pressing the Quit corner.
                main_game = False
            elif event.type == pygame.MOUSEBUTTONDOWN: # Button click events.
                if width/2+10 <= mouse[0] <= width/2 + 150 and height/2 + 150\
                    <= mouse[1] <= height/2 + 190: # Quit button.
                        pygame.quit()
                        main_game = False
                elif width/2 - 150 <= mouse[0] <= width/2 - 10 and \
                    height/2 + 150 <= mouse[1] <= height/2 + 190: # Start button.
                        intro = False
                        game_mode = True # Brings you to select game mode.
                    
        # Breaking out of loop if quit.
        if main_game == False: 
            break
        
        # Creating the intro screen.
        board.fill(bg_color)
        largeText = pygame.font.SysFont("comicsansms", 115)
        TextSurf = largeText.render("PONG", True, object_color)
        TextRect = TextSurf.get_rect()
        TextRect.center = ((width/2),(height/2))
        board.blit(TextSurf, TextRect)
        
        # Making the quit button.
        button(mouse, width/2 + 10, height/2 + 150, width/2 + 150, height/2 + 190, 140, 40)
       
        # Text for the quit button.
        smallfont = pygame.font.SysFont('Corbel', 35)  # Selecting the font.
        quit_button_text = smallfont.render('Quit', True , text_color) 
        board.blit(quit_button_text, (width/2 +50, height/2 + 155))
        
        # Making the start button.
        button(mouse, width/2 - 150, height/2 + 150, width/2 - 10, height/2 + 150+ 40, 140, 40)
        
        # Specifying the text for the start button using same font as for quit.
        start_button_text = smallfont.render('Start' , True , text_color)
        board.blit(start_button_text, (width/2 - 150 + 40, height/2 + 150 + 5))
        
        # Updating the display.
        pygame.display.update()
        clock.tick(15)
        
    while game_mode:
        # Storing mouse movemnt for selecting game mode.
        mouse = pygame.mouse.get_pos()
        
        # Initializing player scores to start at 0
        score_1 = 0
        score_2 = 0
        
        # Paddle 1.
        paddle_1 = Paddle(object_color, 10, 100)# bg_color)
        paddle_1.rect.x = 20
        paddle_1.rect.y = 200
        
        # Paddle 2.
        paddle_2 = Paddle(object_color, 10, 100) #bg_color)
        paddle_2.rect.x = 870
        paddle_2.rect.y = 200
        
        # Defining the ball.
        ball = Ball(object_color, 10, 10)
        ball.rect.x = 345
        ball.rect.y = 195
        
        # List of sprites (game objects)
        all_sprites = pygame.sprite.Group()
        
        # Adding paddles
        all_sprites.add(paddle_1)
        all_sprites.add(paddle_2)
        all_sprites.add(ball)
        
        # Events for the game.
        for event in pygame.event.get():
               if event.type == pygame.QUIT: # Pressing the Quit corner.
                   pygame.quit()
                   main_game = False
               elif event.type == pygame.MOUSEBUTTONDOWN: # Button click events.
                   if width/2 - 100 <= mouse[0] <= width/2 + 100 and height/2 - 100 \
                       <= mouse[1] <= height/2 - 60: # Selecting infinite mode.
                       game_mode = False # Ending select mode.
                       infinite_game_on = True # Initilaizing infinite mode.
                       best_10_on = False
                   elif width/2 - 100 <= mouse[0] <= width/2 + 100 and  height/2 - 40 \
                       <= mouse[1] <= height/2:
                       game_mode = False
                       infinite_game_on = True 
                       best_10_on = True
        # Breaking out of loop if quit.
        if main_game == False:
            break
        
        # Creating the game mode screen.         
        board.fill(bg_color)
        
        #Selecting font for the buttons.
        game_mode_font = pygame.font.SysFont('Corbel',35)
        
        # Creating the buttons.
        button(mouse, width/2 - 100, height/2 - 100, width/2 + 100, height/2 - 60, 200, 40)
        button(mouse, width/2 - 100, height/2 - 40, width/2 + 100, height/2, 200, 40)
        
        # Creating text for the buttons.
        mode_font = pygame.font.SysFont('Corbel', 35)  # Selecting the font.
        
        infinite_game_text = mode_font.render('Infinite mode' , True , text_color)
        board.blit(infinite_game_text, (width/2 - 80, height/2 - 90))
        
        best_of_ten_text = mode_font.render('Best of 10', True, text_color)
        board.blit(best_of_ten_text, (width/2 - 60, height/2 - 30))
        
        
        # Updating the display.
        pygame.display.update()
        clock.tick(15)
    
    # Main Game Loop 
    while infinite_game_on: 
        
        mouse = pygame.mouse.get_pos()
        # Gets events from the queue.
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # User exits game.
                pygame.quit() #Exits loop.
                main_game = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x: # Pressing the x key will quit the game
                    pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                  
                #if the mouse is clicked on the
                # button the game is terminated
                if width/2 + 10 <= mouse[0] <= width/2+150 and 0 <= mouse[1] \
                    <= 40:
                    infinite_game_on = False
                    main_game = False
                    pygame.quit()
                elif width/2 - 210 <= mouse[0] <= width/2 - 10 and 0 <= \
                    mouse[1] <= 40:
                    infinite_game_on = False
                    game_mode = True
            
        # Breaking out of loop if quit.    
        if main_game == False:
            break
        
        # Establising key movements.
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
            score_1 += 1
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x <= 0:
            score_2 += 1
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y > 590:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y < 0:
            ball.velocity[1] = -ball.velocity[1]
            
        # Hitting the paddle.
        if pygame.sprite.collide_mask(ball, paddle_1) or \
        pygame.sprite.collide_mask(ball, paddle_2): 
            ball.bounce()
            
        # Clearing screen to background color.
        board.fill(bg_color)
        
        # Creating the font.
        smallfont = pygame.font.SysFont('Corbel', 35)
        
        # Making quit button.
        button(mouse, width/2 + 20, 0, width/2+150, 40, 140, 40)
        quit_button_text = smallfont.render('Quit' , True, text_color)
        board.blit(quit_button_text, (width/2 + 60, 10))
        
        # Making change game mode button.
        button(mouse, width/2 - 210, 0, width/2 - 10, 40, 200, 40)
        change_mode_text = smallfont.render('Change Mode' , True, text_color)
        board.blit(change_mode_text, (width/2 - 200, 10))
        
        # Drawing the net or half court.
        pygame.draw.line(board, object_color, [450, 0], [450, 600], 5)
        
        # Drawing the sprites (grame objects).
        all_sprites.draw(board)
        
        # Display scores
        font = pygame.font.Font(None, 74)
        text = font.render(str(score_1), 1, object_color)
        board.blit(text, (100, 10))
        text = font.render(str(score_2), 1, object_color)
        board.blit(text, (800, 10))
        
        # Best of 10 mode
        if best_10_on:
            if score_1 == 10 or score_2 == 10:
                ball.velocity[0] = 0
                ball.velocity[1] = 0
                ball.rect.y = height / 2
                ball.rect.x = width / 2
                win_font = pygame.font.SysFont('Corbel', 40)
                pygame.draw.rect(board,color_light, [width / 2 - 100, height / 2 - 20, 200, 40])
                
                # Changing 'Change Mode' Button to 'Play Again' button
                button(mouse, width/2 - 210, 0, width/2 - 10, 40, 200, 40)
                play_again_text = smallfont.render('Play Again' , True, text_color)
                board.blit(play_again_text, (width/2 - 180, 10))
                if score_1 > score_2: 
                    player_text = win_font.render('Player 1 Wins!', 1, object_color)
                else: 
                    player_text = win_font.render('Player 2 Wins!', 1, object_color)
                board.blit(player_text, (width / 2 - 95, height / 2 - 10))

        # Updating screen.
        pygame.display.flip()
        
        # Setting frames per second.
        clock.tick(60)
