import pygame 
from random import randint 

bg_color = (0,0,0)

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
        self.velocity = [randint(4,8), randint(-8,8)]
        
        # Get the object with the dimensions of the image
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)
