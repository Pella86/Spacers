import pygame

import Spaceship


class TestSpaceship:

    def __init__(self, screen):
        self.screen = screen
        
        initial_position = pygame.Vector2(screen.get_size()) / 2
        self.spaceship = Spaceship.Spaceship(initial_position)

        self.sp_spaceship = pygame.sprite.Group()
        self.sp_spaceship.add(self.spaceship)
        
    def run(self):
    
        self.spaceship.change_dir()
        self.spaceship.move()
        self.spaceship.borders(self.screen)

        self.sp_spaceship.draw(self.screen)    
        
        
