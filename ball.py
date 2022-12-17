import pygame 
import random
from random import randint


bg_color = (0,0,0)
blue = (0, 0, 255) # Initialize blue
green = (0, 255, 0) # Initialize green
red = (255, 0, 0) # Initialize red
yellow = (255, 255, 0) # Initialize yellow
color_list = blue, green, red, yellow

class Ball(pygame.sprite.Sprite):
    # This class makes the ball
    
    def __init__(self, color, width, height):
        # Calling the parent class
        super().__init__()
         
        # Getting the color of the ball.
        # Setting the background.
        self.image = pygame.Surface([width, height])
        self.image.fill(bg_color)
        self.image.set_colorkey(bg_color)
        
        #Drawing the ball as a rectangle and getting starting velocity
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.velocity = [randint(4, 8), randint(-8, 8)]
        
        # Get the object with the dimensions of the image
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)
        pygame.draw.rect(self.image, (random.choice(color_list)), \
                         [0, 0, 10, 10]) # Sets a new color of the ball
    
    def restart_gamep1(self):
        self.rect.x = 450
        self.rect.y = 300
        self.velocity = [randint(4, 8), randint(-3, 3)]
    
    def restart_gamep2(self):
        self.rect.x = 450
        self.rect.y = 300
        self.velocity = [randint(4, 8), randint(-3, 3)]
    
    def set_color(self, new_color):
        # Change ball color to a new color
        self.color = new_color

class Speed_Ball(pygame.sprite.Sprite):
    # This class makes the ball for the speed stack mode
    
    def __init__(self, color, width, height):
        # Calling the parent class
        super().__init__()
        
        # Getting the color of the ball and setting the background
        self.image = pygame.Surface([width, height])
        self.image.fill(bg_color)
        self.image.set_colorkey(bg_color)
        
        # Drawing the ball as a rectangle and getting starting velocity
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.velocity = [4, randint(-3, 3)]
        
        # Get the object with the dimensions of the image
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        if self.velocity[0] < 0:
            self.velocity[0] = self.velocity[0] - 2
        elif self.velocity[0] > 0:
            self.velocity[0] = self.velocity[0] + 2
        self.velocity[1] = randint(-8, 8)
    
    def restart_gamep1(self):
        self.rect.x = 450
        self.rect.y = 300
        self.velocity = [-4, randint(-3, 3)]
    
    def restart_gamep2(self):
        self.rect.x = 450
        self.rect.y = 300
        self.velocity = [4, randint(-3, 3)]
        
