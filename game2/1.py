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

speed = 4

pygame.mouse.set_visible(False)

background = pygame.image.load('./img/road.jpg')
car_pic = pygame.image.load('./img/car.png')
car_pic = pygame.transform.scale(car_pic, (50,80))


def draw():
    screen.blit(background,(0, 0))
    screen.blit(car_pic,(car.x, car.y))

    # screen.draw.text("Score: "+str(len(blocks)), (WIDTH-100,0), color="black")

    for block in blocks:
        screen.draw.filled_rect(Rect((block.x,block.y), (block.w, block.h)), 'black')



def update():
    global speed

    position = pygame.mouse.get_pos()[0]
    if position >= 270 and position <= 350:
        car.x = position 
    elif position < 270:
        car.x = 270
    elif position > 350:
        car.x = 350

    if len(blocks) < 1:
        rand = random.randrange(0, 2)
        if rand == 0:
            blocks.append(Block(350, 0, 20, 40))
        else:
            blocks.append(Block(300, 0, 20, 40))

    for block in blocks:
        block.y += speed
        if block.y > HEIGHT:
            blocks.remove(block)

    # speed+=0.1

pgzrun.go()

# замість чорного прямокутника, рандомне зображення машинки
# бонус зменшувати швидкість і додавати бали
# на лівій полосі, машинки в зворотню сторону будуть їхати