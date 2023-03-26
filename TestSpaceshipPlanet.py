import pygame

import Spaceship
import Planet

class TestSpaceshipPlanet:

    def __init__(self, screen):
        self.screen = screen
        
        initial_position = pygame.Vector2(screen.get_size()) / 2
        self.spaceship = Spaceship.Spaceship(initial_position)
        
        self.planet_list = []
        
        self.planet_list.append(Planet.Planet(100, (320, 110), (255, 255, 0)))
        self.planet_list.append(Planet.Planet(200, (800, 400), (255, 0, 255)))   
        
        self.sp_planets = pygame.sprite.Group()
        for planet in self.planet_list:
            self.sp_planets.add(planet)

        self.sp_spaceship = pygame.sprite.Group()
        self.sp_spaceship.add(self.spaceship)   
        
        loaded_background = pygame.image.load("./images/background_images/background_image.png")
        self.background = pygame.transform.scale(loaded_background, screen.get_size())
    
    
    def run(self):
    
        self.screen.blit(self.background, (0, 0))
 
        if pygame.sprite.spritecollide(self.spaceship, self.sp_planets, False):
            print("Rectangle collision detected")
            
            planets = pygame.sprite.spritecollide(self.spaceship, self.sp_planets, False, pygame.sprite.collide_mask)
            
            if planets:
                print("sprite collision")
                for planet in planets:
                    
                    # take the position of the planet
                    planet_pos = planet.get_pos()
                    
                    # take the position of the spaceship
                    spaceship_pos = self.spaceship.get_pos()
                    
                    # calculate the vector
                    outward_vec = spaceship_pos - planet_pos
                    
                    if outward_vec == pygame.Vector2(0, 0):
                        outward_vec = pygame.Vector(1, 0)
                    
                    
                    outward_vec.normalize_ip()
                    
                    
                    self.spaceship.rect.center = planet_pos + outward_vec * (self.spaceship.radius + planet.radius + 7)
                    
                    self.spaceship.reset_force()
                    
                    print("moving space ship to:", self.spaceship.rect.center)
                    
                    
                    
                    
        self.spaceship.change_dir()
        
        self.spaceship.calc_forces(self.planet_list)
        self.spaceship.move()
        self.spaceship.borders(self.screen)            
            
        
        # draw planets
        self.sp_planets.draw(self.screen)
        
        # draw the spaceship
        self.sp_spaceship.draw(self.screen) 
        
        
               
