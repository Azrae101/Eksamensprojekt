import pygame
import random

# Define the Healthy class, which is a sprite:
class Healthy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load('Images_healthy/healthy.png')
        self.image = pygame.transform.scale(self.original_image, (35, 70))
        self.rect = self.image.get_rect(topleft=(random.randint(195, 200), random.randint(195, 200)))

# Define the Game class
class Game:
    # Initialize the game
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Set up the screen
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("My Game")

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
                new_healthy = Healthy()
                self.all_sprites.add(new_healthy)
                self.health_count += 1
                self.add_healthy = False
                self.healthy_group.add(new_healthy)
                ret = pygame.sprite.spritecollideany(new_healthy, self.healthy_group)
                print(ret)
                print(self.healthy_group.sprites())

                # if len(ret) > 1:
                #     new_healthy.kill()
                #     self.health_count -= 1

            # Update and draw all sprites
            self.all_sprites.update()
            self.all_sprites.draw(self.screen)

            # Update the Healthy objects
            healthy_group.update()
            healthy_group.draw(self.screen)

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
        quit()

# Create a group for the Healthy objects
healthy_group = pygame.sprite.Group()

game = Game()
game.run()
