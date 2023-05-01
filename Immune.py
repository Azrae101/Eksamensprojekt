import pygame
import random

# Define the healthy class, which is a sprite:
class Immune(pygame.sprite.Sprite):
    def __init__(self, group, all_sprites):
        super().__init__()
        self.original_image = pygame.image.load('Images_vaccinated/immune.png')
        self.image = pygame.transform.scale(self.original_image, (35, 70))
        self.rect = self.image.get_rect(topleft=(random.randint(50, 900), random.randint(50, 500)))
        #self.rect.center = (random.randint(50, 1090), random.randint(50, 630))
        self.image_list = [] # List to hold the different images
        
        self.image_list.append(self.image) # Add the first image to the list
        
        self.image_list_down = [] # List to hold the different images for running down
        self.image_list_up = [] # List to hold the different images for running up
        self.image_list_left = [] # List to hold the different images for running left
        self.image_list_right = [] # List to hold the different images for running right

        # Running down:
        for i in range(1, 4):
            self.image_list_down.append(pygame.image.load(f'Images_vaccinated/immune{i}.png'))

        # Running up:
        for i in range(10, 13):
            self.image_list_up.append(pygame.image.load(f'Images_vaccinated/immune{i}.png'))

        # Running left:
        for i in range(4, 7):
            self.image_list_left.append(pygame.image.load(f'Images_vaccinated/immune{i}.png'))

        # Running right:
        for i in range(7, 10):
            self.image_list_right.append(pygame.image.load(f'Images_vaccinated/immune{i}.png'))
        self.group = group
        self.all_sprites = all_sprites
        self.reset_position()

    def reset_position(self):
        # Set the initial position of the sprite randomly within the game window
        x = random.randint(0, 800 - self.rect.width)
        y = random.randint(0, 600 - self.rect.height)
        self.rect.topleft = (x, y)

        # Check for collisions with other sprites
        attempts = 0
        while pygame.sprite.spritecollide(self, self.all_sprites, False) and attempts < 10:
            self.rect.move_ip(random.randint(1, 5), random.randint(1, 5))
            attempts += 1

        self.direction = "down" # Default direction

    def update(self):
        # Randomly change the direction of the sprite
        if random.random() < 0.05: # 5% chance to change direction
            directions = ["up", "down", "left", "right"]
            directions.remove(self.direction) # Remove current direction
            self.direction = random.choice(directions) # Choose a new direction at random
        if self.direction == "down" and self.rect.bottom < 550:
            # Update the rect to move the sprite down
            self.rect.move_ip(0, 1)
            # Animate the sprite's movement
            self.image = self.image_list_down[int(pygame.time.get_ticks() % 9 / 3)]
        elif self.direction == "up" and self.rect.top > 0:
            # Update the rect to move the sprite up
            self.rect.move_ip(0, -1)
            # Animate the sprite's movement
            self.image = self.image_list_up[int(pygame.time.get_ticks() % 9 / 3)]
        elif self.direction == "left" and self.rect.left > 0:
            # Update the rect to move the sprite left
            self.rect.move_ip(-1, 0)
            # Animate the sprite's movement
            self.image = self.image_list_left[int(pygame.time.get_ticks() % 9 / 3)]
        elif self.direction == "right" and self.rect.right < 900:
            # Update the rect to move the sprite right
            self.rect.move_ip(1, 0)
            # Animate the sprite's movement
            self.image = self.image_list_right[int(pygame.time.get_ticks() % 9 / 3)]
'''
        # Check for collisions with other sprites in the group
        collisions = pygame.sprite.spritecollide(self, self.all_sprites, False)
        if len(collisions) > 0 and collisions[0] != self:
            # Move the sprite in a random direction to try to avoid collisions
            print("Immune")
            # Check again for collisions with other sprites in the group
            collisions = pygame.sprite.spritecollide(self, self.group, False)
'''