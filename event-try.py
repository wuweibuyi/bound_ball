# -*-coding=utf-8  -*-

import pygame
import sys
import  random

pygame.init()
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

my_ball=Ball("image/ball.jpg",[10,0],[10,0])
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type ==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                my_ball.rect.top = my_ball.rect.top - 10
            if event.key == pygame.K_DOWN:
                my_ball.rect.top = my_ball.rect.top + 10
    clock.tick(30)
    screen.blit(background,[0,0])
    my_ball.move()
    screen.blit(my_ball.image,my_ball.rect)
    pygame.display.flip()










