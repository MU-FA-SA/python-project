import pygame
import math
from pygame.locals import *
#Initialize the game 
pygame.init()
width,height = 760,660
screen = pygame.display.set_mode((width,height))
keys = [False,False,False,False]
playerpos = [100,100]
acc = [0,0]
arrows=[]

#3= load images
player = pygame.image.load(r'C:\Users\SONY\Desktop\pycodes\download.png')
arrow = pygame.image.load(r'C:\Users\SONY\Desktop\pycodes\virus.png')
castle = pygame.image.load(r'C:\Users\SONY\Desktop\pycodes\cp9y.png')

#4-keep loop through
while 1:
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         pygame.quit()
            # quit()
    screen.blit(castle,(0,0))
    screen.blit(player,playerpos)
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
    playerrot = pygame.transform.rotate(player,360-angle*57.29)
    playerpos1 =(playerpos[0]-playerrot.get_rect().width/2,playerpos[1]-playerrot.get_rect().height/2)
    screen.blit(playerrot,playerpos1)
    for bullet in arrows:
        index=0
        velx=math.cos(bullet[0])*10
        vely=math.sin(bullet[0])*10
        bullet+=velx
        bullet+=vely
        if bullet[1]<-64 or bullet>640 or bullet[2]<-64 or bullet>480:
            arrow.pop(index)
            index+=1
for projectile in arrows:
            arrow1 =pygame.transform.rotate(arrow,360-projectile[0]*57.29)
            screen.blit(arrow1,(projectile[1],projectile[2]))
pygame.display.flip()
for event in pygame.event.get():
    if event.type ==pygame.QUIT:
        pygame.quit()
        exit(0)
    if even.type==KEYDOWN:
        if event.key == k_w:
            key[0]=True
        elif event.key ==k_a:
            key[1]== True
        elif event.key ==k_s:
            key[2]== True
        elif event.key ==k_d:
            key[3]== True
    if even.type==KEYUP:
        if event.key == k_w:
            key[0]==False
        elif event.key ==k_a:
            key[1]== False
        elif event.key ==k_s:
            key[2]== False
        elif event.key ==k_d:
            key[3]== False
if key[0]:
    playerpos[1]-=1
elif key[2]:
    playerpos[1]+=1
if key[1]:
    playerpos[0]-=1
elif key[3]:
    playerpos[0]+=1
if event.type==pygame.MOUSEBUTTONDOWN:
    position=pygame.mouse.get_pos()
    acc[1]+=1
    arrows.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])
