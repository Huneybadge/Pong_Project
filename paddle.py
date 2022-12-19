"""
Software Carpentry Final
EN.540.635

"""

"""
This code is that holds the class to make the paddles from the pong game.

"""
import pygame
bg_color = (0, 0, 0) # Black

class Paddle(pygame.sprite.Sprite):
    """
    Paddle class that makes the paddle and its attributes.
    """
    def __init__(self, color, width, height):
        """
        Class is instantiated. Variables are initiated.
        
        Parameters
        ----------
        self :  Instance of the class.
        
        color : tuple
            Color of the paddle.
        
        width : int
            Width of the paddle.
        
        height : int
            Height of the paddle.

        """
        # Initializes the class. 
        super().__init__()
        
        # Set up the paddle with the color and size.
        self.image = pygame.Surface([width, height])
        self.image.fill(bg_color)
        self.image.set_colorkey(bg_color)
        
        # Drawing the paddle.
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        # Getting rectangle object.
        self.rect = self.image.get_rect()
    
    def moveUp(self, pixels):
        """
        Function for the paddle moving up.
        
        Parameters
        ----------
        self :  Instance of the class.
        
        pixels : int
            Number of pixels the paddle moves up per step.
        
        """
        self.rect.y -= pixels
        # Check that you're not going too far off the screen
        if self.rect.y < 0:
            self.rect.y = 0
        
    def moveDown(self, pixels):
        """
        Function for the paddle moving down.
        
        Parameters
        ----------
        self :  Instance of the class.
        
        pixels : int
            Number of pixels the paddle moves down per step.
        
        """
        self.rect.y += pixels
        # Again check that you're not going too far off the screen
        if self.rect.y > 500: # Take off 100 due to paddle length.
            self.rect.y = 500
            
