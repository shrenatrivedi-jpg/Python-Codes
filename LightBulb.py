import pygame
from time import *
pygame.init()

WIDTH=600
HEIGHT=600

screen=pygame.display.set_mode((400,500))
pygame.display.set_caption("Light Bulb")

img1=pygame.image.load("lightbulb_on.jpeg")
image1=pygame.transform.scale(img1,(400,500))

img2=pygame.image.load("lightbulb_off.jpeg")
image2=pygame.transform.scale(img2,(400,500))

running=True

while running:
    screen.fill((255, 255, 255))
    screen.blit(image1,(100,50))
    pygame.display.update()
    sleep(2)

    screen.fill((255, 255, 255))
    screen.blit(image2,(100,50))
    pygame.display.update()
    sleep(2)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

pygame.quit()
