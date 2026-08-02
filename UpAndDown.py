import pygame

pygame.init()

WIDTH=600
HEIGHT=400
screen=pygame.display.set_mode((WIDTH, HEIGHT))

WHITE=(255,255,255)
BLACK=(0,0,0)

class Line:
    def __init__(self,):
        self.y=HEIGHT//2
        self.speed=2
    
    def update(self, keys):
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

        if self.y < 0:
            self.y = 0
        if self.y > HEIGHT:
            self.y = HEIGHT


    def draw(self, screen):
        start=(150, self.y)
        end=(450, self.y)
        pygame.draw.line(screen, BLACK, start, end, 3)

line=Line()

running=True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    keys=pygame.key.get_pressed()
    line.update(keys)

    screen.fill(WHITE)
    line.draw(screen)
    pygame.display.update()

pygame.quit()
