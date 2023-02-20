import pgzrun
import pygame.mouse
import random

WIDTH = 500
HEIGHT = 400

class Car():
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

car = Car(WIDTH/2-45, HEIGHT-100, 45, 90)


blocks = []


for i in range(3):
    blocks.append(Block(10 + 200*i, 30, 60, 20))
for i in range(5):
    blocks.append(Block(40 + 250*i, 70, 60, 20))
for i in range(3):
    blocks.append(Block(10 + 200*i, 110, 60, 20))


speed = 5
speedX = speed
speedY = speed


pygame.mouse.set_visible(False)


background = pygame.image.load('./img/road.jpg')
car_pic = pygame.image.load('./img/car.png')
car_pic = pygame.transform.scale(car_pic, (0,0))


def draw():
    screen.blit(background,(0, 0))

    for block in blocks:
            screen.draw.filled_rect(Rect((block.x,block.y), (block.w, block.h)), 'black')



def update():
    global speedX, speedY

    car.x = pygame.mouse.get_pos()[0]

        
    car.x+=speedX
    car.y+=speedY











pgzrun.go()