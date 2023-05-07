import pygame
import random
from Napisy import *
pygame.init()
 
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Pong")

background = pygame.image.load("background.png")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
 
done = False
player1_points = 0
player2_points = 0
p1_board = Napisy(screen,(151,53,252),"0",100, "fixedsys")
p2_board = Napisy(screen,(151,53,252),"0",100, "fixedsys")
 
clock = pygame.time.Clock()

class rect(pygame.sprite.Sprite):
    def __init__(self, x, y, v,key_up,key_down):
        self.x = x
        self.y = y
        self.v = v
        self.key_up = key_up
        self.key_down = key_down

        self.image = pygame.Surface((self.x,self.y))

        self.rect = self.image.get_rect(topleft=(self.x,self.y))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[self.key_down] and self.y <= 530:
            self.y += self.v
        elif keys[self.key_up] and self.y >= 0:
            self.y -= self.v
        pygame.draw.rect(screen,(255,255,255),(self.x,self.y,20,70))

class ball(pygame.sprite.Sprite):
    def __init__(self, x, y, x_v, y_v):
        self.x = x
        self.y = y
        self.x_v = x_v
        self.y_v = y_v
        self.x_direction = random.randint(1,2) #l=1 r=2
        self.y_direction = random.randint(1,2) #d=1 u=2

        self.image = pygame.Surface((self.x,self.y))

        self.rect = self.image.get_rect(topleft=(self.x,self.y))
        self.player1_points =  0
        self.player2_points =  0

    def spawn(self):
            self.x_direction = random.randint(1,2)
            self.x = screen_width/2
            self.y = 10
            self.x_v = random.randint(5,8)
            self.y_v = random.randint(5,6)
    def update(self):
        if self.x_direction == 1:
            self.x -= self.x_v
        if self.x_direction == 2:
            self.x += self.x_v
        if self.y_direction == 1:
            self.y += self.y_v
        if self.y_direction == 2:
            self.y -= self.y_v

        #--------------------------------#
        
        if self.x <= 0:
            self.spawn()
            self.player1_points +=1
        if self.x >= 800-20:
            self.spawn()
            self.player2_points +=1
        if self.y <= 0:
            self.y_direction = 1
        if self.y >= 600-20:
            self.y_direction = 2

        pygame.draw.rect(screen,(255,255,255),(self.x,self.y,20,20))
        pygame.draw.rect(screen,(151,53,252),(self.x,self.y,20,20),1)


    
player1 = rect(20,screen_height/2,10,pygame.K_w,pygame.K_s)
player2 = rect(screen_width-40,screen_height/2,9,pygame.K_UP,pygame.K_DOWN)
players = [player1,player2]
ball = ball(screen_width/2,10,random.randint(5,7),random.randint(5,6))  
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 

    if ball.x <= player1.x+20 and ball.y >= player1.y and ball.y <= player1.y+70:
        ball.x_direction = 2
        ball.x_v = random.randint(2,10)
        ball.y_v = random.randint(6,10)

    if ball.x+20 >= player2.x and ball.y >= player2.y and ball.y <= player2.y+70:
        ball.x_direction = 1
        ball.x_v = random.randint(2,10)
        ball.y_v = random.randint(6,10)




    screen.fill((0,0,0))
    screen.blit(background,(-2,0))
    player1.update()
    player2.update()
    ball.update()
    p1_board.change(str(ball.player1_points))
    p2_board.change(str(ball.player2_points))
    p2_board.update(50,20)
    p1_board.update(800-85,20)
    pygame.display.update()
 
    clock.tick(60)
 
pygame.quit()