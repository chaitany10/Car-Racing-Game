import pygame

pygame.init()#initializing pygame

display_width=800#
display_height=600

black=(0,0,0)
white=(255,255,255)
car_width=73

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Race')

clock = pygame.time.Clock()

carimg=pygame.image.load('racecar.png')

def car(x,y):
    gameDisplay.blit(carimg,(x,y))


def gameLoop():
    x=(display_width*0.45)
    y=display_height*0.8

    x_change=0
    y_change=0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT :
                gameExit = True

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-5
                elif event.key==pygame.K_RIGHT:
                    x_change=5
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change = 0

        x +=x_change


        gameDisplay.fill(white)
        car(x,y)

        if x > display_width-car_width or x<0:
            gameExit=True
        pygame.display.update()

        clock.tick(60)

gameLoop()

pygame.quit()
quit()
