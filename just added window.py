import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))#initializing pygame
pygame.display.set_caption('Race')#setting title of window

clock = pygame.time.Clock()#inintializing game clock

crashed = False#state of car

while not crashed:#a loop till the car has no crashed
    for event in pygame.event.get():#for some event if pygame detects it
        if event.type == pygame.QUIT:#quit on press of x
            crashed = True#change state of car

        print(event)

    pygame.display.update()

    clock.tick(60)

pygame.quit()
quit()
