import pygame
import time
import sys, random
from pygame.locals import *

pygame.init()

# Window width and height
window_width = 700
window_height = 500

## Window Dimensions
window = pygame.display.set_mode([window_width, window_height])

# Colors
white = [255, 255, 255]
black = [0, 0, 0]
blue = [0, 0, 255]
dark_blue = [0, 0, 50]
cyan = [0, 255, 255]
green = [200, 255, 200]
red = [255, 0, 0]

# Clock
clock = pygame.time.Clock()

## initial position of the paddle y
paddle1y = 50
paddle2y = 50

## Points of player one
point1 = 00
## Points of player one
point2 = 00

## Number of the times the ball hits the right paddle with one player
count = 0

## initial position of the ball x y
x = 350
y = 250

dt = 1
#this variable changes the position in X 
vx = 5 
#this variable changes the position in y
vy = 5 
#this variable changes is the radius of the ball
radius = 10 

pygame.display.set_caption("Pong")

font = pygame.font.Font('freesansbold.ttf', 80)
title = font.render("PONG", True, green)
window.blit(title, (235, 70))
font1 = pygame.font.Font('freesansbold.ttf', 24)
onePlayer = font1.render("One Player", True, green)
window.blit(onePlayer, (300, 250))
twoPlayers = font1.render("Two Players", True, green)
window.blit(twoPlayers, (300, 300))
close = font1.render("Close", True, green)
window.blit(close, (300, 350))

pygame.display.update()
while True:
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                if mouseX > 282 and mouseX < 440 and mouseY > 245 and mouseY < 277:
                    import onePlayer
                if mouseX > 282 and mouseX < 440 and mouseY > 292 and mouseY < 333:
                    import twoPlayers
                if mouseX > 282 and mouseX < 440 and mouseY > 348 and mouseY < 389:
                    pygame.quit()
                    sys.exit()
                
