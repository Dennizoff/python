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
    w = 45
    h = 80
    def __init__(self, x, y):
        self.x = x
        self.y = y

car = Car(WIDTH/2-45, HEIGHT-100, 45, 90) 
block = Block(WIDTH/2-45, HEIGHT-100) 


blocks = []

speed = 4

pygame.mouse.set_visible(False)

background = pygame.image.load('./img/road.jpg')
car_pic = pygame.image.load('./img/car.png')
car_pic = pygame.transform.scale(car_pic, (car.w,car.h))
block_pic = pygame.image.load('./img/car2.png')
block_pic = pygame.transform.scale(block_pic, (Block.w,Block.h))

cut = 10
fixedCar = 0
position = 0

def draw():
    screen.blit(background,(0, 0))
    screen.blit(car_pic,(car.x, car.y))
    
    screen.draw.text("Score: "+str(car.x), (WIDTH-100,0), color="black")

    

    # screen.draw.text("Score: "+str(len(blocks)), (WIDTH-100,0), color="black")

    for block in blocks:
       screen.blit(block_pic,(block.x, block.y))
    #    screen.draw.filled_rect(Rect((block.x,block.y), (cut, cut)), 'orange')
    #    screen.draw.filled_rect(Rect((block.x+block.w-cut,block.y), (cut, cut)), 'orange')

    #    screen.draw.filled_rect(Rect((block.x,block.y+block.h-cut), (cut, cut)), 'orange')
    #    screen.draw.filled_rect(Rect((block.x+block.w-cut,block.y+block.h-cut), (cut, cut)), 'orange')

    # screen.draw.filled_rect(Rect((car.x,car.y), (cut, cut)), 'orange')
    # screen.draw.filled_rect(Rect((car.x+car.w-cut,car.y), (cut, cut)), 'orange')

    # screen.draw.filled_rect(Rect((car.x,car.y+car.h-cut), (cut, cut)), 'orange')
    # screen.draw.filled_rect(Rect((car.x+car.w-cut,car.y+car.h-cut), (cut, cut)), 'orange')
    # screen.draw.text(str(block.x)+" "+str(block.w), (WIDTH-200,0), color="black")




def update():
    global speed, fixedCar, position

    if fixedCar == 0:
        position = pygame.mouse.get_pos()[0]
    
    if position >= 270 and position <= 350:
        car.x = position 
    elif position < 270:
        car.x = 270
    elif position > 350:
        car.x = 350
        # 97,180

    if len(blocks) < 1:
        rand = random.randrange(0, 2)
        if rand == 0:
            blocks.append(Block(350, 0)) 
            
            blocks.append(Block(97, 0)) 

        else:
            blocks.append(Block(300, 0))
            
            blocks.append(Block(180, 0)) 

    for block in blocks:
        block.y += speed
        if block.y > HEIGHT:
            blocks.remove(block)

    for block in blocks:
         if  (block.x <= car.x <= block.x+block.w or block.x <= car.x+car.w <= block.x+block.w) and (block.y <= car.y <= block.y+block.h or block.y <= car.y+car.h <= block.y+block.h ):
            #  position = (270+350)/2 #не працює
            blocks.remove(block)
            #  speed = 0
            #  fixedCar = position

            #  screen.draw.text("Game Over", (WIDTH/2-100,HEIGHT/2-24), color="black", fontsize=48)#не працює



    # speed+=0.1

pgzrun.go()

# замість чорного прямокутника, рандомне зображення машинки
# бонус зменшувати швидкість і додавати бали
# на лівій полосі, машинки в зворотню сторону будуть їхати