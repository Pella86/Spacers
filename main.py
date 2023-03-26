import pygame

import TitleScene
import TestPlanet
import TestSpaceship
import TestSpaceshipPlanet


SCREEN_SIZE = (1240, 640)


class GameState:

    
    TITLE_SCREEN = 0
    NEW_GAME = 1
    
    TEST_PLANET = 2
    TEST_SPACESHIP = 3
    TEST_SPACEPLANET = 4
    
    def __init__(self, screen):
        self.state = self.TEST_SPACEPLANET
        
        self.scene = {}
        
        self.scene[self.TEST_PLANET] = TestPlanet.TestPlanet(screen)
        self.scene[self.TEST_SPACESHIP] = TestSpaceship.TestSpaceship(screen)
        self.scene[self.TEST_SPACEPLANET] = TestSpaceshipPlanet.TestSpaceshipPlanet(screen)
        
        if self.state == self.TITLE_SCREEN:
            self.title_screen = TitleScene.TitleScene(screen)
        
        
    
    def run(self, screen):
        if self.state == self.TITLE_SCREEN:
            self.title_screen.run(self)
        
        if self.state == self.NEW_GAME:
            pass
            
        self.scene[self.state].run()

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
        
        pygame.display.update()
         
         
    
    
if __name__ == "__main__":
    main()   


