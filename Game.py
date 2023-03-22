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
        self.all_sprites = pygame.sprite.Group()

        # Create a button for adding healthy objects and set its text
        self.button = pygame.Rect(10, 420, 120, 40)
        self.button_text = pygame.font.SysFont('Arial' , 24).render('Add Healthy', True, (255, 255, 255))

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
                    # Add a new Healthy object
                    new_healthy = Healthy 
                    self.all_sprites.add(new_healthy)
                    self.health_count += 1

            # Clear the screen
            self.screen.fill((0, 0, 0))

            # Draw the button and health count
            pygame.draw.rect(self.screen, (128, 128, 128), self.button)
            self.screen.blit(self.button_text, (17, 422, 120, 40))
            health_count_text = pygame.font.SysFont('Arial', 24).render(f'Health Count: {self.health_count}', True, (255, 255, 255))
            self.screen.blit(health_count_text, (self.screen_width - health_count_text.get_width() - 10, 10))

            # Update and draw all sprites
            self.all_sprites.update()
            self.all_sprites.draw(self.screen)

            # Update the screen
            pygame.display.flip()

            # Control the FPS
            self.clock.tick(self.fps)


# Define the healthy class, which is a sprite:
class Healthy:
    # Initialize the Healthy object
    def __init__(self):
        self.x = 0 # starting x position
        self.y = 0 # starting y position
        self.animation_index = 0 # Starting animation index
        self.animation_frames = [

        # Set the image and rect for the Healthy object
            # List of 3 images for each animation direction
            ["running_up_1.png", "running_up_2.png", "running_up_3.png"],
            ["running_down_1.png", "running_down_2.png", "running_down_3.png"],
            ["running_left_1.png", "running_left_2.png", "running_left_3.png"],
            ["running_right_1.png", "running_right_2.png", "running_right_3.png"]
        ]
        
    def move_randomly(self): # Randomly moves character by one unit in x or y
        dx = random.choice([-1, 0, 1])
        dy = random.choice([-1, 0, 1])
        self.x += dx
        self.y += dy
    
    # Update the Healthy object
    def animate(self): # Displays the animation frame of the character
        # Move the Healthy object randomly
        animation_frame = self.animation_frames[self.animation_index]
        for row in animation_frame:
            print(''.join(row))
        self.animation_index = (self.animation_index + 1) % len(self.animation_frames)
    
    def run(self): # Calls the move_randomly and animate methods in loop, so the character seems to move around.
        while True:
            self.move_randomly()
            self.animate()


# Create and run the game
game = Game()
game.run()
