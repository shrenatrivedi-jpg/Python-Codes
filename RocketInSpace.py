import pygame
from pygame.locals import *
from time import *

pygame.init()

screen=pygame.display.set_mode((600,600))

player_x=200
player_y=200

keys=[False,False,False,False]

player=pygame.image.load("character.jpeg")
background=pygame.image.load("spacebackground.jpeg")

while player_y<600:
    screen.blit(background,(0,0))
    screen.blit(player,(player_x,player_y))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.KEYDOWN:
            #check which button is pressed
            if event.key==K_UP:
                keys[0]=True
            elif event.key==K_DOWN:
                keys[1]=True
            elif event.key==K_LEFT:
                keys[2]=True
            elif event.key==K_RIGHT:
                keys[3]=True
        if event.type==pygame.KEYUP:
            if event.key==K_UP:
                keys[0]=False
            elif event.key==K_DOWN:
                keys[1]=False
            elif event.key==K_LEFT:
                keys[2]=False
            elif event.key==K_RIGHT:
                keys[3]=False
            