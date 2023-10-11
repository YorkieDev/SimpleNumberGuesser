import pygame
from random import randint
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Number Guessing Game')
font = pygame.font.Font(None, 36)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.fill(white)
    text_surface = font.render('Guess a number between 1 and 9', True, black)
    screen.blit(text_surface, (0, 0))
    guess = pygame.draw.rect(screen, yellow, [250, 300, 100, 40])
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            collide = guess.collidepoint(pos)
            if collide:
                screen.fill(white)
                text_surface = font.render('Guess a number between 1 and 9', True, black)
                screen.blit(text_surface, (0, 0))
                guess = pygame.draw.rect(screen, yellow, [250, 300, 100, 40])
                number = randint(1,9)
                text_surface = font.render('Is your number ' + str(number), True, black)
                screen.blit(text_surface, (250, 300))
    pygame.display.update()