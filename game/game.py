import pgzrun
import pygame.mouse

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

ball = Ball(WIDTH/2, HEIGHT-100, 10)

paddle = Paddle(WIDTH/2-50, HEIGHT-100, 100, 20)

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

pygame.mouse.set_visible(False)

background = pygame.image.load('./img/1.jpg')

def draw():
    screen.blit(background,(0, 0))

    screen.draw.filled_circle((ball.x,ball.y), ball.r, 'red')
    screen.draw.filled_rect(Rect((paddle.x,paddle.y), (paddle.w, paddle.h)), 'green')

    for block in blocks:
        screen.draw.filled_rect(Rect((block.x,block.y), (block.w, block.h)), 'orange')

    screen.draw.text("Score: "+str(ball.x), (100,0), color="black")

def update():
    global speedX, speedY

    paddle.x = pygame.mouse.get_pos()[0]
    
    if ball.x >= WIDTH or ball.x < 0:
        speedX *= -1
    if ball.y >= HEIGHT or ball.y < 0:
        speedY *= -1
    ball.x+=speedX
    ball.y+=speedY

    if paddle.y <= ball.y <= paddle.y+paddle.h and paddle.x <= ball.x <= paddle.x+paddle.w:
        speedY *= -1  
        
    if blocks.Block.x <= ball.y <= blocks.Block.y+blocks.Block.h and blocks.Block.x <= ball.x <= blocks.Block.x+blocks.Block.w:
        speedY *= -1  and blocks.pop(Block)

pgzrun.go()
