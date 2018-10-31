import pygame

pygame.init()

white=(255,255,255)
black=(0,0,0)
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)

gameDisplay=pygame.display.set_mode((800,600))
gameDisplay.fill(black)

pixAr = pygame.PixelArray(gameDisplay)
pixAr[10][20]=green

pygame.draw.circle(gameDisplay,blue,(400,400),10)
pygame.draw.polygon(gameDisplay,green,((100,100),(200,200),(173,100)))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()