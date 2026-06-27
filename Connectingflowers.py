import pgzrun
from random import randint
from time import time

WIDTH = 800
HEIGHT = 600

flowers = []
lines=[]
next_flower = 0

start_time=0
total_time=0
end_time=0

number_of_flowers=8

def create_flowers():
    global start_time
    for count in range(0,number_of_flowers):
        flower = Actor('flower')
        flower.pos = randint(40, WIDTH-40), randint(40, HEIGHT-40)
        flowers.append(flower)
    start_time = time()

def draw():
    global total_time

    screen.blit("background", (0, 0))

    number=1
    for flower in flowers:
        screen.draw.text(str(number), (flower.pos[0], flower.pos[1]+20))
        flower.draw()
        number=number+1
    for line in lines:
        screen.draw.line(line[0], line[1], (255, 255, 255))
    if next_flower<number_of_flowers:
        total_time = time() - start_time
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize=30)
    else:
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize=30)

def update(): 
    pass

def on_mouse_down(pos):
    global next_flower, lines
    if next_flower<number_of_flowers:
        if flowers[next_flower].collidepoint(pos):
            if next_flower>0:
                lines.append((flowers[next_flower-1].pos, flowers[next_flower].pos))
            next_flower=next_flower+1
        else:
            lines=[]
            next_flower=0
create_flowers()
pgzrun.go()
