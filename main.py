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
        
        self.radius = radius
        self.mass = 10000
        
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        self.image.fill(background) 
        
        pygame.draw.circle(self.image, color, [radius, radius], radius)
        
        self.mask = pygame.mask.from_surface(self.image)
        
        self.rect = self.image.get_rect(center=position)
        
    
    def blit(self, surface):
        surface.blit(self.image, self.rect)
        
    def get_pos(self):
        return pygame.Vector2(self.rect.center)
        
        
                


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


class Spaceship(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        
        self.radius = 30
        self.mass = 1
        self.center = pygame.Vector2(self.radius, self.radius)
        self.size = pygame.Vector2(self.radius*2, self.radius*2)
        color = "blue"
        
        self.direction = pygame.Vector2(0, 1)
        
        position = pygame.Vector2(SCREEN_SIZE) / 2
        
        # accelleration
        self.thrust_force = 1
        self.force = pygame.Vector2(0, 0)
        
        # image stuff
        self.image = pygame.Surface(self.size, pygame.SRCALPHA)
        
        
        
        pygame.draw.circle(self.image, color, self.center, self.radius)
        
        self.mask = pygame.mask.from_surface(self.image)
        
        self.original_image = self.image.copy()
        
        self.image.fill((10, 0, 0, 10))
        
        self.rect = self.image.get_rect(center=position)
        
        self.draw_dir()
    
    
    def draw_dir(self):
        self.image.blit(self.original_image, self.original_image.get_rect(topleft=(0, 0)))
        
        dir_image = pygame.Surface(self.size, pygame.SRCALPHA)
        start_pos = self.center
        end_pos = self.center + self.direction * (self.radius * (1 - 0.01))
        pygame.draw.line(dir_image, "green", start_pos, end_pos)
        
        dir_rect = dir_image.get_rect(topleft=(0,0))

        self.image.blit(dir_image, dir_rect)  
        
    def reset_force(self):
        self.force = pygame.Vector2(0, 0)
        
    def borders(self, screen):
        pos = pygame.Vector2(self.rect.center)
        
        if pos.x - self.radius < 0:
            self.rect.center = (self.radius, pos.y)
            self.reset_force()
        
        if pos.x > screen.get_width() - self.radius:
            self.rect.center =  (screen.get_width() - self.radius, pos.y)
            self.reset_force()
        
        if pos.y - self.radius < 0:
            self.rect.center = (pos.x, self.radius)
            self.reset_force()
         
        if pos.y > screen.get_height() - self.radius:
            self.rect.center = (pos.x, screen.get_height() - self.radius)
            self.reset_force()
            
    
    def change_dir(self):
        if pygame.key.get_pressed()[pygame.K_a]:
            self.direction = self.direction.rotate(-10) 
            self.draw_dir()

        if pygame.key.get_pressed()[pygame.K_d]:
            self.direction = self.direction.rotate(+10) 
            self.draw_dir()  
   
   
    def calc_forces(self, planet_list):
        for planet in planet_list:
            d = (planet.get_pos() - self.get_pos()).magnitude()
            g = 1
            
            print("distance to planet", d)
            
            force_dir = planet.get_pos() - self.get_pos()
            force_dir.normalize_ip()
            
            self.force += force_dir * (g * (planet.mass * self.mass) / d**2)
        
        print("force on the spaceship:", self.force)
        
        
    def move(self):
        
            
        acceleration = self.force
        dt = 1
        delta_pos = (acceleration * (dt ** 2))
            
            
        self.rect.center += delta_pos
             
        if pygame.key.get_pressed()[pygame.K_w]:
            self.force += self.thrust_force * self.direction
    
    def get_pos(self):
        return pygame.Vector2(self.rect.center)

                  

def test_spaceship(screen, spaceship):
    spaceship.change_dir()
    spaceship.move()
    spaceship.borders(screen)
    
    sp_spaceship = pygame.sprite.Group()
    sp_spaceship.add(spaceship)
    
    sp_spaceship.draw(screen)    
    

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
    
    

    def __init__(self):
        self.state = self.TEST_SPACEPLANET
        
        if self.state == self.TEST_SPACESHIP:
            self.spaceship = Spaceship()
        
        if self.state == self.TEST_SPACEPLANET:
            test_spaceship_planet_init(self)
        
    
    def run(self, screen):
        if self.state == self.TITLE_SCREEN:
            title_screen_scene(screen, self)
        
        if self.state == self.NEW_GAME:
            pass
            
        if self.state == self.TEST_PLANET:
            test_planet(screen)
        
        if self.state == self.TEST_SPACESHIP:
            test_spaceship(screen, self.spaceship)
        
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


