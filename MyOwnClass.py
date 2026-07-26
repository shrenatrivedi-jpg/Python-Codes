import pygame
pygame.init()
screen=pygame.display.set_mode([500,500])

red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
yellow=(255,255,0)
black=(0,0,0)

screen.fill(white)

class Circle():
    def __init__(self, color, pos, rad, wid=0):
        self.color=color
        self.radius=rad
        self.pos=pos
        self.wid=wid
        self.screen=screen

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.rad, self.wid)

    def grow(self,x):
        self.rad+=x
        pygame.draw.circle(self.screen, self.color, self.pos, self.rad, self.wid)

color="red"
position=(300,300)
radius=50
wid=2
pygame.draw.circle(screen,color,position,radius, wid)
pygame.display.update()

redCircle=Circle(red, position, radius+40)
yellowCircle=Circle(yellow, position, radius,5)
blueCircle=Circle(blue, position, radius+60)
greenCircle=Circle(green, position, 20)

while True:
    for event in pygame.event.get():
        if (event.type==pygame.MOUSEBUTTONDOWN):
            blueCircle.draw()
            redCircle.draw()
            yellowCircle.draw()
            greenCircle.draw()
            pygame.display.update()
        elif event.type==pygame.MOUSEBUTTONUP:
            blueCircle.grow()
            redCircle.grow()
            yellowCircle.grow()
            greenCircle()
            pygame.display.update()
        elif event.type==pygame.MOUSEMOTION:
            pos=pygame.mouse.get_pos()
            blackCircle=Circle(black, pos, 10)
            blackCircle.draw()
            pygame.display.update()

    


