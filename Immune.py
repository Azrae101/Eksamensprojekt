import pygame
import random

# Define the healthy class, which is a sprite:
class Immune(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load('Images_vaccinated/immune1.png')
        self.image = pygame.transform.scale(self.original_image, (35, 70))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, 1090), random.randint(50, 630))
        self.image_list = [] # List to hold the different images
        
        self.image_list.append(self.image) # Add the first image to the list
        
        self.image_list.append(pygame.image.load('Images_vaccinated/immune1.png'))
        self.image_list.append(pygame.image.load('Images_vaccinated/immune2.png'))
        self.image_list.append(pygame.image.load('Images_vaccinated/immune3.png'))
        self.image_list.append(pygame.image.load('Images_vaccinated/immune4.png'))
        self.image_list.append(pygame.image.load('Images_vaccinated/immune5.png'))
        self.image_list.append(pygame.image.load('Images_vaccinated/immune6.png'))
        self.image_list.append(pygame.image.load('Images_vaccinated/immune7.png'))
        self.image_list.append(pygame.image.load('Images_vaccinated/immune8.png'))
        self.image_list.append(pygame.image.load('Images_vaccinated/immune9.png'))
        self.image_list.append(pygame.image.load('Images_vaccinated/immune10.png'))
        self.image_list.append(pygame.image.load('Images_vaccinated/immune11.png'))
        self.image_list.append(pygame.image.load('Images_vaccinated/immune12.png'))

        self.image_index = 0 # Index of the current image in the list
        self.animation_speed = 10 # How many game frames per image change
        self.frame_count = 0 # Counter for the current frame in the animation

    def update(self):
        # Update the frame count
        self.frame_count += 1
        if self.frame_count >= self.animation_speed:
            self.frame_count = 0
            self.image_index += 1
            if self.image_index >= len(self.image_list):
                self.image_index = 0
            self.image = self.image_list[self.image_index]