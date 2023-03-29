import pygame
import os

# Initialize pygame
pygame.init()

# Get the full path to the images folder
image_folder = os.path.join(os.path.dirname(__file__), 'images')

# Load an image from the images folder
image_filename = 'running_down_1.png'
image_path = os.path.join(image_folder, image_filename)
image = pygame.image.load(image_path)

# Display the image
screen = pygame.display.set_mode((image.get_width(), image.get_height()))
screen.blit(image, (0, 0))
pygame.display.flip()

# Wait for user to close window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
