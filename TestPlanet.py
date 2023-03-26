import pygame

import Planet


class TestPlanet:

    def __init__(self, screen):
        self.screen = screen
        
        planet_radius = 200
        planet_position = pygame.Vector2(screen.get_size()) / 2
        planet_background = (255, 0, 0, 50)
        planet_color = "red" 
        
        planet = Planet.Planet(planet_radius, planet_position, planet_color, planet_background)
 
        self.sp_planet = pygame.sprite.Group()
        self.sp_planet.add(planet)      
    
    def run(self):
        self.sp_planet.draw(self.screen)
           
