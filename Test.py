import pygame
import random

# Define the Healthy class, which is a sprite:
class Healthy(pygame.sprite.Sprite):
    def __init__(self, group, all_sprites):
        super().__init__()
        self.original_image = pygame.image.load('Images_healthy/healthy.png')
        self.image = pygame.transform.scale(self.original_image, (35, 70))
        self.rect = self.image.get_rect()
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
        elif self.direction == "up" and self.rect.top > 0:
            # Update the rect to move the sprite up
            self.rect.move_ip(0, -1)
        elif self.direction == "left" and self.rect.left > 0:
            # Update the rect to move the sprite left
            self.rect.move_ip(-1, 0)
        elif self.direction == "right" and self.rect.right < 900:
            # Update the rect to move the sprite right
            self.rect.move_ip(1, 0)

        # Check for collisions with other sprites in the group
        collisions = pygame.sprite.spritecollide(self, self.all_sprites, False)
        if len(collisions) > 0 and collisions[0] != self:
            # Move the sprite in a random direction to try to avoid collisions
            self.rect.move_ip(random.randint(-10, 10), random.randint(-10, 10))
            # Check again for collisions with other sprites in the group
            collisions = pygame.sprite.spritecollide(self, self.group, False)
            if len(collisions) > 1: # There's still a collision, pause movement for a short duration
                self.rect.move_ip(random.randint(0, 1), random.randint(0, 1))

# Define the Game class
class Game:
    # Initialize the game
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Set up the screen
        self.screen = pygame.display.set_mode((800, 600))

        # Set up the font
        self.font = pygame.font.SysFont(None, 30)

        # Set up the buttons
        self.button = pygame.Rect(50, 50, 100, 50)
        self.button_quit = pygame.Rect(700, 550, 100, 50)

        # Set up the groups
        self.all_sprites = pygame.sprite.Group()
        self.healthy_group = pygame.sprite.Group()

        # Set up the counters
        self.health_count = 0

    # Run the game
    def run(self):
        running = True
        self.add_healthy = False

        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and self.button.collidepoint(event.pos):
                    self.add_healthy = True
                elif event.type == pygame.MOUSEBUTTONDOWN and self.button_quit.collidepoint(event.pos):
                    running = False

            # Add new Healthy objects if the button is clicked
            if self.add_healthy:
                new_healthy = Healthy(self.healthy_group, self.all_sprites)
                self.all_sprites.add(new_healthy)
                self.health_count += 1
                self.add_healthy = False
                self.healthy_group.add(new_healthy)

            # Update and draw all sprites
            self.all_sprites.update()
            self.all_sprites.draw(self.screen)

            # Update the screen
            self.screen.fill((255, 255, 255))
            pygame.draw.rect(self.screen, (0, 255, 0), self.button)

            # Draw the Healthy objects on the screen
            self.healthy_group.draw(self.screen)

            # Update the counters
            health_count_text = self.font.render(f"Healthy: {self.health_count}", True, (0, 0, 0))
            self.screen.blit(health_count_text, (50, 120))

            pygame.display.flip()

        # Quit the game when the loop ends
        pygame.quit()    

# Create a group for the Healthy objects
healthy_group = pygame.sprite.Group()

game = Game()
game.run()