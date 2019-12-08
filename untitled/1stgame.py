import pygame
import random
import time
pygame.init()

display_width = 600
display_height = 400
fps = 120

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
back_color = (61, 200, 45)

win = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("1st Game")

clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 70))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.center = (display_width*0.3, 0)
        self.vel = 0
        self.jump = 0

    def update(self):
        event = pygame.key.get_pressed()
        if self.rect.bottom < display_height*0.63:
            self.acc = 0.2
        else:
            self.rect.bottom = display_height * 0.63
            self.acc = 0
            self.vel = 0
            self.jump = 0

        if event[pygame.K_UP] and not self.jump:
            self.vel = -7
            self.jump = 1
        # event = pygame.event.get()
        '''for event1 in pygame.event.get():
            if event1.type == pygame.KEYUP:
                self.vel = 1'''

        self.rect.centery += self.vel + 0.5 * self.acc
        self.vel += self.acc

        if event[pygame.K_LEFT]:
            self.rect.centerx -= 4
        if event[pygame.K_RIGHT]:
            self.rect.centerx += 4


class Blocks(pygame.sprite.Sprite):
    def __init__(self, a):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(a)
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.rect.bottom = display_height*0.63
        self.rect.x = display_width*1.2
        self.speedx = 3

    def update(self):
        self.rect.x -= self.speedx
        if self.rect.right < -display_width*0.25:
            i = random.randint(0, 3)
            self.image = pygame.Surface(types[i])
            self.image.fill(black)
            self.rect = self.image.get_rect()
            self.rect.bottom = display_height*0.63
            self.rect.x = display_width*1.6


def score(dodged, level):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(dodged), True, black)
    text1 = font.render("Level: " + str(level), True, black)
    win.blit(text1, (display_width * 0.85, 0))
    win.blit(text, (0, 0))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(win, color, [thingx, thingy, thingw, thingh])


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 30)
    textsurf, textrect = text_objects(text, largeText)
    textrect.center = (display_width*0.5, display_height*0.05)
    win.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(2)


def crash():
    message_display('You Crashed')


types = ((30, 70), (75, 70), (30, 35), (80, 35))


def gameloop():

    all_sprites = pygame.sprite.Group()
    mobs = pygame.sprite.Group()

    player = Player()
    all_sprites.add(player)

    i = random.randint(0, 3)
    j = random.randint(0, 3)
    m1 = Blocks(types[i])
    m2 = Blocks(types[j])
    m2.rect.x = display_width*2
    all_sprites.add(m1, m2)
    mobs.add(m1, m2)
    m1check = 0
    m2check = 0

    dodged = 0
    level = 1

    gameRun = True
    while gameRun:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRun = False
                pygame.quit()
                quit()
            print(event)

        if (m1.rect.x <= display_width*0.31 and m1check == 0) or (m2.rect.x <= display_width*0.31 and m2check == 0):
            dodged += 1
            if not m1check:
                m1check = 1
            if not m2check:
                m2check = 1
            if not dodged % 10 and dodged:
                level += 1
                m1.speedx += 0.5
                m2.speedx += 0.5
        if m1.rect.x > display_width*0.31:
            m1check = 0
        if m2.rect.x > display_width*0.31:
            m2check = 0
        win.fill(white)
        all_sprites.update()
        all_sprites.draw(win)
        things(0, 0.63 * display_height, display_width, 2, black)
        score(dodged, level)

        collisions = pygame.sprite.spritecollide(player, mobs, False)
        if collisions:
            crash()
            gameRun = False

        pygame.display.update()

        clock.tick(fps)


gameloop()
pygame.quit()
quit()