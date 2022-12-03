from pygame import *

window = display.set_mode((700, 500))

ball = image.load("ball.png")
ball = transform.scale(ball, (30, 30))

clock = time.Clock()
game = True
#TODO Слишком много переменных для одного мяча - использовать классы
ball_x = 50
ball_y = 50
ball_speed_x = 3
ball_speed_y = 3
while game:
    clock.tick(60)

    for e in event.get():
        if e.type == QUIT:
            game = False
        
    # Правила
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    #TODO Это надо упростить
    if ball_y+30 >= 500:
        ball_speed_y *= -1
    if ball_x+30 >= 700:
        ball_speed_x *= -1
    if ball_y < 0:
        ball_speed_y *= -1
    if ball_x < 0:
        ball_speed_x *= -1

    # Отрисовка    
    window.fill((30, 240, 255))
    window.blit(ball, (ball_x, ball_y))    
    display.update()
