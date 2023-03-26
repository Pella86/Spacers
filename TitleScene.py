import pygame

def create_text(text, color, size, font, pos):
    font = pygame.font.SysFont(font, size)
    text_color = color
    text = font.render(text, True, text_color)
   
    text_rect = text.get_rect(midbottom=pos)
    
    return text, text_rect   


class TitleScene:
    
    def __init__(self, screen):
        half_screen_width = int(screen.get_width() / 2)
        
        self.screen = screen
        
        # Title
        pos_x = half_screen_width
        pos_y = int(self.screen.get_height() * 0.1)  
        
        self.title, self.title_rect = create_text("Spacers", "seagreen", 64, "UbuntuMono", (pos_x, pos_y))
        
          
        
        # New game button
        new_game_pos = (half_screen_width, int(screen.get_height() * 0.3))
        self.new_game_text, self.new_game_text_rect = create_text("New Game", "red", 32, "UbuntuMono", new_game_pos)

        
        self.new_game_frame = pygame.Surface(self.new_game_text_rect.size + pygame.Vector2(50, 40))
        self.new_game_frame.fill((200, 0, 0))
        self.new_game_frame_rect = self.new_game_frame.get_rect(center=self.new_game_text_rect.center)
        
         
    
    def run(self, game_state):
        if pygame.mouse.get_pressed() == (True, False, False):
            print("mouse pressed")
            if self.new_game_frame_rect.collidepoint(pygame.mouse.get_pos()):
                print("new game button pressed")
                game_state.state = game_state.NEW_GAME 
        
        # Draw Title
        self.screen.blit(self.title, self.title_rect) 
        
        # Draw New Game Button
        self.screen.blit(self.new_game_frame, self.new_game_frame_rect)
        self.screen.blit(self.new_game_text, self.new_game_text_rect)                


