# Game class

# Import necessary libraries
import pygame
import sys
import random 

# Define the game class
class Game:
    # Initialize the game
    def __init__(self):
        # Initialize pygame
        pygame.init()
        # Set screen dimensions
        self.screen_width = 640
        self.screen_height = 480

        # Set the screen and clock
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.fps = 60

        # Set initial health count and create a sprite group for all sprites
        self.health_count = 0
        self.infected_count = 0
        self.all_sprites = pygame.sprite.Group()

        # Create a button for adding healthy objects and set its text
        self.button = pygame.Rect(10, 420, 120, 40)
        self.button_text = pygame.font.SysFont('Arial' , 24).render('Add Healthy', True, (255, 255, 255))
        self.add_healthy = False

        self.button_infected = pygame.Rect(200, 420, 120, 40)
        self.button_infected_text = pygame.font.SysFont('Arial' , 24).render('Add Infected', True, (255, 255, 255))
        self.add_infected = False

    # Run the game
    def run(self):
        running = True
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # If the mouse button is clicked on the button, add a new Healthy object
                elif event.type == pygame.MOUSEBUTTONDOWN and self.button.collidepoint(event.pos):
                    self.add_healthy = True

                elif event.type == pygame.MOUSEBUTTONDOWN and self.button.collidepoint(event.pos):
                    self.add_infected = True

# def add() ?
            if self.add_healthy:
                new_healthy = Healthy()
                self.add.sprites.add(new_healthy)
                self.health_count += 1
                self.add_healthy = False
            
            if self.add_infected:
                new_infected = Infected()
                self.add.sprites.add(new_infected)
                self.infected_count += 1
                self.add_infected = False

            # Clear the screen
            self.screen.fill((255, 255, 255))

            # BUTTONS #
            # Draw the button and health count
            pygame.draw.rect(self.screen, (128, 128, 128), self.button)
            self.screen.blit(self.button_text, (17, 422, 120, 40))
            health_count_text = pygame.font.SysFont('Arial', 24).render(f'Health Count: {self.health_count}', True, (0, 0, 0))
            self.screen.blit(health_count_text, (self.screen_width - health_count_text.get_width() - 10, 10))

            # Draw the button and health count
            pygame.draw.rect(self.screen, (128, 128, 128), self.button)
            self.screen.blit(self.button_text, (17, 422, 120, 40))
            infected_count_text = pygame.font.SysFont('Arial', 24).render(f'Infected Count: {self.infected_count}', True, (0, 0, 0))
            self.screen.blit(infected_count_text, (self.screen_width - infected_count_text.get_width() - 10, 40))

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
    def init(self):
        super().init()
        # Load the images for the animations
        self.animation_frames = {
        'up': [pygame.image.load("running_up_1.png"), pygame.image.load("running_up_2.png"), pygame.image.load("running_up_3.png")],
        'down': [pygame.image.load("running_down_1.png"), pygame.image.load("running_down_2.png"), pygame.image.load("running_down_3.png")],
        'left': [pygame.image.load("running_left_1.png"), pygame.image.load("running_left_2.png"), pygame.image.load("running_left_3.png")],
        'right': [pygame.image.load("running_right_1.png"), pygame.image.load("running_right_2.png"), pygame.image.load("running_right_3.png")],
        }
        self.direction = 'down' # Set the initial direction
        self.animation_index = 0 # Starting animation index
        self.image = self.animation_frames[self.direction][self.animation_index] # Set the initial image
        self.rect = self.image.get_rect() # Set the rect for the sprite

        # Set the initial position of the Healthy object
        self.rect.x = 0 # starting x position
        self.rect.y = 0 # starting y position
        
    def move_randomly(self): # Randomly moves character by one unit in x or y
        dx = random.choice([-1, 0, 1])
        dy = random.choice([-1, 0, 1])
        self.rect.x += dx
        self.rect.y += dy

    # Update the Healthy object
    def update(self):
        # Move the Healthy object randomly
        self.move_randomly()

        # Animate the Healthy object
        self.animation_index = (self.animation_index + 1) % len(self.animation_frames[self.direction])
        self.image = self.animation_frames[self.direction][self.animation_index]

    def run(self): # Calls the move_randomly and animate methods in loop, so the character seems to move around.
        while True:
            self.move_randomly()
            self.animate()

# Define the infected class, which is a sprite:
class Infected(pygame.sprite.Sprite):
# Initialize the Healthy object
    def init(self):
        super().init()
        # Load the images for the animations
        self.animation_frames = {
        'up': [pygame.image.load("running_up_1.png"), pygame.image.load("running_up_2.png"), pygame.image.load("running_up_3.png")],
        'down': [pygame.image.load("running_down_1.png"), pygame.image.load("running_down_2.png"), pygame.image.load("running_down_3.png")],
        'left': [pygame.image.load("running_left_1.png"), pygame.image.load("running_left_2.png"), pygame.image.load("running_left_3.png")],
        'right': [pygame.image.load("running_right_1.png"), pygame.image.load("running_right_2.png"), pygame.image.load("running_right_3.png")],
        }
        self.direction = 'down' # Set the initial direction
        self.animation_index = 0 # Starting animation index
        self.image = self.animation_frames[self.direction][self.animation_index] # Set the initial image
        self.rect = self.image.get_rect() # Set the rect for the sprite

        # Set the initial position of the Infected object
        self.rect.x = 0 # starting x position
        self.rect.y = 0 # starting y position
        
    def move_randomly(self): # Randomly moves character by one unit in x or y
        dx = random.choice([-1, 0, 1])
        dy = random.choice([-1, 0, 1])
        self.rect.x += dx
        self.rect.y += dy

    # Update the Infected object
    def update(self):
        # Move the Infected object randomly
        self.move_randomly()

        # Animate the Infected object
        self.animation_index = (self.animation_index + 1) % len(self.animation_frames[self.direction])
        self.image = self.animation_frames[self.direction][self.animation_index]

    def run(self): # Calls the move_randomly and animate methods in loop, so the character seems to move around.
        while True:
            self.move_randomly()
            self.animate()

game = Game()
game.run()