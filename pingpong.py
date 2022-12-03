from pygame import *

window = display.set_mode((700, 500))

clock = time.Clock()
game = True
while game:
    clock.tick(60)

    for e in event.get():
        if e.type == QUIT:
            game = False
        
    window.fill((30, 240, 255))    
    display.update()
