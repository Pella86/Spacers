import pygame

import enum

SCREEN_SIZE = (1240, 640)


def create_text(text, color, size, font, pos):
    font = pygame.font.SysFont(font, size)
    text_color = color
    text = font.render(text, True, text_color)
   
    text_rect = text.get_rect(midbottom=pos)
    
    return text, text_rect   


def title_screen_scene(screen, game_state):
    pos_x = int(screen.get_width() / 2)
    pos_y = int(screen.get_height() * 0.1)
    
    title, title_rect = create_text("Spacers", "seagreen", 64, "UbuntuMono", (pos_x, pos_y))
    
    screen.blit(title, title_rect)
    
    # New game
    new_game_pos = (int(screen.get_width() / 2), int(screen.get_height() * 0.3))
    new_game_text, new_game_text_rect = create_text("New Game", "red", 32, "UbuntuMono", new_game_pos)
    
    
    
    new_game_frame = pygame.Surface(new_game_text_rect.size + pygame.Vector2(50, 40))
    new_game_frame.fill((200, 0, 0))
    new_game_frame_rect = new_game_frame.get_rect(center=new_game_text_rect.center)
    
    screen.blit(new_game_frame, new_game_frame_rect)
    screen.blit(new_game_text, new_game_text_rect)
    
    if pygame.mouse.get_pressed() == (True, False, False):
        print("mouse pressed")
        if new_game_frame_rect.collidepoint(pygame.mouse.get_pos()):
            print("new game button pressed")
            game_state.state = GameState.NEW_GAME
    


class Planet(pygame.sprite.Sprite):

    def __init__(self, radius, position, color, background=(0, 0, 0, 0)):
        super().__init__()
        
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        self.image.fill(background) 
        
        pygame.draw.circle(self.image, color, [radius, radius], radius)
        
        self.rect = self.image.get_rect(center=position)
        
    
    def blit(self, surface):
        surface.blit(self.image, self.rect)
        
        
                


def test_planet(screen):
    
    # draw a planet to the screen
    
    planet_radius = 200
    planet_position = pygame.Vector2(screen.get_size()) / 2
    planet_background = (255, 0, 0, 50)
    planet_color = "red"
    
    planet = Planet(planet_radius, planet_position, planet_color, planet_background)
    
    
    planet.blit(screen)
    
    planet_2 = Planet(planet_radius, planet_position * 2, planet_color)
    
    planet_2.blit(screen)
   


def test_spaceship(screen):
    
    spaceship_size = pygame.Vector2(100, 100)
    spaceship_color = "blue"
    spaceship_position = pygame.Vector2(SCREEN_SIZE) / 2
    
    spaceship_image = pygame.Surface(spaceship_size, pygame.SRCALPHA)
    spaceship_image.fill((10, 0, 0, 10))
    
    
    pygame.draw.circle(spaceship_image, spaceship_color, spaceship_size / 2, spaceship_size[0] / 2)
    
    screen.blit(spaceship_image, spaceship_image.get_rect(center=spaceship_position))
    
    if 
    

    
    
    
    
    
    
    


class GameState:

    
    TITLE_SCREEN = 0
    NEW_GAME = 1
    TEST_PLANET = 2
    TEST_SPACESHIP = 3
    
    

    def __init__(self):
        self.state = self.TITLE_SCREEN
    
    def run(self, screen):
        if self.state == self.TITLE_SCREEN:
            title_screen_scene(screen, self)
        
        if self.state == self.NEW_GAME:
            pass
            
        if self.state == self.TEST_PLANET:
            test_planet(screen)
        
        if self.state == self.TEST_SPACESHIP:
            test_spaceship(screen)
            

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
    game_state = GameState()
    
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


