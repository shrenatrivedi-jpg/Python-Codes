import pgzrun
WIDTH=400
HEIGHT=400
def draw():
    screen.fill("white")
    screen.draw.filled_circle((200,200),200,"red")
    screen.draw.filled_circle((200,200),180,"orange")
    screen.draw.filled_circle((200,200),160,"yellow")
    screen.draw.filled_circle((200,200),140,"green")
    screen.draw.filled_circle((200,200),120,"blue")
    screen.draw.filled_circle((200,200),100,"indigo")
    screen.draw.filled_circle((200,200),80,"violet")
pgzrun.go()
