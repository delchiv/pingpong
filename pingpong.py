from pygame import *
from random import randint

W_W = 700
W_H = 500
window = display.set_mode((W_W, W_H))
BG_COLOR = (30, 240, 255)
font.init()
fnt = font.SysFont("Arial", 24)

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
        global p1, p2
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y+30 >= W_H:
            self.speed_y *= -1
            BG_COLOR = (randint(0, 255), randint(0, 255), randint(0, 255))
        if self.rect.x+30 >= W_W: # Коснулись правого края
            self.speed_x *= -1
            self.rect.x = W_W // 2
            self.rect.y = W_H // 2
            p1 += 1
            BG_COLOR = (randint(0, 255), randint(0, 255), randint(0, 255))
        if self.rect.y < 0:
            self.speed_y *= -1
            BG_COLOR = (randint(0, 255), randint(0, 255), randint(0, 255))
        if self.rect.x < 0:  # Коснулись левого края
            self.speed_x *= -1
            self.rect.x = W_W // 2
            self.rect.y = W_H // 2
            p2 += 1
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
            if self.rect.y - self.speed_y > 0:
                self.rect.y -= self.speed_y
        elif key_pressed[self.k_down]:
            if self.rect.y + self.speed_y + self.rect.h < W_H:
                self.rect.y += self.speed_y
        super().draw()

def text(txt, color, coord, rf=fnt):
    img = rf.render(
        txt, # Что писать
        1,
        color # Цвет
    )
    if coord == "center":
        img_rect = img.get_rect()
        coord = ((W_W - img_rect.width) // 2, (W_H - img_rect.height) // 2)
    window.blit(img, coord)

ball = Ball(50, 50, 30, 30, 3, "ball.png")
player1 = Player(10, 200, 20, 100, 5, "player.png", K_w, K_s)
player2 = Player(670, 200, 20, 100, 5, "player.png", K_UP, K_DOWN)

clock = time.Clock()
game = True
game_over = False
p1 = 0
p2 = 0
while game:
    clock.tick(60)

    for e in event.get():
        if e.type == QUIT:
            game = False
        
    # Правила
    if player1.rect.colliderect(ball.rect):
        ball.speed_x *= -1
    if player2.rect.colliderect(ball.rect):
        ball.speed_x *= -1
    if p1 > 5:
        game_over = True
    if p2 > 5:
        game_over = True

    # Отрисовка    
    window.fill(BG_COLOR)
    if not game_over:
        ball.draw()
        player1.draw()
        player2.draw()
        text(str(p1), (255, 255, 255), (W_W//2-20, 10))
        text(str(p2), (255, 255, 255), (W_W//2+20, 10))
    else:
        if p1 > 5:
            text("Победил игрок 1", (255, 0, 0), "center")
        else:
            text("Победил игрок 2", (255, 0, 0), "center")
    display.update()
