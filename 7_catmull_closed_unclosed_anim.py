import pygame
from pygame.locals import *
import sys
import numpy
from interpylate.interpylate import InterPylate
from interpylate.curve import Curve

def main():
    pygame.init()
    passing_thrus=((240,300),(230,50),(340,218),(348,487), \
            (150,200),(278,245),(453,385),(140,238),(240,300))
    screen=pygame.display.set_mode((500,500),0,24)
    bg=pygame.surface.Surface((500,500),0,24)
    clock=pygame.time.Clock()
    i=Curve("catmull")
    k=Curve("catmull")
    i.set_passthru(passing_thrus)
    k.set_passthru(passing_thrus)
    #Set Curve 'k' to be a closed curve
    k.set_closed(True)
    steps=2
    steps1=2
    points=i.yieldall(60)
    points1=k.yieldall(60)
    #c1,c2=i.get_control()[0],i.get_control()[1]
    print "control",i.get_control()
    print "No. of points obtained",len(points)
    while 1:
        clock.tick(60)
        steps+=1
        if steps==len(points):
            steps=2

        
        bg.fill((255,255,255))
        
        pygame.draw.aalines(bg,(255,0,0),0,list(points[i] for i in range(steps)))
        pygame.draw.aalines(bg,(0,255,0),0,list(points1[i] for i in range(steps)))
        
        pygame.draw.aalines(bg,(255,0,0),0,((0,500),points[steps]))
        pygame.draw.aalines(bg,(0,255,0),0,((500,0),points1[steps]))
        
        for point in passing_thrus:
            pygame.draw.rect(bg,(255,0,0),Rect(point[0],point[1],5,5))
        
        screen.blit(bg,(0,0))
        pygame.display.update()
    
if __name__=="__main__":
    main()