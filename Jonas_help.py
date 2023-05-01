import pygame as pg
import time

class Player(pg.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.rect = pg.Rect(x,y,50,50)
        self.color = (20,20,200)
        self.image = pg.Surface((50,50))
        self.image.fill(self.color)

    def update(self):
        self.rect.x += 10
        if self.rect.x > 600:
            self.rect.x = 0

        self.image.fill(self.color)

class Box(pg.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.rect = pg.Rect(x,y,100,100)
        self.color = (20,200,20)
        self.original_color = self.color
        self.image = pg.Surface((100,100))
        self.image.fill(self.color)

    def update(self):
        self.image.fill(self.color)

pg.init()

screen = pg.display.set_mode((600,600))

all_sprites = pg.sprite.Group()
box_sprites = pg.sprite.Group()

for i in range(4):
    b = Box(i*120+50, 75)
    all_sprites.add(b)
    box_sprites.add(b)

player = Player(100,100)
all_sprites.add(player)

running=True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running=False
    screen.fill((0,0,0))

    box_cols = pg.sprite.spritecollide(player,box_sprites, False)
    if box_cols:
        print("Colliding!!!", box_cols)
    for box in box_sprites:
        if box in box_cols:
            box.color = (200,20,20)
        else: # To make the boxes go back to the original color
            box.color = box.original_color

    #print(f"Colliding with {len(box_cols)} box(es)")

    all_sprites.update()
    all_sprites.draw(screen)

    pg.display.flip()
    time.sleep(0.1)
