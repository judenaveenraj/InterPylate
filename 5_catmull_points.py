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
    j=Curve("bezier")    
    i.set_passthru(passing_thrus)
    j.set_passthru(passing_thrus)
    steps=2
    steps1=2
    points=i.yieldall(30)
    points1=j.yieldall(30)
    #c1,c2=i.get_control()[0],i.get_control()[1]
    print "control",i.get_control()
    print "No. of points obtained",len(points)
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
        
        #pygame.draw.aalines(bg,(0,0,0),0,(points[0],points[59]))
        for point in passing_thrus:
            pygame.draw.rect(bg,(255,0,0),Rect(point[0],point[1],5,5))
    #    pygame.draw.rect(bg,(255,0,0),Rect(250,300,5,5))
     #   pygame.draw.rect(bg,(255,0,0),Rect(300,100,5,5))
        for control_pair in i.get_control():
            pygame.draw.rect(bg,(0,255,0),Rect(control_pair[0][0],control_pair[0][1],5,5))
            pygame.draw.rect(bg,(0,255,0),Rect(control_pair[1][0],control_pair[1][1],5,5))
                        
            
        
        screen.blit(bg,(0,0))
        pygame.display.update()
    
if __name__=="__main__":
    main()