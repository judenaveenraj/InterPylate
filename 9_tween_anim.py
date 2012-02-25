import pygame
from pygame.locals import *
import sys
import numpy
from interpylate.interpylate import InterPylate
from interpylate.curve import Curve
from interpylate.tween import Tween
from interpylate.locals import *

def main():
    pygame.init()
    passing_thrus=((240,300),(230,50),(340,218),(348,487), \
            (150,200),(278,245),(453,385),(140,238),(240,300))
    screen=pygame.display.set_mode((500,500),0,24)
    bg=pygame.surface.Surface((500,500),0,24)
    clock=pygame.time.Clock()
    i=Curve("bezier")
    j=Curve("bezier") 
    i.set_passthru(passing_thrus)
    j.set_passthru(passing_thrus)
    steps=2
    steps1=2
    points=i.yieldall(60)
    #j.set_steps((20,50,20,100,50,150,30,60))
    points1=j.yieldall(60)
    twe=Tween(j)
    twe.set_tween(EASEIN)
    points1=twe.yieldall()
    #print points1
    #c1,c2=i.get_control()[0],i.get_control()[1]
    print "control",i.get_control()
    print "No. of points obtained",len(points)
    print "No. of points1 obtained",len(points1)
        
    
    while 1:
        clock.tick(60)
        steps+=1
        if steps==len(points):
            steps=2
        steps1+=1
        if steps1==len(points1):
            steps1=2
        
        bg.fill((255,255,255))
        
        pygame.draw.aalines(bg,(255,0,0),0,list(points[i] for i in range(steps)))
        pygame.draw.aalines(bg,(0,0,0),0,list(points1[i] for i in range(steps1)))
        
        pygame.draw.aalines(bg,(255,0,0),0,((0,500),points[steps]))
        pygame.draw.aalines(bg,(0,0,0),0,((0,500),points1[steps1]))

        for point in passing_thrus:
            pygame.draw.rect(bg,(255,0,0),Rect(point[0],point[1],5,5))
    # 
        
        screen.blit(bg,(0,0))
        pygame.display.update()
    
if __name__=="__main__":
    main()