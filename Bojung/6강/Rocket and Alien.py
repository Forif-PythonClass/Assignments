# 1 - Import library
import pygame
from pygame.locals import *

# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
keys = [False, False]
rocketpos = [320, 400]
alienpos = [320,10]
bulletpos =[]
alienRorL = True # true=right/false=left
clock = pygame.time.Clock()
FRAMES_PER_SECOND = 10
deltat = clock.tick(FRAMES_PER_SECOND)

# 3 - Load images
rocket = pygame.image.load("resources/image/rocket.png")
alien = pygame.image.load("resources/image/alien.png")
bullet = pygame.image.load("resources/image/bullet.png")

# 4 - keep looping through
while 1 :
     screen.fill(0)
     deltat
     screen.blit(alien,alienpos)
     screen.blit(rocket,rocketpos)
     pygame.display.flip()

     if alienRorL == True :
          if alienpos[0] < 620:
               alienpos[0] = alienpos[0] + .2
          else :
               alienRorL = False
     if alienRorL == False :
          if alienpos[0] > 15 :
               alienpos[0] = alienpos[0] - .2
          else :
               alienRorL = True   
     
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               pygame.quit()
               exit(0)
          if event.type == pygame.KEYDOWN:
               if event.key==K_RIGHT:
                    keys[0]=True
               elif event.key==K_LEFT:
                    keys[1]=True
               elif event.key==K_SPACE:
                    
          if event.type == pygame.KEYUP:
               if event.key==pygame.K_RIGHT:
                    keys[0]=False
               elif event.key==pygame.K_LEFT:
                    keys[1]=False
                    

     if keys[0]:
          rocketpos[0]+=.2
     elif keys[1]:
          rocketpos[0]-=.2
               
