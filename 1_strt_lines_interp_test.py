import pygame
from pygame.locals import *
import sys
from interpylate.interpylate import InterPylate

def main():
    pygame.init()
    screen=pygame.display.set_mode((500,500),0,24)
    bg=pygame.surface.Surface((500,500),0,24)
    clock=pygame.time.Clock()
    print dir(InterPylate)
    i=InterPylate((450,445),(53,384),(2,3))
    i1=InterPylate((35,100),(487,384),(2,3))
    i2=InterPylate((200,300),(345,23),(2,3))
    i3=InterPylate((450,10),(53,314),(2,3))
    i4=InterPylate((480,100),(187,244),(2,3))
    i5=InterPylate((500,300),(341,68),(2,3))
    i.set_mode("linear")
    i1.set_mode("linear")
    i2.set_mode("linear")
    i3.set_mode("linear")
    i4.set_mode("linear")
    i5.set_mode("linear")
    steps=2
    points=i.yieldall(60)
    points1=i1.yieldall(60)
    points2=i2.yieldall(60)
    points3=i3.yieldall(60)
    points4=i4.yieldall(60)
    points5=i5.yieldall(60)
    while 1:
        clock.tick(60)
        steps+=1
        if steps==60:
            steps=2
        bg.fill((255,255,255))
        pygame.draw.aalines(bg,(0,0,0),0,list(points[i] for i in range(steps)))
        pygame.draw.aalines(bg,(0,0,0),0,list(points1[i] for i in range(steps)))
        pygame.draw.aalines(bg,(0,0,0),0,list(points2[i] for i in range(steps)))
        pygame.draw.aalines(bg,(0,0,0),0,(points3[0],points3[steps]))
        pygame.draw.aalines(bg,(0,0,0),0,(points4[0],points4[steps]))
        pygame.draw.aalines(bg,(0,0,0),0,(points5[0],points5[steps]))
        
        screen.blit(bg,(0,0))
        pygame.display.update()
    
if __name__=="__main__":
    main()