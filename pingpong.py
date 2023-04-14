from pygame import *
from time import time as timer

# создай окно игры 700x500 с фоном картинкой
w, h = 700, 500

window = display.set_mode((w, h))
display.set_caption('Игра шутер')

class GameSprite(sprite.Sprite):
    def __init__(self, imagefile, x, y,  wide=65, hight=65, speed=5):
        super().__init__()
        self.image = transform.scale(image.load(imagefile), (wide,hight))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Roketki(GameSprite):
    def update_l(self):
        k = key.get_pressed()
        if k[K_a] and self.rect.y > 0:
            self.rect.y -= self.speed
        if k[K_z] and self.rect.y < h-80:
            self.rect.y += self.speed

    # копируем код def update_l
    def update_r(self):
        k = key.get_pressed()
        if k[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if k[K_DOWN] and self.rect.y < h-80:
            self.rect.y += self.speed

raketka1 = Roketki('roketka-l.png', 10, 20, 50, 80, 15)
raketka2 = Roketki('roketka-r.png', 640, 320, 50, 80, 15)
ball = GameSprite('ball.png', 300, 250)
ball.speed_x = ball.speed
ball.speed_y = ball.speed

font.init()
font1 = font.SysFont('Arial', 36)
lose1 = font1.render("Первый игрок (слева) проиграл!", 1, (255, 0, 0)) 
lose2 = font1.render("Второй игрок (справа) проигал!", 1, (255, 0, 0)) 

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    window.fill((0, 130, 144))
    raketka1.reset()
    raketka1.update_l()

    raketka2.reset()
    raketka2.update_r()

    ball.reset()
    if not finish:
        ball.rect.x += ball.speed_x
        ball.rect.y += ball.speed_y
    if ball.rect.y > h-65 or ball.rect.y < 0:
        ball.speed_y *= -1
    if sprite.collide_rect(ball, raketka2) or sprite.collide_rect(ball, raketka1):
        ball.speed_x *= -1

    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (100,200))

    if ball.rect.x > w-65:
        finish = True
        window.blit(lose2, (100,200))

    


    display.update()
    time.delay(15)
