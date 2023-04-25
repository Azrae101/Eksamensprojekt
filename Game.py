# Game class #
# Import necessary libraries
import pygame
import sys
import random
import os

# Import other python programmes
from Healthy import Healthy
from Infected import Infected
from Immune import Immune

# Definitions
characters = 0

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
        self.dead_count = 0
        self.point_count = 0
        self.all_sprites = pygame.sprite.Group()

        # Creates spawn window
        self.spawn = pygame.Rect(self.screen_width - 1140, self.screen_height - 680, 920, 575) # box position

        # Create a button for adding healthy objects and set its text
        self.button = pygame.Rect(self.screen_width - 1120, self.screen_height - 100, 280, 90) # box position
        self.button_text = pygame.font.SysFont('Concolas' , 35).render('ADD HEALTHY', True, (106, 168, 79))
        self.add_healthy = False

        # Create a button for adding infected objects and set its text
        self.button_infected = pygame.Rect(self.screen_width - 820, self.screen_height - 100, 280, 90) # box position
        self.button_infected_text = pygame.font.SysFont('Concolas' , 35).render('ADD INFECTED', True, (204, 0, 0))
        self.add_infected = False

        # Create a button for adding vaccinated objects and set its text
        self.button_vaccinated = pygame.Rect(self.screen_width - 520, self.screen_height - 100, 280, 90) # box position
        self.button_vaccinated_text = pygame.font.SysFont('Concolas' , 35).render('ADD VACCINATED', True, (61, 133, 198))
        self.add_vaccinated = False

        # Settings
        self.button_dead = pygame.Rect(self.screen_width - 218, self.screen_height - 100, 200, 42) # box position
        self.button_dead_text = pygame.font.SysFont('Concolas' , 30).render('DEAD', True, (255, 255, 255))
        #self.add_settings = False

        # Dead
        self.button_settings = pygame.Rect(self.screen_width - 218, self.screen_height - 100, 200, 42) # box position
        self.button_settings_text = pygame.font.SysFont('Concolas' , 30).render('SETTINGS', True, (255, 255, 255))
        #self.add_settings = False

        # Quit
        self.button_quit = pygame.Rect(self.screen_width - 218, self.screen_height - 52, 200, 42) # box position
        self.button_quit_text = pygame.font.SysFont('Concolas', 30).render('QUIT', True, (255, 255, 255))
        #self.add_quit = False

        # Points
        self.button_points = pygame.Rect(self.screen_width - 218, self.screen_height - 616, 200, 270) # box position
        self.button_points_text = pygame.font.SysFont('Concolas', 35).render('POINTS', True, (40, 40, 40))
        self.button_pointcounter_text = pygame.font.SysFont('Concolas', 50).render(f'{self.point_count}', True, (255, 255, 255))
        
        # Count
        self.button_count = pygame.Rect(self.screen_width - 218, self.screen_height - 660, 200, 42) # box position
        self.button_count_text = pygame.font.SysFont('Concolas', 35).render('COUNT', True, (255, 255, 255))

    # Run the game
    def run(self):
        running = True
        characters = 0
        while running:
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
                elif event.type == pygame.MOUSEBUTTONDOWN and self.button_quit.collidepoint(event.pos):
                    pygame.quit
                    quit()

            if self.add_healthy and characters < 50:
                new_healthy = Healthy()
                self.all_sprites.add(new_healthy)
                self.health_count += 1
                self.add_healthy = False

            if self.add_infected and characters < 50:
                new_infected = Infected()
                self.all_sprites.add(new_infected)
                self.infected_count += 1
                self.add_infected = False

            if self.add_vaccinated and characters < 50:
                new_vaccinated = Immune()
                self.all_sprites.add(new_vaccinated)
                self.vaccinated_count += 1
                self.add_vaccinated = False

            # Counting characters:
            characters = self.health_count + self.infected_count + self.vaccinated_count

            # Clear the screen
            self.screen.fill((255, 255, 255))

            # BUTTONS #
            # Draw the background for the counts & points button + point count and circle.
            pygame.draw.rect(self.screen, (50, 50, 50), self.button_points)
            # Points circle
            pygame.draw.circle(self.screen, (160, 0, 0), (self.screen_width - 118, self.screen_height - 205), 75)
            self.screen.blit(self.button_pointcounter_text, (self.screen_width - 128, self.screen_height - 220)) # Moves button text
            self.screen.blit(self.button_points_text, (self.screen_width - 165, self.screen_height - 320)) # Moves button text

            # Draw spawn_window
            pygame.draw.rect(self.screen, (253, 253, 253), self.spawn) 

            # Draw the healthy button and health count
            pygame.draw.rect(self.screen, (255, 255, 255), self.button) 
            self.screen.blit(self.button_text, (self.screen_width - 1062, self.screen_height - 70)) # Moves button text
            health_count_text = pygame.font.SysFont('Concolas', 32).render(f'HEALTHY:     ', True, (255, 255, 255))
            self.screen.blit(health_count_text, (self.screen_width - health_count_text.get_width() - 70, 95)) # Moves count text
            # count 
            health_count_text = pygame.font.SysFont('Concolas', 35).render(f'{self.health_count}', True, (255, 255, 255))
            self.screen.blit(health_count_text, (self.screen_width - health_count_text.get_width() - 30, 95)) # Moves count text
            
            # makes borders
            for i in range(4):
                pygame.draw.rect(self.screen, (0,0,0), (self.screen_width - 1100 -i,self.screen_height - 100 -i,260,85), 1)

            # Draw the infected button and infected count
            pygame.draw.rect(self.screen, (255, 255, 255), self.button_infected)
            self.screen.blit(self.button_infected_text, (self.screen_width - 772, self.screen_height - 70)) # Moves button text
            infected_count_text = pygame.font.SysFont('Concolas', 32).render(f'INFECTED:    ', True, (255, 255, 255))
            self.screen.blit(infected_count_text, (self.screen_width - infected_count_text.get_width() - 69, 155)) # Moves count text
            # count
            infected_count_text = pygame.font.SysFont('Concolas', 35).render(f'{self.infected_count}', True, (255, 255, 255))
            self.screen.blit(infected_count_text, (self.screen_width - infected_count_text.get_width() - 30, 155)) # Moves count text

            # makes borders
            for i in range(4):
                pygame.draw.rect(self.screen, (0,0,0), (self.screen_width - 810 -i,self.screen_height - 100 -i,260,85), 1)

            # Draw the vaccinated button and vaccinated count
            pygame.draw.rect(self.screen, (255, 255, 255), self.button_vaccinated)
            self.screen.blit(self.button_vaccinated_text, (self.screen_width - 498, self.screen_height - 70)) # Moves button text
            vaccinated_count_count_text = pygame.font.SysFont('Concolas', 32).render(f'VACCINATED:      ', True, (255, 255, 255))
            self.screen.blit(vaccinated_count_count_text, (self.screen_width - vaccinated_count_count_text.get_width() - 26, 215)) # Moves count text
            #count
            vaccinated_count_count_text = pygame.font.SysFont('Concolas', 35).render(f'{self.vaccinated_count}', True, (255, 255, 255))
            self.screen.blit(vaccinated_count_count_text, (self.screen_width - vaccinated_count_count_text.get_width() - 30, 215)) # Moves count text
            # makes borders
            for i in range(4):
                pygame.draw.rect(self.screen, (0,0,0), (self.screen_width - 520 -i,self.screen_height - 100 -i,260,85), 1)
            
            # Draw dead 
            pygame.draw.rect(self.screen, (255, 255, 255), self.button_dead)
            dead_count_text = pygame.font.SysFont('Concolas', 32).render(f'DEAD:     ', True, (255, 255, 255))
            self.screen.blit(dead_count_text, (self.screen_width - dead_count_text.get_width() - 110, 275)) # Moves dead text
            # count
            dead_count_text = pygame.font.SysFont('Concolas', 35).render(f'{self.dead_count}', True, (255, 255, 255))
            self.screen.blit(dead_count_text, (self.screen_width - dead_count_text.get_width() - 30, 275)) # Moves dead text

            # Draw the settings button and settings 
            pygame.draw.rect(self.screen, (50, 50, 50), self.button_settings)
            self.screen.blit(self.button_settings_text, (self.screen_width - 174, self.screen_height - 90,)) # Moves button text

            # Draw the quit button and quit 
            pygame.draw.rect(self.screen, (50, 50, 50), self.button_quit)
            self.screen.blit(self.button_quit_text, (self.screen_width - 145, self.screen_height - 42)) # Moves button text

            # Draw the count button 
            pygame.draw.rect(self.screen, (20, 20, 20), self.button_count)
            self.screen.blit(self.button_count_text, (self.screen_width - 160, self.screen_height - 649)) # Moves button text

            # Update and draw all sprites
            self.all_sprites.update()
            self.all_sprites.draw(self.screen)

            # Update the Healthy objects
            healthy_group.update()
            healthy_group.draw(self.screen)

            # Update the Infected objects
            infected_group.update()
            infected_group.draw(self.screen)

            # Update the Immune objects
            immune_group.update()
            immune_group.draw(self.screen)

            # Update the screen
            pygame.display.flip()

            # Control the FPS
            self.clock.tick(self.fps)

# Create a group for the Healthy objects
healthy_group = pygame.sprite.Group()

# Create a group for the infected objects
infected_group = pygame.sprite.Group()

# Create a group for the immune objects
immune_group = pygame.sprite.Group()
            
# Create a game instance and run the game
game = Game()
game.run()
