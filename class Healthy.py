import random

class Healthy:
    def __init__(self):
        self.x = 0 # starting x position
        self.y = 0 # starting y position
        self.animation_index = 0 # Starting animation index
        self.animation_frames = [
            # List of 3 images for each animation direction
            ["running_up_1.png", "running_up_2.png", "running_up_3.png"],
            ["running_down_1.png", "running_down_2.png", "running_down_3.png"],
            ["running_left_1.png", "running_left_2.png", "running_left_3.png"],
            ["running_right_1.png", "running_right_2.png", "running_right_3.png"]
        ]
        
    def move_randomly(self): # Randomly moves character by one unit in x or y
        dx = random.choice([-1, 0, 1])
        dy = random.choice([-1, 0, 1])
        self.x += dx
        self.y += dy
    
    def animate(self): # Displays the animation frame of the character
        animation_frame = self.animation_frames[self.animation_index]
        for row in animation_frame:
            print(''.join(row))
        self.animation_index = (self.animation_index + 1) % len(self.animation_frames)
    
    def run(self): # Calls the move_randomly and animate methods in loop, so the character seems to move around.
        while True:
            self.move_randomly()
            self.animate()
