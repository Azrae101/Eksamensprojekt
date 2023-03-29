# Game class

# Import necessary libraries
import pygame
import sys
import random
import os

# Define the game class
class Game:
    # Initialize the game
    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Layout
        # Set screen dimensions
        self.screen_width = 1140
        self.screen_height = 680

        # Set the screen and clock
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.fps = 60

        # Set initial health count and create a sprite group for all sprites
        self.health_count = 0
        self.infected_count = 0
        self.vaccinated_count = 0
        self.all_sprites = pygame.sprite.Group()

        # Create a button for adding healthy objects and set its text
        self.button = pygame.Rect(self.screen_width - 1120, self.screen_height - 100, 280, 90)
        self.button_text = pygame.font.SysFont('Concolas' , 35).render('ADD HEALTHY', True, (106, 168, 79))
        self.add_healthy = False

        # Create a button for adding infected objects and set its text
        self.button_infected = pygame.Rect(self.screen_width - 820, self.screen_height - 100, 280, 90)
        self.button_infected_text = pygame.font.SysFont('Concolas' , 35).render('ADD INFECTED', True, (204, 0, 0))
        self.add_infected = False

        # Create a button for adding vaccinated objects and set its text
        self.button_vaccinated = pygame.Rect(self.screen_width - 520, self.screen_height - 100, 280, 90)
        self.button_vaccinated_text = pygame.font.SysFont('Concolas' , 35).render('ADD VACCINATED', True, (61, 133, 198))
        self.add_vaccinated = False

        # Settings
        self.button_settings = pygame.Rect(self.screen_width - 218, self.screen_height - 100, 200, 42)
        self.button_settings_text = pygame.font.SysFont('Concolas' , 30).render('SETTINGS', True, (255, 255, 255))
        #self.add_settings = False

        # Quit
        self.button_quit = pygame.Rect(self.screen_width - 218, self.screen_height - 52, 200, 42)
        self.button_quit_text = pygame.font.SysFont('Concolas', 30).render('QUIT', True, (255, 255, 255))
        #self.add_quit = False

        # Count
        self.button_count = pygame.Rect(self.screen_width - 218, self.screen_height - 660, 200, 42)
        self.button_count_text = pygame.font.SysFont('Concolas', 30).render('COUNT', True, (255, 255, 255))
        #self.add_count = False

    # Run the game
    def run(self):
        running = True
        while running:

            # Get the full path to the images folder
            # image_folder = os.path.join(os.path.dirname(__file__), 'images')

            # Load images:
            # healthy_img = pygame.image.load(os.path.join(image_folder, "running_up_1.png"))

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # If the mouse button is clicked on the button, add a new Healthy or Infected object
                elif event.type == pygame.MOUSEBUTTONDOWN and self.button.collidepoint(event.pos):
                    self.add_healthy = True # Healthy button
                elif event.type == pygame.MOUSEBUTTONDOWN and self.button_infected.collidepoint(event.pos):
                    self.add_infected = True # Infected button
                elif event.type == pygame.MOUSEBUTTONDOWN and self.button_vaccinated.collidepoint(event.pos):
                    self.add_vaccinated = True # Vaccinated button

            if self.add_healthy:
                new_healthy = Healthy()
                self.all_sprites.add(new_healthy)
                self.health_count += 1
                self.add_healthy = False
                # print("healthy: " + str(self.health_count))

            if self.add_infected:
                new_infected = Infected()
                self.all_sprites.add(new_infected)
                self.infected_count += 1
                self.add_infected = False
                # print("infected: " + str(self.infected_count))

            if self.add_vaccinated:
                new_vaccinated = Vaccinated()
                self.all_sprites.add(new_vaccinated)
                self.vaccinated_count += 1
                self.add_vaccinated = False
                # print("vaccinated: " + str(self.vaccinated_count))

            # Clear the screen
            self.screen.fill((255, 255, 255))

            # BUTTONS #
            # Draw the healthy button and health count
            pygame.draw.rect(self.screen, (255, 255, 255), self.button)
            self.screen.blit(self.button_text, (self.screen_width - 1062, self.screen_height - 70)) # Moves button text
            health_count_text = pygame.font.SysFont('Concolas', 30).render(f'HEALTHY: {self.health_count}', True, (0, 0, 0))
            self.screen.blit(health_count_text, (self.screen_width - health_count_text.get_width() - 20, 140)) # Moves count text
            for i in range(4):
                pygame.draw.rect(self.screen, (0,0,0), (self.screen_width - 1100 -i,self.screen_height - 100 -i,260,85), 1)

            # Draw the infected button and infected count
            pygame.draw.rect(self.screen, (255, 255, 255), self.button_infected)
            self.screen.blit(self.button_infected_text, (self.screen_width - 772, self.screen_height - 70)) # Moves button text
            infected_count_text = pygame.font.SysFont('Concolas', 30).render(f'INFECTED: {self.infected_count}', True, (0, 0, 0))
            self.screen.blit(infected_count_text, (self.screen_width - infected_count_text.get_width() - 20, 140)) # Moves count text
            for i in range(4):
                pygame.draw.rect(self.screen, (0,0,0), (self.screen_width - 810 -i,self.screen_height - 100 -i,260,85), 1)

            # Draw the vaccinated button and vaccinated count
            pygame.draw.rect(self.screen, (255, 255, 255), self.button_vaccinated)
            self.screen.blit(self.button_vaccinated_text, (self.screen_width - 498, self.screen_height - 70)) # Moves button text
            vaccinated_count_count_text = pygame.font.SysFont('Concolas', 30).render(f'VACCINATED: {self.vaccinated_count}', True, (0, 0, 0))
            self.screen.blit(vaccinated_count_count_text, (self.screen_width - vaccinated_count_count_text.get_width() - 20, 140)) # Moves count text
            for i in range(4):
                pygame.draw.rect(self.screen, (0,0,0), (self.screen_width - 520 -i,self.screen_height - 100 -i,260,85), 1)

            # Draw the settings button and settings 
            pygame.draw.rect(self.screen, (50, 50, 50), self.button_settings)
            self.screen.blit(self.button_settings_text, (self.screen_width - 174, self.screen_height - 90,)) # Moves button text

            # Draw the quit button and quit 
            pygame.draw.rect(self.screen, (50, 50, 50), self.button_quit)
            self.screen.blit(self.button_quit_text, (self.screen_width - 145, self.screen_height - 42)) # Moves button text

            # Draw the settings button and count
            pygame.draw.rect(self.screen, (50, 50, 50), self.button_count)
            self.screen.blit(self.button_count_text, (self.screen_width - 150, self.screen_height - 648)) # Moves button text

            # Update and draw all sprites
            self.all_sprites.update()
            self.all_sprites.draw(self.screen)

            # Update the screen
            pygame.display.flip()

            # Control the FPS
            self.clock.tick(self.fps)

# Define the healthy class, which is a sprite:
class Healthy(pygame.sprite.Sprite):
# Initialize the Healthy object
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((50, 200, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, 1090), random.randint(50, 630))

# Define the infected class, which is a sprite:
class Infected(pygame.sprite.Sprite):
# Initialize the infected object
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((200, 50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, 1090), random.randint(50, 630))

# Define the Vaccinated class, which is a sprite:
class Vaccinated(pygame.sprite.Sprite):
# Initialize the Vaccinated object
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((50, 50, 200))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, 1090), random.randint(50, 630))
            
# Create a game instance and run the game
game = Game()
game.run()