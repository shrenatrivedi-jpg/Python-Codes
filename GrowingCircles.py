import pygame
import sys

pygame.init()
screen=pygame.display.set_mode([500,500])

blue=(0,0,255)

screen.fill((255,255,255))
pygame.display.update()

class Circle():
    def __init__(self, color, pos, radius, width=0):
        self.color=color
        self.pos=pos
        self.radius=radius
        self.width=width
        self.screen=screen

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius, self.width)

    def grow(self, r):
        self.radius=self.radius+r
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius, self.width)

circle1=Circle(blue, (300,300), 25, 0)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if (event.type==pygame.MOUSEBUTTONDOWN):
            screen.fill((255,255,255))
            circle1.draw()
            pygame.display.update()
        elif event.type==pygame.MOUSEBUTTONUP:
            screen.fill((255,255,255))
            circle1.grow(2)
            pygame.display.update()
        elif event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()


    


