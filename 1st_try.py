# -*- coding-utf-8 -*-

import  pygame
import sys
import math
import numpy as np
from pygame import transform


pygame.init()
#screen=pygame.display.set_mode([640,480])
#screen.fill([255,255,255])

''' draw sin(x)
plotPoints=[]
for x in range(0,640):
    y=int(math.sin(x/640.0 *8 *math.pi) * 200 + 240)
    plotPoints.append([x,y])
    #pygame.draw.rect(screen,[0,255,0],[x,y,1,1],2)
    pygame.draw.line(screen,[255,120,120],[0,240],[640,240],1)
pygame.draw.lines(screen,[0,250,0],False,plotPoints,1)
'''
''' draw shuye
dots = [[221, 432] , [225 , 331] , [133 , 342] , [141 , 310] ,[51 , 230] , [74 , 217] , [58 , 153] , [114 , 164] ,[123 , 135] , [176, 190] , [159 , 77] , [193 , 93],[230 , 28] , [267 , 93], [301 , 77], [284 , 190] ,[327 , 135] , [336 , 164] , [402 , 153] , [386 , 217] ,[409 , 230] , [319 , 310] , [327 , 342] , [233 , 331] ,[237 , 432]]
pygame.draw.lines(screen,[0,250,0],True,dots,1)
for i in range(24):
    pygame.draw.line(screen,[0,250,0],dots[np.random.randint(2,22)],[229,331],1)
'''

my_ball=pygame.image.load("image/ball.jpg")   #87x87
#pygame.transform.resize(my_ball,87,87)
#screen.blit(my_ball,[200,50])
#pygame.display.flip()

#image params
image_length=87
image_width=87



#screen params
screen_width=600
screen_height=800
screen=pygame.display.set_mode([screen_width,screen_height])
screen.fill([255,255,255])

#ball params
i=41
x=50
y=300
x_speed=10
y_speed=7
board_pos=700

#bar params
bar_left=200
bar_top=screen_height-100
bar_width=4
bar_speed=0
bar_speed_step=10
bar_length=200

#def game level
game_level=10

while True:
    pygame.draw.rect(screen,[255,255,255],[bar_left,bar_top,bar_length,bar_width],0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                bar_speed = -bar_speed_step;
               # print "press left"
            if event.key == pygame.K_RIGHT:
                bar_speed = bar_speed_step
                #print "press right"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                bar_speed = 0
            if event.key == pygame.K_RIGHT:
                bar_speed = 0
    pygame.time.delay(10)
    pygame.draw.rect(screen,[255,255,255],[x,y,image_length,image_width],0)

    x=x+x_speed
    y=y+y_speed
    bar_left=bar_left+bar_speed
    if x>screen.get_width() -image_width or x<0:
        x_speed=-x_speed
    if y<0 or y>screen.get_height()-image_width:
        y_speed=-y_speed
    if y>bar_top-image_width and bar_left-image_length<x<bar_left+bar_length:
        y_speed=-y_speed
    if y>screen.get_height()-image_width:
        sys.exit()
    if bar_left <0:
         pygame.draw.rect(screen,[255,100,255],[0,bar_top,bar_length,bar_width],0)
    elif bar_left>screen_width-bar_length:
        pygame.draw.rect(screen, [255, 100, 255], [screen_width-bar_length, bar_top, bar_length, bar_width], 0)
    else:
        pygame.draw.rect(screen,[255,100,255],[bar_left,bar_top,bar_length,bar_width],0)
    screen.blit(my_ball, [x, y])
    pygame.display.flip()

