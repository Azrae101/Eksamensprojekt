# Game class

# Import necessary libraries
import pygame
import sys
import random
import os # Used to load the images

# Initialize pygame
pygame.init()

# Get the full path to the images folder
image_folder = os.path.join(os.path.dirname(__file__), 'images')

# Load images for the player animation
player_images = {
    'up': [pygame.image.load(os.path.join(image_folder, "running_up_1.png")),
           pygame.image.load(os.path.join(image_folder, "running_up_2.png")),
           pygame.image.load(os.path.join(image_folder, "running_up_3.png"))],
    'down': [pygame.image.load(os.path.join(image_folder, "running_down_1.png")),
             pygame.image.load(os.path.join(image_folder, "running_down_2.png")),
             pygame.image.load(os.path.join(image_folder, "running_down_3.png"))],
    'left': [pygame.image.load(os.path.join(image_folder, "running_left_1.png")),
             pygame.image.load(os.path.join(image_folder, "running_left_2.png")),
             pygame.image.load(os.path.join(image_folder, "running_left_3.png"))],
    'right': [pygame.image.load(os.path.join(image_folder, "running_right_1.png")),
              pygame.image.load(os.path.join(image_folder, "running_right_2.png")),
              pygame.image.load(os.path.join(image_folder, "running_right_3.png"))]
}

# Initialize game variables
player_animation = player_images['down']
player_frame = 0
player_image = player_animation[player_frame]
screen = pygame.display.set_mode((player_image.get_width(), player_image.get_height()))

# Set up the clock
clock = pygame.time.Clock()
FPS = 10

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update player animation
    player_frame = (player_frame + 1) % len(player_animation)
    player_image = player_animation[player_frame]

    # Redraw screen
    screen.fill((0, 0, 0)) # Fill screen with black
    screen.blit(player_image, (0, 0)) # Draw player image
    pygame.display.flip() # Update display

    # Limit the framerate
    clock.tick(FPS)
