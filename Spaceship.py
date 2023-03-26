import pygame

class Spaceship(pygame.sprite.Sprite):

    def __init__(self, initial_position):
        super().__init__()
        
        self.radius = 30
        self.mass = 1
        self.center = pygame.Vector2(self.radius, self.radius)
        self.size = pygame.Vector2(self.radius*2, self.radius*2)
        color = "blue"
        
        self.direction = pygame.Vector2(0, 1)
        
        position = initial_position
        
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
