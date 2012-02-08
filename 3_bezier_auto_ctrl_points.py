import pygame
from pygame.locals import *
import sys
import numpy
from interpylate.interpylate import InterPylate
from interpylate.curve import Curve

def main():
    pygame.init()
    screen=pygame.display.set_mode((500,500),0,24)
    bg=pygame.surface.Surface((500,500),0,24)
    clock=pygame.time.Clock()
    i=Curve("bezier")
    i.set_passthru(((50,250),(450,250)))
    i.set_auto_control()
    steps=2
    points=i.yieldall(60)
    c1,c2=i.get_control()[0],i.get_control()[1]
    print "control",c1,c2
    
    while 1:
        clock.tick(60)
        steps+=1
        if steps==60:
            steps=2
        bg.fill((255,255,255))
        pygame.draw.aalines(bg,(0,0,0),0,points)#list(points[i] for i in range(steps)))
        pygame.draw.aalines(bg,(0,0,0),0,(points[0],points[59]))
        pygame.draw.rect(bg,(255,0,0),Rect(50,250,5,5))
        pygame.draw.rect(bg,(255,0,0),Rect(450,250,5,5))
        pygame.draw.rect(bg,(0,255,0),Rect(c1[0],c1[1],5,5))
        pygame.draw.rect(bg,(0,255,0),Rect(c2[0],c2[1],5,5))
        
        screen.blit(bg,(0,0))
        pygame.display.update()
    
if __name__=="__main__":
    main()