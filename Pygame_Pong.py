#-*-coding:utf8-*-
#qpy:pygame
"""
Pygame support is builtin from QPython >= 2.4.0

Create by: Jonatha Rihan da Silva


"""

import sys
import pygame
from pygame.locals import *
import random

pygame.init()
screen = pygame.display.set_mode((720, 1280))
clock = pygame.time.Clock()
myfont1 = pygame.font.SysFont("DejaVuSans", 64)
myfont2 = pygame.font.SysFont("DejaVuSans", 128)
myfont3 = pygame.font.SysFont("DejaVuSans", 32)
myfont4 = pygame.font.SysFont("DejaVuSans", 16)
myfont5 = pygame.font.SysFont("DejaVuSans", 32)

def Menu():
    value = 11
    r,g,b = value,value,value

    color_r = 85
    color_g = 170
    color_b = 255


    while True:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()

            if ev.type == MOUSEBUTTONDOWN:
                pass
            if ev.type == MOUSEBUTTONUP:
                Game()
        clock.tick(60)
        screen.fill((0, 0, 0))


        label2 = myfont2.render("{}".format("PONG GAME"), 1, (color_r, color_g, color_b ))
        label2 = pygame.transform.rotate(label2, 90)
        label3 = myfont3.render("{}".format("Press on screen to start"), 1, (255, 255, 255))
        label3 = pygame.transform.rotate(label3, 90)
        label4 = myfont4.render("{}".format("Made by: Jonathan Ryan"), 1, (255, 255, 255))
        label4 = pygame.transform.rotate(label4, 90)



        screen.blit(label2, (150,240))
        screen.blit(label3, (300,440))
        screen.blit(label4, (600,100))

        if(color_r >= 240):
            r=-value
        if(color_r <= 10):
            r=value

        if(color_g >= 240):
            g=-value
        if(color_g <= 10):
            g=value

        if(color_b >= 240):
            b=-value
        if(color_b <= 10):
            b=value


        color_r += r
        color_g += g
        color_b += b



        pygame.display.update()


def Game():

#Variables
    vel=10
    vel_player = vel
    vel_ball = vel
    pos_ball_x = 360
    pos_ball_y = 640
    vel_ball_x = vel_ball
    vel_ball_y = vel_ball
    pos_player_x = 0
    pos_bot_x = 0
    vector=-10
    vector_bot = vel
    player_point = 0
    bot_point = 0

#Loop/Player Command

    while True:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()

            if ev.type == MOUSEBUTTONDOWN:
                vector = 10
            if ev.type == MOUSEBUTTONUP:
                vector = -10
#Ball Setup

        if(pos_ball_x >= 700):
            vel_ball_x = -vel_ball
        if(pos_ball_x <= 20):
            vel_ball_x = vel_ball

#Player Setup

        if(pos_player_x >= 420):
            pos_player_x = 420
        if(pos_player_x <= 0):
            pos_player_x = 0

#Bot Setup

        if(pos_bot_x >= 420):
            pos_bot_x = 420
        if(pos_bot_x <= 0):
            pos_bot_x = 0

        if(pos_bot_x == pos_ball_x-150):
            vector_bot = 0
        if(pos_bot_x > pos_ball_x-150):
            vector_bot = -vel
        if(pos_bot_x < pos_ball_x-150):
            vector_bot = vel



#Colision Player/Bot Setup
        
        if(pos_ball_x > pos_player_x):
            if(pos_ball_x < pos_player_x+300):
                if(pos_ball_y in range(1211,1241)):
                    vel_ball_y=-vel_player
                    vel_ball += 1.0
        if(pos_ball_x > pos_bot_x):
            if(pos_ball_x < pos_bot_x+300):
                if(pos_ball_y in range(50,70)):
                    vel_ball_y=vel_player
                    vel_ball += 1.0


#Time and Background        
        clock.tick(60)
        screen.fill((0, 0, 0))

#Reset
        if(pos_ball_y > 1280): 
            bot_point += 1
            pos_ball_x = 360
            pos_ball_y = 640
            vel_ball_x = vel_ball * random.choice([-1,1])
            vel_ball_y = vel_ball * random.choice([-1,1])
            vel_ball = vel
        if(pos_ball_y < 0):
            player_point += 1
            pos_ball_x = 360
            pos_ball_y = 640
            vel_ball_x = vel_ball * random.choice([-1,1])
            vel_ball_y = vel_ball * random.choice([-1,1])
            vel_ball = vel

#Objects
        pygame.draw.line(screen, (255,255,255), [720, 640], [0,640], 5) 
        pygame.draw.rect(screen,(255,255,255),[pos_bot_x,20,300,30])    
        pygame.draw.rect(screen,(255,255,255),[pos_player_x,1230,300,30])    
        pygame.draw.circle(screen, (255,255,255), [pos_ball_x, pos_ball_y], 20)

#Moves
        pos_ball_x += vel_ball_x
        pos_ball_y += vel_ball_y
        pos_player_x += vector
        pos_bot_x += vector_bot
        label1 = myfont1.render("{}                             {}".format(player_point,bot_point), 1, (255, 255, 255))
        label1 = pygame.transform.rotate(label1, 90)
        label5 = myfont5.render("{}x".format((vel_ball)-9), 1, (255, 255, 255))
        label5 = pygame.transform.rotate(label5, 90)
        screen.blit(label5, (0,100))
        screen.blit(label1, (0,300))
        pygame.display.update()

Menu()
