import pygame

import TitleScene
import TestPlanet
import TestSpaceship

SCREEN_SIZE = (1240, 640)
    

def test_spaceship_planet_init(game_state):
    game_state.spaceship = Spaceship()
    
    game_state.planet_list = []
    
    game_state.planet_list.append(Planet(100, (320, 110), (255, 255, 0)))
    game_state.planet_list.append(Planet(200, (800, 400), (255, 0, 255)))
    game_state.sp_planets = pygame.sprite.Group()
    for planet in game_state.planet_list:
        game_state.sp_planets.add(planet)

    game_state.sp_spaceship = pygame.sprite.Group()
    game_state.sp_spaceship.add(game_state.spaceship)

def test_spaceship_planet(screen, game_state):

    if pygame.sprite.spritecollide(game_state.spaceship, game_state.sp_planets, False):
        print("collision detected")
        
        spaceship = game_state.spaceship
        planets = pygame.sprite.spritecollide(spaceship, game_state.sp_planets, False, pygame.sprite.collide_mask)
        if planets:
            print("sprite collision")
            for planet in planets:
                
                # take the position of the planet
                planet_pos = planet.get_pos()
                
                # take the position of the spaceship
                spaceship_pos = spaceship.get_pos()
                
                # calculate the vector
                outward_vec = spaceship_pos - planet_pos
                
                if outward_vec == pygame.Vector2(0, 0):
                    outward_vec = pygame.Vector(1, 0)
                
                
                outward_vec.normalize_ip()
                
                
                spaceship.rect.center = planet_pos + outward_vec * (spaceship.radius + planet.radius + 2)
                
                spaceship.reset_force()
                
                print("moving space ship to:", game_state.spaceship.rect.center)
                
                
                
                
    game_state.spaceship.change_dir()
    
    game_state.spaceship.calc_forces(game_state.planet_list)
    game_state.spaceship.move()
    game_state.spaceship.borders(screen)            
        
    
    # draw planets
    game_state.sp_planets.draw(screen)
    
    # draw the spaceship
    game_state.sp_spaceship.draw(screen)            
    
    
    
    
    


class GameState:

    
    TITLE_SCREEN = 0
    NEW_GAME = 1
    
    TEST_PLANET = 2
    TEST_SPACESHIP = 3
    TEST_SPACEPLANET = 4
    
    

    def __init__(self, screen):
        self.state = self.TEST_SPACESHIP
        
        if self.state == self.TITLE_SCREEN:
            self.title_screen = TitleScene.TitleScene(screen)
        
        if self.state == self.TEST_PLANET:
            self.test_planet = TestPlanet.TestPlanet(screen)
        
        if self.state == self.TEST_SPACESHIP:
            self.test_spaceship = TestSpaceship.TestSpaceship(screen)
        
        if self.state == self.TEST_SPACEPLANET:
            test_spaceship_planet_init(self)
        
    
    def run(self, screen):
        if self.state == self.TITLE_SCREEN:
            self.title_screen.run(self)
        
        if self.state == self.NEW_GAME:
            pass
            
        if self.state == self.TEST_PLANET:
            self.test_planet.run()
        
        if self.state == self.TEST_SPACESHIP:
            self.test_spaceship.run()
        
        if self.state == self.TEST_SPACEPLANET:
            test_spaceship_planet(screen, self)
            

def main():
    
    # initialize pygame stuff
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Spacers")
    
    clock = pygame.time.Clock()
    
    # make a background
    background = pygame.Surface(SCREEN_SIZE)
    background.fill((200, 200, 200))
    
    # game controlling agency
    game_state = GameState(screen)
    
    # do the things
    while True:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        screen.blit(background, (0, 0))

        game_state.run(screen)
        
        pygame.display.flip()
         
         
    
    
if __name__ == "__main__":
    main()   


