import numpy
class Curve:
    def __init__(self,mode):
        self.mode=self.__get_mode(mode)
        self.passthru=()
        self.data=[]
        self.control=[]
        
    def set_passthru(self,points):
        self.data=points
        
    def set_control(self,points):
        self.control=points
        
    def __get_mode(self,mode):
        if mode is "bezier":
            print "mode is 1"
            return 1
    
    def set_auto_control(self):
        c1x=((2*self.data[0][0])+self.data[1][0])/3
        c1y=((2*self.data[0][1])+self.data[1][1])/3
        c2x=(2*c1x)-self.data[0][0]
        c2y=(2*c1y)-self.data[0][1]
        self.control=((c1x,c1y),(c2x,c2y))
        
    def get_control(self):
        return self.control
    
    def make_points_with_control(self,t):
        if self.data and self.control:
            bx=(numpy.power((1-t),3)*self.data[0][0])+(3*numpy.power((1-t),2)*t*self.control[0][0])+(3*(1-t)*numpy.power(t,2)*self.control[1][0])+(numpy.power(t,3)*self.data[1][0])
            by=(numpy.power((1-t),3)*self.data[0][1])+(3*numpy.power((1-t),2)*t*self.control[0][1])+(3*(1-t)*numpy.power(t,2)*self.control[1][1])+(numpy.power(t,3)*self.data[1][1])
        return (bx,by)
    
    def yieldall(self,steps):
        if self.mode==1:
            if not self.control:
                self.set_auto_control()
            interv=1.0/(steps-1)
            return tuple(self.make_points_with_control(i*interv) for i in range(steps))
                
            
            