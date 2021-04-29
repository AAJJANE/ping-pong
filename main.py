#ping pong game
#ping pong game

from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, w , h, x, y, img, speed):
       super().__init__()
       self.image = transform.scale(image.load(img), (w,h))
       self.speed = speed
       self.rect = self.image.get_rect()
       self.rect.x = x
       self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        k = key.get_pressed() # Получаем нажатую клавишу
        if k[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if k[K_s] and self.rect.y < w - 70:
            self.rect.y += self.speed

class Player1(GameSprite):
    def update(self):
        k = key.get_pressed() # Получаем нажатую клавишу
        if k[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if k[K_DOWN] and self.rect.y < w - 70:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        pass

w, h = 700, 500
display.set_caption("Shooter")
window = display.set_mode((w,h))
player = Ball(70, 70, 300, 50,"1.png", 10)
player1 = Player(30, 150, 30, 50,"6.png", 10)
player2 = Player1(30, 150, 650, 50,"6.png", 10)


bg = transform.scale(image.load("background.jpg"), (w,h))

run = True
while run :
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    window.blit(bg, (0,0))
    player.update()
    player.reset()

    player1.update()
    player1.reset()

    player2.update()
    player2.reset()

    display.update()

    time.delay(100)
