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
point1 = 0
## Points of player one
point2 = 0

## Number of the times the ball hits the right paddle with one player
count = 0

## initial position of the ball x y
x = 350
y = 250

## initial position of the second ball x y
x1 = 350
y1 = 250

dt = 0

#this variable changes the position in X 
vx = 5 

#this variable changes the position in y
vy = 5

dt1 = 0

#this variable changes the position in X 
vx1 = 5 

#this variable changes the position in y
vy1 = 5 

#this variable changes is the radius of the ball
radius = 10 

pygame.display.set_caption("Pong")

while True:
    window.fill(black)
    for e in pygame.event.get():
        if e.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            if mouseX > 7 and mouseX < 89 and mouseY > 11 and mouseY < 43:
                import PONG

    key_pressed = pygame.key.get_pressed()

    ## Net Line
    pygame.draw.line(window, white, [349, 0], [349, 20], 5)
    pygame.draw.line(window, white, [349, 40], [349, 60], 5)
    pygame.draw.line(window, white, [349, 80], [349, 100], 5)
    pygame.draw.line(window, white, [349, 120], [349, 140], 5)
    pygame.draw.line(window, white, [349, 160], [349, 180], 5)
    pygame.draw.line(window, white, [349, 200], [349, 220], 5)
    pygame.draw.line(window, white, [349, 240], [349, 260], 5)
    pygame.draw.line(window, white, [349, 280], [349, 300], 5)
    pygame.draw.line(window, white, [349, 320], [349, 340], 5)
    pygame.draw.line(window, white, [349, 360], [349, 380], 5)
    pygame.draw.line(window, white, [349, 400], [349, 420], 5)
    pygame.draw.line(window, white, [349, 440], [349, 460], 5)
    pygame.draw.line(window, white, [349, 480], [349, 500], 5)
    
##    Movement 0f Right Paddle
    if x >= 400 and vx != -vx:
        paddle1y = y
    if x1 >= 400 and vx1 != -vx1:
        paddle1y = y1
                    
##    Draw Right Paddle
    pygame.draw.rect(window, white, (665, paddle1y, 10, 70))

        ##    Movement Left Paddle
    if key_pressed[K_w] and paddle2y > 0:
        if paddle2y >= 0:
            paddle2y -= 15
    if key_pressed[K_s] and paddle2y < window_height - 100:
        if paddle2y <= window_height:
            paddle2y += 15
                
        ##    Draw Left Paddle
    pygame.draw.rect(window, white, (20, paddle2y, 10, 70))


        ##    Draw Ball
    pygame.draw.circle(window, cyan, (x, y), radius)
    x += vx * dt
    y += vy * dt

        ## when the ball touches the x margins
    if x < 0:
        point1 += 5
        x = 350
        y = 250
        dt = 1
        count = 0
             
    if x > 700:
        point2 += 5
        x = 350
        y = 250
        dt = 1
        count = 0
    
    if x1 < 0:
        point1 += 5
        x1 = 350
        y1 = 250
        dt1 = 1
        count = 0
             
    if x1 > 700:
        point2 += 5
        x1 = 350
        y1 = 250
        dt1 = 1
        count = 0

        ## Define the Font   
    font = pygame.font.Font('freesansbold.ttf', 32)
    text1 = font.render(str(point2), True, white)
    window.blit(text1, (300,10))   
    text2 = font.render(str(point1), True, white)
    window.blit(text2, (360, 10))
    back1 = font.render("Back", True, red)
    window.blit(back1, (10, 10))

        ## Start the game pressing  w or s 
    if point1 == 0 and point2 == 0 and (key_pressed[K_w] or key_pressed[K_s]):
        dt = 1
        dt1 = 1
        point1 = 0
        point2 = 0
    
        ## Game Over and the computer wins
    if point1 == 40:
        pygame.draw.rect(window, black, (150, 550, 150, 350))
        finish = font.render("GAME OVER", True, red)
        window.blit(finish, (250, window_height/2))
        font2 = pygame.font.Font('freesansbold.ttf', 20)
        finish1 = font2.render("O Computador Ganhou", True, green)
        window.blit(finish1, (240, 290))
        font1 = pygame.font.Font('freesansbold.ttf', 15)
        restart = font1.render("Press [P] to Restart", True, green)
        window.blit(restart, (280, 320))

        dt = 0
        dt1 = 0
        if key_pressed[K_p]:
            dt = 1
            dt1 = 1
            point1 = 0
            point2 = 0
            count = 0

        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                if mouseX > 7 and mouseX < 89 and mouseY > 11 and mouseY < 43:
                    import PONG
            
        ## Game Over and the player wins
    if point2 == 40:
        pygame.draw.rect(window, black, (150, 550, 150, 350))
        finish = font.render("GAME OVER", True, red)
        window.blit(finish, (250, window_height/2))
        font2 = pygame.font.Font('freesansbold.ttf', 20)
        finish1 = font2.render("Player Ganhou", True, green)
        window.blit(finish1, (270, 290))
        font1 = pygame.font.Font('freesansbold.ttf', 15)
        restart = font1.render("Press [P] to Restart", True, green)
        window.blit(restart, (280, 320))
        
        dt = 0
        dt1 = 0
        if key_pressed[K_p]:
            dt = 1
            dt1 = 1
            point1 = 0
            point2 = 0
            count = 0

        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                if mouseX > 7 and mouseX < 89 and mouseY > 11 and mouseY < 43:
                    import PONG

        ## when the ball touches the y margins
    if y + radius >= window_height or y + radius <= 0:
        vy = -vy

        ## when the ball touches the left paddle
    if y + radius >= paddle2y and y + radius <= paddle2y + 100 and x == 30:
        vx = -vx
        vy = -vy
        vy = random.randint(1, 5)    

        ## when the ball touches the right paddle
    if y + radius >= paddle1y and y + radius <= paddle1y + 100 and x == 660:
        vx = -vx
        vy = -vy
        vy = random.randint(1, 5)
        count += 1

        ## when the second ball touches the y margins
    if y1 + radius >= window_height or y1 + radius <= 0:
        vy1 = -vy1

        ## when the second ball touches the left paddle
    if y1 + radius >= paddle2y and y1+ radius <= paddle2y + 100 and x1 == 30 :
        vx1 = -vx1
        vy1 = -vy1
        vy1 = random.randint(1, 5)

        ## when the ball second touches the right paddle
    if y1 + radius >= paddle1y and  y1 + radius <= paddle1y + 100 and x1 == 660:
        vx1 = -vx1
        vy1 = -vy1
        vy1 = random.randint(1, 5)
        count += 1   
         
    if count >= 2:
        pygame.draw.circle(window, green, (x1, y1), radius)
        x1 += vx1 * dt1
        y1 += vy1 * dt1

        ## Exit Game
    if key_pressed[K_ESCAPE]:
        pygame.quit()
        sys.exit()

    time.sleep(0.01)
    pygame.display.update()