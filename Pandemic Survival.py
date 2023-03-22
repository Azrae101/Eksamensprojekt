# Survive the digital pandemic
# Programmering B, eksamensprojekt

import pygame
import sys
import random

class Game: 
	def __init__(self): 
		pygame.init() 
		self.screen_width = 640 
		self.screen_height = 480
		self.screen = pygame.display.set_mode((self.screen_width, self.screen_height)) 
		self.clock = pygame.time.Clock() 
		self.fps = 60 
		self.health_count = 0 
		self.all_sprites = pygame.sprite.Group() 

# Create a button 
		self.button = pygame.Rect(50, 50, 100, 50) 
		self.button_text = pygame.font.SysFont('Arial', 24).render('Add Healthy', True, (255, 255, 255)) 

def run(self): 
	running = True 
	while running: 
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT: 
				running = False 
			elif event.type == pygame.MOUSEBUTTONDOWN and self.button.collidepoint(event.pos): 

# Add a new Healthy object 
	new_healthy = Healthy() 
	self.all_sprites.add(new_healthy) 
	self.health_count += 1 

# Draw the button and health count 
	pygame.draw.rect(self.screen, (0, 0, 255), self.button)
	self.screen.blit(self.button_text, self.button.center) 
	health_count_text = pygame.font.SysFont('Arial', 24).render(f'Health Count: {self.health_count}', True, (255, 255, 255)) 
	self.screen.blit(health_count_text, (self.screen_width - health_count_text.get_width() - 10, 10))

# Update and draw all sprites 
	self.all_sprites.update() 
	self.all_sprites.draw(self.screen) 

	pygame.display.flip() 
	self.clock.tick(self.fps) 

class Healthy(pygame.sprite.Sprite): 
	def __init__(self): 
		super().__init__() 
		self.image = pygame.Surface((30, 30)) 
		self.image.fill((0, 255, 0)) 
		self.rect = self.image.get_rect() 
		self.rect.center = (random.randint(0, 640), random.randint(0, 480)) def update(self): 
		self.rect.move_ip(random.randint(-5, 5), random.randint(-5, 5)) 

game = Game() 
game.run()
