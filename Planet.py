import pygame

class Planet(pygame.sprite.Sprite):

    def __init__(self, radius, position, color, background=(0, 0, 0, 0)):
        super().__init__()
        
        # open the image
        loaded_image = pygame.image.load("./images/planet_images/planet_image_test.png").convert_alpha()
        
        loaded_image = pygame.transform.scale(loaded_image, (radius*2, radius*2))

        self.radius = radius
        self.mass = 10000
        
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        self.image.fill(background) 
        
        #pygame.draw.circle(self.image, color, [radius, radius], radius)
        self.image.blit(loaded_image, (0, 0))
        
        self.mask = pygame.mask.from_surface(self.image)
        
        self.rect = self.image.get_rect(center=position)
        
    def get_pos(self):
        return pygame.Vector2(self.rect.center)
