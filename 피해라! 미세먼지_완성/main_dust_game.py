# 1 - Import library
import pygame
import time
import random
import sys
from pygame.locals import *

# 2 - Initialize the game
pygame.init()
screen=pygame.display.set_mode((640, 480))
keys = [False, False, False, False]
pygame.display.set_caption('We need clean air')
black = (0,0,0)
white = (255,255,255)
red = (255,25,25)

# About Frame
clock = pygame.time.Clock()
FRAMES_PER_SECOND = 10
playerpos=[100,100]

# About timer
font = pygame.font.Font(None, 38)
t0=pygame.time.get_ticks()

#About dust
dustnum = 2
dustpos=[[random.uniform(0,640),random.uniform(0,320)] for i in range(dustnum)]

# 3 - Load images
background = pygame.image.load("resources/background.jpg").convert()
player = pygame.image.load("resources/metamon.png")
clock1 = pygame.image.load("resources/clock.png")
Clock = pygame.transform.scale(clock1,(55,55))
dust = pygame.image.load("resources/dust.png")

Win = pygame.image.load("resources/win.png")
win = pygame.transform.scale(Win,(600,350))
GG = pygame.image.load("resources/gameover.png")
gg = pygame.transform.scale(GG,(500,270))


# 3.1 - Load audio
fail = pygame.mixer.Sound("resources/gamefail.wav")
success = pygame.mixer.Sound("resources/gamesuccess.wav")
fail.set_volume(1)
success.set_volume(1)
pygame.mixer.music.load("resources/bgm.mp3")
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.15)


# 4 - keep looping through
running = 1
exitcode = 0
while running:
    # 5 - clear the screen before drawing it again
    screen.fill((255,255,255))
    clock.tick(FRAMES_PER_SECOND)
    # 6 - draw the screen elements
    screen.blit(background,(0,0))
    screen.blit(player,playerpos)
    screen.blit(Clock,[575,10])
    
    
    # 6.1 - timer
    t1=pygame.time.get_ticks()
    seconds=int(60-(t1-t0)/1000)
    if seconds<0:
        seconds=0
        t0=t1
    text=font.render(str(seconds),True,(0,0,0))
    screen.blit(text,[587,27])


    # 6.3 - Dust
    for pos in dustpos:
          screen.blit(dust,pos)
    for move in dustpos:
          move[0]+=random.uniform(-50,50)
          move[1]+=random.uniform(-50,50)
    for check in dustpos:
          if check[0] >= 620 :
               while check[0] >= 620 :
                    check[0]-=30
          if check[0] <= 0 :
               while check[0] <= 0 :
                    check[0]+=30
          if check[1] >= 450 :
               while check[1] >= 450 :
                    check[1]-=20
          if check[1] <= 0 :
               while check[1] <= 0 :
                    check[1]+=20


    # 7 - update the screen
    pygame.display.flip()
    
    # 8 - loop through the events
    for event in pygame.event.get():
        if event.type== QUIT or (event.type ==KEYDOWN and event.key == K_ESCAPE):
            pygame.quit() 
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key==K_UP:
                keys[0]=True
            if event.key==K_DOWN:
                keys[1]=True
            if event.key==K_LEFT:
                keys[2]=True
            if event.key==K_RIGHT:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_UP:
                keys[0]=False
            if event.key==pygame.K_DOWN:
                keys[1]=False
            if event.key==pygame.K_LEFT:
                keys[2]=False
            if event.key==pygame.K_RIGHT:
                keys[3]=False

    # 9 - Move player
    if keys[0]:
        playerpos[1]-=25
    elif keys[1]:
        playerpos[1]+=25
    if keys[2]:
        playerpos[0]-=25
    elif keys[3]:
        playerpos[0]+=25
    if playerpos[0]<0:
        playerpos[0]+=25
    elif playerpos[0]>620:
        playerpos[0]-=25
    if playerpos[1]<0:
        playerpos[1]+=25
    elif playerpos[1]>450:
        playerpos[1]-=25

    # 10 - Collision
    playerrect=pygame.Rect(player.get_rect())
    playerrect.left=playerpos[0]
    playerrect.top=playerpos[1]


    for d_rect in dustpos:
        dustrect=pygame.Rect(dust.get_rect())
        dustrect.left=d_rect[0]
        #height 조정
        dustrect.top=d_rect[1]

        if dustrect.colliderect(playerrect):
            exitcode = 1
            running = 0


    #11 - Win/Lose check 60초 지나면 클리어
    if pygame.time.get_ticks()>=60000:
        running=0    #60초가 지나면 #4의 running의 값을 0으로 바꿔줍니다.
        exitcode=0

if exitcode == 1:#exitcode가 1인 경우는 먼지와 플레이어가 부딪혔을때 게임오버를 표시하기위해서 설정했습니다.
    screen.blit(gg,(72,110))
    pygame.mixer.music.stop()
    fail.play()
elif exitcode==0:
    screen.blit(win,(30,70))
    pygame.mixer.music.stop()
    success.play()
    
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()
