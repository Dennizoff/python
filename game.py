import pgzrun
import pygame.mouse
import random

WIDTH = 500
HEIGHT = 400

class Ball():
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

class Paddle():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

class Block():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

class Extralife():
    def __init__(self, x, y):
        self.x = x
        self.y = y


extralife = []


ball = Ball(WIDTH/2, HEIGHT-100, 10)

paddle = Paddle(WIDTH/2-50, HEIGHT-20, 100, 20)

blocks = []


for i in range(7):
    blocks.append(Block(10 + 70*i, 30, 60, 20))
for i in range(6):
    blocks.append(Block(40 + 70*i, 70, 60, 20))
for i in range(7):
    blocks.append(Block(10 + 70*i, 110, 60, 20))

speed = 5
speedX = speed
speedY = speed

lifes = 3
score = 0

pygame.mouse.set_visible(False)

background = pygame.image.load('./img/1.jpg')
heart = pygame.image.load('./img/heart.png')
heart = pygame.transform.scale(heart, (20,20))
Extralife = pygame.image.load('./img/heart.png')
Extralife = pygame.transform.scale(Extralife, (20,20))

def draw():
    screen.blit(background,(0, 0))
    

    screen.draw.filled_circle((ball.x,ball.y), ball.r, 'red')
    screen.draw.filled_rect(Rect((paddle.x,paddle.y), (paddle.w, paddle.h)), 'green')

    for block in blocks:
        screen.draw.filled_rect(Rect((block.x,block.y), (block.w, block.h)), 'orange')
    for life in range(lifes):
        screen.blit(heart,(30*life, 0))
    
    # screen.draw.text("Lifes: "+str(lifes), (10,0), color="black")
    screen.draw.text("Score: "+str(score), (WIDTH-100,0), color="black")
    if lifes == 0:
        screen.draw.text("Game Over", (WIDTH/2-100,HEIGHT/2-24), color="black", fontsize=48)
    if len(blocks) == 0:
        screen.draw.text("You Win!", (WIDTH/2-100,HEIGHT/2-24), color="black", fontsize=48)

def update():
    global speedX, speedY, score, lifes

    paddle.x = pygame.mouse.get_pos()[0]
    
    if ball.x >= WIDTH or ball.x < 0:
        speedX *= -1
    if ball.y >= HEIGHT or ball.y < 0:
        speedY *= -1
    if ball.y >= HEIGHT:
        lifes-=1
    ball.x+=speedX
    ball.y+=speedY

    if paddle.y <= ball.y <= paddle.y+paddle.h and paddle.x <= ball.x <= paddle.x+paddle.w:
        speedY *= -1  

    for block in blocks:
        if block.y <= ball.y <= block.y+block.h and block.x <= ball.x <= block.x+block.w:
            speedY *= -1
            blocks.remove(block)
            score+=1
            rand = random.sample(range(3))
            if rand == 0:
                extralifes.append(Extralife(block.x, block.y))


    if lifes == 0 or len(blocks) == 0:
        speedX = 0
        speedY = 0
        ball.x = WIDTH/2
        ball.y = HEIGHT-100
    

pgzrun.go()
# next step
# серце, появляються рандомно коли наш мяч знищує блок, на його місці може появитися серце, який буде падати, добавити додаткове життя
# бонуси, появляються рандомно коли наш мяч знищує блок, на його місці може появитися бонус, який буде падати, робити платформу 2х
