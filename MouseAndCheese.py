import pgzrun
from random import randint

WIDTH=600
HEIGHT=500

score=0
game_over=False

mouse=Actor("mouse")
mouse.pos=100,100

cheese=Actor("cheese")
cheese.pos=200,200

def draw():
    screen.blit("background",(0,0))
    cheese.draw()
    mouse.draw()
    screen.draw.text("Score: "+str(score),color="black",topleft=(10,10))

    if game_over:
        screen.fill("pink")
        screen.draw.text("Time's Up! Your final score: "+str(score), midtop=(WIDTH/2,10),fontsize=40,color="red")

def place_cheese():
    cheese.x=randint(70,WIDTH-70)
    cheese.y=randint(70,HEIGHT-70)

def time_up():
    global game_over
    game_over=True

def update():
    global score
    if keyboard.left:
        mouse.x=mouse.x-2
    if keyboard.right:
        mouse.x=mouse.x+2
    if keyboard.up:
        mouse.y=mouse.y-2
    if keyboard.down:
        mouse.y=mouse.y+2
    cheese_collected=mouse.colliderect(cheese)
    if cheese_collected:
        score=score+10
        place_cheese()
clock.schedule(time_up,60.0)
pgzrun.go()