# -*- coding-utf-8 -*-

import  pygame
import sys
import math
from random import *



class MyBallClass(pygame.sprite.Sprite):

    def __init__(self,iamge_file,location,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(iamge_file)
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top = location
        self.speed=speed

    def move(self):
        self.rect=self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right>screen_width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom> screen_height:
            self.speed[1] = -self.speed[1]

def animate(group):
    screen.fill([255,255,255])
    for ball in group:
        ball.move()
    for ball in group:
        group.remove(ball)
        if pygame.sprite.spritecollide(ball,group,False):
            ball.speed[0]=-ball.speed[0]
            ball.speed[1]=-ball.speed[1]
        group.add(ball)
        screen.blit(ball.image,ball.rect)
    pygame.time.delay(game_level)
    pygame.display.flip()



screen_size=screen_width,screen_height=640,480
screen=pygame.display.set_mode(screen_size)
screen.fill([255,255,255])
image_file="image/ball.jpg"
#balls=[]
speed=[2,3]
game_level=10
group = pygame.sprite.Group()
for row in range(0,2):
    for colum in range(0,2):
        location=[colum*130+10,row*164+10]
        speed=[choice([-2,2]),choice([-2,2])]
        ball = MyBallClass(image_file,location,speed)
        group.add(ball)


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    animate(group)
































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

