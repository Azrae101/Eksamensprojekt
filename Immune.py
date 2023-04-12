import random

class Immune:
    def __init__(self, healthy):
        self.x = 0
        self.y = 0
        self.animation_index = 0
        self.animation_frames = [
            # Replace the placeholder values with your animation frames
            # Each frame should be a 3x3 matrix of characters representing the animation image
            [[' ', 'X', ' '],
             ['\\', '|', '/'],
             ['/', ' ', '\\']],
             
            [[' ', 'X', ' '],
             ['/', '|', '\\'],
             ['\\', ' ', '/']],
             
            [[' ', 'X', ' '],
             ['|', 'V', '|'],
             ['/', ' ', '\\']]
        ]
        self.healthy = healthy
    
    def move_randomly(self):
        dx = random.choice([-1, 0, 1])
        dy = random.choice([-1, 0, 1])
        self.x += dx
        self.y += dy
    
    def chase_healthy(self):
        if self.x < self.healthy.x:
            self.x += 1
        elif self.x > self.healthy.x:
            self.x -= 1
        if self.y < self.healthy.y:
            self.y += 1
        elif self.y > self.healthy.y:
            self.y -= 1
    
    def animate(self):
        animation_frame = self.animation_frames[self.animation_index]
        for row in animation_frame:
            print(''.join(row))
        self.animation_index = (self.animation_index + 1) % len(self.animation_frames)
        
