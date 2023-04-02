from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, x=0, y=0, width=50, height=50):
        self.image = transform.scale(image.load(sprite_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

BG_COLOR = (255,255,255)

WIDTH = 600
HEIGHT = 400
FPS = 60

mw = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Ping pong')
mw.fill(BG_COLOR)

clock = time.Clock()
rum = True

while rum:

    for e in event.get():
        if e.type == QUIT:
            rum = False
    
    display.update()
    clock.tick(FPS)