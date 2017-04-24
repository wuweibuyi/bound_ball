# -*-coding=utf-8  -*-

import pygame
import sys
import  random

pygame.init()
delay=100
interval=50
pygame.key.set_repeat(delay,interval)
screen=pygame.display.set_mode([640,480])
background=pygame.Surface(screen.get_size())
background.fill([255,255,255])
clock=pygame.time.Clock()


class Ball(pygame.sprite.Sprite):
    def __init__(self,image_file,location,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(image_file)
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=location
        self.speed =speed

    def move(self):
        if self.rect.left < screen.get_rect().left or \
                        self.rect.right>screen.get_rect().right:
            self.speed[0]=-self.speed[0]
      #  if self.rect.top < screen.get_rect().top or \
      #                  self.rect.bottom >screen.get_rect().bottom:
       #     self.speed[1]=-self.speed[1]
        newpos=self.rect.move(self.speed)
        self.rect=newpos

my_ball=Ball("image/ball.jpg",[10,0],[0,0])
held_down=False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            #print "ball center is ",my_ball.rect.center
            if  my_ball.rect.center[0]-30< event.pos[0]<my_ball.rect.center[0]+30 and \
                                            my_ball.rect.center[1]-30<event.pos[1]<my_ball.rect.center[1]+30:
                held_down=True
            #print "mouse is here: ", event.pos
            #print "held_down is ", held_down
        elif event.type==pygame.MOUSEBUTTONUP:
            held_down=False
        elif event.type==pygame.MOUSEMOTION:
            if held_down:
                my_ball.rect.center=event.pos
    clock.tick(30)
    screen.blit(background,[0,0])
    my_ball.move()
    screen.blit(my_ball.image,my_ball.rect)
    pygame.display.flip()










