import pygame
import random

# Define the healthy class, which is a sprite:
class Healthy(pygame.sprite.Sprite):
    def __init__(self, spawn_rect):
        super().__init__()
        self.original_image = pygame.image.load('Images_healthy/healthy.png')
        self.image = pygame.transform.scale(self.original_image, (35, 70))
        self.rect = self.image.get_rect()
        self.spawn_rect = spawn_rect
        # placement
        self.rect.center = (random.randint(self.spawn_rect.left, self.spawn_rect.right), random.randint(self.spawn_rect.top, self.spawn_rect.bottom))
        self.image_list = [] # List to hold the different images
        
        self.image_list.append(self.image) # Add the first image to the list
        
        self.image_list_down = [] # List to hold the different images for running down
        self.image_list_up = [] # List to hold the different images for running up
        self.image_list_left = [] # List to hold the different images for running left
        self.image_list_right = [] # List to hold the different images for running right

        # Running down:
        for i in range(1, 4):
            self.image_list_down.append(pygame.image.load(f'Images_healthy/healthy{i}.png'))

        # Running up:
        for i in range(10, 13):
            self.image_list_up.append(pygame.image.load(f'Images_healthy/healthy{i}.png'))

        # Running left:
        for i in range(4, 7):
            self.image_list_left.append(pygame.image.load(f'Images_healthy/healthy{i}.png'))

        # Running right:
        for i in range(7, 10):
            self.image_list_right.append(pygame.image.load(f'Images_healthy/healthy{i}.png'))


        self.direction = "down" # Default direction

    def update(self):
        # Randomly change the direction of the sprite
        if random.random() < 0.05: # 5% chance to change direction
            directions = ["up", "down", "left", "right"]
            directions.remove(self.direction) # Remove current direction
            self.direction = random.choice(directions) # Choose a new direction at random
        if self.direction == "down":
            # Update the rect to move the sprite down
            self.rect.move_ip(0, 1)
            # Check if the sprite has moved out of the spawn box and move it back in if it has
            if not self.spawn_rect.contains(self.rect):
                self.rect.bottom = self.spawn_rect.bottom
        elif self.direction == "up":
            # Update the rect to move the sprite up
            self.rect.move_ip(0, -1)
            # Check if the sprite has moved out of the spawn box and move it back in if it has
            if not self.spawn_rect.contains(self.rect):
                self.rect.top = self.spawn_rect.top
        elif self.direction == "left":
            # Update the rect to move the sprite left
            self.rect.move_ip(-1, 0)
            # Check if the sprite has moved out of the spawn box and move it back in if it has
            if not self.spawn_rect.contains(self.rect):
                self.rect.left = self.spawn_rect.left
        elif self.direction == "right":
            # Update the rect to move the sprite right
            self.rect.move_ip(1, 0)
            # Check if the sprite has moved out of the spawn box and move it back in if it has
            if not self.spawn_rect.contains(self.rect):
                self.rect