import pygame
import time
import random

'''
Importing pygame and initializing it.
making a layer 
'''
pygame.init()  # initializing pygame

display_width = 800
display_height = 600

block_colour = (0, 0, 255)
black = (0, 0, 0)
green = (0, 200, 0)
red = (200, 0, 0)
dark_red = (255, 0, 0)
dark_green = (0, 255, 0)
white = (255, 255, 255)
car_width = 73

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Race')

clock = pygame.time.Clock()

carimg = pygame.image.load('racecar.png')


def things_dodged(count):
    font = pygame.font.SysFont(None, 24, True)
    text = font.render("Dodged : " + str(count), True, black)

    gameDisplay.blit(text, (0, 0))

    pygame.display.update()


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def car(x, y):
    gameDisplay.blit(carimg, (x, y))


def crash():
    message_display('You Crashed!!')


def gameIntro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 75)
        TextSurf, TextRect = text_objects("A Racing Game", largeText)
        TextRect.center = (display_width / 2, display_height / 3)
        gameDisplay.blit(TextSurf, TextRect)
        mouse1 = pygame.mouse.get_pos()

        if 150 < mouse1[0] < 250 and 450 < mouse1[1] < 500:
            pygame.draw.rect(gameDisplay, dark_green, (150, 450, 100, 50))
        else:
            pygame.draw.rect(gameDisplay, green, (150, 450, 100, 50))
        if 550 < mouse1[0] < 650 and 450 < mouse1[1] < 500:
            pygame.draw.rect(gameDisplay, dark_red, (550, 450, 100, 50))
        else:
            pygame.draw.rect(gameDisplay, red, (550, 450, 100, 50))

        pygame.display.update()
        clock.tick(10)


def text_objects(text, font):
    textSurface = font.render(text, True, block_colour)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (display_width / 2, display_height / 2)
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)

    gameLoop()


def gameLoop():
    x = (display_width * 0.45)
    y = display_height * 0.8
    dodged = 0
    x_change = 0
    y_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 3
    thing_width = 100
    thing_height = 100
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(white)

        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed

        car(x, y)
        things_dodged(dodged)
        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            if dodged % 5 == 0:
                thing_speed += 1
            if (dodged % 8 == 0):
                thing_width *= 1.2

        if y < thing_starty + thing_height:
            if x + car_width > thing_startx and x < thing_startx + thing_width:
                crash()
        pygame.display.update()

        clock.tick(60)


gameIntro()
gameLoop()

pygame.quit()
quit()
