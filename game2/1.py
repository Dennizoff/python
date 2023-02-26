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

class Bonus():
    def __init__(self, x, y,) :
         self.x = x
         self.y = y
         self.h = 20
         self.w = 20
class Block():
    w = 45
    h = 80
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Block2():
    w = 45
    h = 80
    def __init__(self, x, y):
        self.x = x
        self.y = y
car = Car(WIDTH/2-45, HEIGHT-100, 45, 90) 
# block = Block(WIDTH/2-45, HEIGHT-100) 
# block2 = Block2(WIDTH/2-45, HEIGHT-100) 



bonuses = []

blocks = []
blocks2 = []

speed = 3
speed2 = -3




pygame.mouse.set_visible(False)

background = pygame.image.load('./img/road.jpg')
car_pic = pygame.image.load('./img/car.png')
car_pic = pygame.transform.scale(car_pic, (car.w,car.h))
block_pic = pygame.image.load('./img/car2.png')
block_pic = pygame.transform.scale(block_pic, (Block.w,Block.h))
bonus_pic = pygame.image.load('./img/circleBonus.png')
bonus_pic = pygame.transform.scale(bonus_pic, (20,20))
block2_pic = pygame.image.load('./img/car3.png')
block2_pic = pygame.transform.scale(block2_pic, (Block2.w,Block2.h))
    
cut = 10
fixedCar = 0
position = 0

def draw():
    screen.blit(background,(0, 0))
    screen.blit(car_pic,(car.x, car.y))
    # screen.blit(block2_pic,(block2.x, block2.y))
    for bonus in bonuses:
        screen.blit(bonus_pic,(bonus.x, bonus.y))





    
    # screen.draw.text("Score: "+str(block.y), (WIDTH-100,0), color="black")

    

    # screen.draw.text("Score: "+str(len(blocks)), (WIDTH-100,0), color="black")
    print(len(blocks2))
    for block in blocks:
       screen.blit(block_pic,(block.x, block.y))
    
    for block2 in blocks2:
       screen.blit(block2_pic,(block2.x, block2.y))

    if gameOver:
        screen.draw.text("Game Over", (WIDTH/2-100,HEIGHT/2-24), color="black", fontsize=48)
    #    screen.draw.filled_rect(Rect((block.x,block.y), (cut, cut)), 'orange')
    #    screen.draw.filled_rect(Rect((block.x+block.w-cut,block.y), (cut, cut)), 'orange')

    #    screen.draw.filled_rect(Rect((block.x,block.y+block.h-cut), (cut, cut)), 'orange')
    #    screen.draw.filled_rect(Rect((block.x+block.w-cut,block.y+block.h-cut), (cut, cut)), 'orange')

    # screen.draw.filled_rect(Rect((car.x,car.y), (cut, cut)), 'orange')
    # screen.draw.filled_rect(Rect((car.x+car.w-cut,car.y), (cut, cut)), 'orange')

    # screen.draw.filled_rect(Rect((car.x,car.y+car.h-cut), (cut, cut)), 'orange')
    # screen.draw.filled_rect(Rect((car.x+car.w-cut,car.y+car.h-cut), (cut, cut)), 'orange')
    # screen.draw.text(str(block.x)+" "+str(block.w), (WIDTH-200,0), color="black")


gameOver = False

def update():
    global speed, fixedCar, position, bonuses, gameOver
    if gameOver:
        return 0

    if fixedCar == 0:
        position = pygame.mouse.get_pos()[0]
    
    if position >= 270 and position <= 350:
        car.x = position 
    elif position < 270:
        car.x = 270
    elif position > 350:
        car.x = 350
        # 106,177


    rand = random.randrange(0, int(1000/speed) if speed > 0 else 1000)
    if rand == 0:
        bonuses.append(Bonus(350, 0)) 
    elif rand == 2:
        bonuses.append(Bonus(97, 0,)) 

    for bonus in bonuses:
        bonus.y += speed
        if bonus.y > HEIGHT:
            bonuses.remove(bonus)

    
    if len(blocks) < 1:
        rand = random.randrange(0, 2)
        if rand == 0:
            blocks.append(Block(350, 0)) 
        else:
            blocks.append(Block(300, 0))
            


    if len(blocks2) < 1:
        rand = random.randrange(0, 2)
        if rand == 0:
            blocks2.append(Block2(106, 350))  
        else:
            blocks2.append(Block2(177, 300))

    for block in blocks:
        block.y += speed
        if block.y > HEIGHT:
            blocks.remove(block)

    for block2 in blocks2:
        block2.y += speed2
        if block2.y < 0:
            blocks2.remove(block2)


    for bonus in bonuses:
         if  (bonus.x <= car.x <= bonus.x+bonus.w or bonus.x <= car.x+car.w <= bonus.x+bonus.w) and (bonus.y <= car.y <= bonus.y+bonus.h or bonus.y <= car.y+car.h <= bonus.y+bonus.h ):
            if speed > 0.5:
                speed -= 0.2

    for block in blocks:
         if  (block.x <= car.x <= block.x+block.w or block.x <= car.x+car.w <= block.x+block.w) and (block.y <= car.y <= block.y+block.h or block.y <= car.y+car.h <= block.y+block.h ):
            #  position = (270+350)/2 #не працює
            # blocks.remove(block)
            speed = 0
            gameOver = True
            break
         else:
            speed+=0.005   
            #  fixedCar = position

    

pgzrun.go()

# замість чорного прямокутника, рандомне зображення машинки
# бонус зменшувати швидкість і додавати бали
# на лівій полосі, машинки в зворотню сторону будуть їхати