from pygame import *
from random import randint

window = display.set_mode((700, 500))
BG_COLOR = (30, 240, 255)

class GameSprite(sprite.Sprite):
    def __init__(self, x, y, w, h, speed, image_name):
        self.img = image.load(image_name)
        self.img = transform.scale(self.img, (w, h))
        self.rect = Rect(x, y, w, h)
        self.speed_x = speed
        self.speed_y = speed

    def draw(self):
         window.blit(self.img, (self.rect.x, self.rect.y))

class Ball(GameSprite):
    def draw(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y+30 >= 500:
            self.speed_y *= -1
            BG_COLOR = (randint(0, 255), randint(0, 255), randint(0, 255))
        if self.rect.x+30 >= 700:
            self.speed_x *= -1
            BG_COLOR = (randint(0, 255), randint(0, 255), randint(0, 255))
        if self.rect.y < 0:
            self.speed_y *= -1
            BG_COLOR = (randint(0, 255), randint(0, 255), randint(0, 255))
        if self.rect.x < 0:
            self.speed_x *= -1
            BG_COLOR = (randint(0, 255), randint(0, 255), randint(0, 255))
        super().draw()

class Player(GameSprite):
    def __init__(self, x, y, w, h, speed, image_name, k_up, k_down):
        super().__init__(x, y, w, h, speed, image_name)
        self.k_up = k_up
        self.k_down = k_down

    def draw(self):
        key_pressed = key.get_pressed()
        if key_pressed[self.k_up]:
            self.rect.y -= self.speed_y
        elif key_pressed[self.k_down]:
            self.rect.y += self.speed_y
        super().draw()

ball = Ball(50, 50, 30, 30, 3, "ball.png")
player1 = Player(10, 200, 20, 100, 5, "player.png", K_w, K_s)
player2 = Player(670, 200, 20, 100, 5, "player.png", K_UP, K_DOWN)

clock = time.Clock()
game = True
while game:
    clock.tick(60)

    for e in event.get():
        if e.type == QUIT:
            game = False
        
    # Правила

    # Отрисовка    
    window.fill(BG_COLOR)
    ball.draw()
    player1.draw()
    player2.draw()
    display.update()
