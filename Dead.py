import pygame
import random

# Define the dead class, which is a sprite:
class Dead(pygame.sprite.Sprite):

    def __init__(self, group, all_sprites):
        super().__init__()
        self.original_image = pygame.image.load('Other Images/dead.png')
        self.image = pygame.transform.scale(self.original_image, (110, 90))
        self.rect = self.image.get_rect(topleft=(random.randint(100, 800), random.randint(100, 400)))
        self.group = group
        self.all_sprites = all_sprites
