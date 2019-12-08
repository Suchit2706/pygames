import pygame
import time
import random
pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
back_color = (61, 200, 45)


win=pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("A bit Racey")

clock = pygame.time.Clock()

carImg = pygame.image.load("racecar4.png")


def score(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    win.blit(text, (0, 0))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(win, color, (thingx, thingy, thingw, thingh))


def car(x, y):
    win.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    textsurf, textrect = text_objects(text, largeText)
    textrect.center = ((display_width/2, display_height/2))
    win.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(2)

    game_loop()


def crash():
    message_display('You Crashed')


def game_loop():
    x = (display_width*0.43)
    y = (display_height*0.855)
    carWidth = 50
    carHeigth = 85

    x_change = 0
    y_change = 0
    dodged = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_heigth = 100
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                '''if event.key == pygame.K_UP:
                    y_change = -5
                if event.key == pygame.K_DOWN:
                    y_change = 5'''
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                '''if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0'''

            print(event)
        x = x + x_change
        y = y + y_change
        win.fill(back_color)
        things(thing_startx, thing_starty, thing_width, thing_heigth, blue)
        thing_starty += thing_speed
        car(x, y)
        score(dodged)

        if x >= display_width - carWidth or x <= 0:
            crash()
        if y <= 0 or y >= display_height - carHeigth:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_heigth
            thing_startx = random.randrange(0, display_width - thing_width)
            dodged += 1
            thing_speed += 1
            thing_width += 1

        if y < thing_starty + thing_heigth:
            if x > thing_startx and x < thing_startx + thing_width or x + carWidth > thing_startx and x + carWidth < thing_startx + thing_width:
                crash()
        pygame.display.update()
        clock.tick(60)

game_loop()
