import pygame
bg_color = (0, 0, 0) # Black

class Paddle(pygame.sprite.Sprite):
    # This class makes the paddles for the game.
    
    def __init__(self, color, width, height): # bg_color):
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
        self.rect.y -= pixels
        # Check that you're not going too far off the screen
        if self.rect.y < 0:
            self.rect.y = 0
        
    def moveDown(self, pixels):
        self.rect.y += pixels
        # Again check that you're not going too far off the screen
        if self.rect.y > 500: # Take off 100 due to paddle length.
            self.rect.y = 500
            
