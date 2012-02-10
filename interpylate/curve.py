import numpy
class Curve:
    def __init__(self,mode):
        self.mode=self.__get_mode(mode)
        self.passthru=()
        self.num_points=0
        self.data=[]
        self.control=[]
        self.rhs=[]
	
    def set_passthru(self,points):
        self.data=points
        self.num_points=len(points)
        
    def set_control(self,points):
        self.control=points
        
    def __get_mode(self,mode):
        if mode is "bezier":
            print "mode is 1"
            return 1
    
    def set_auto_control(self):
        if self.num_points==2:
            c1x=((2*self.data[0][0])+self.data[1][0])/3
            c1y=((2*self.data[0][1])+self.data[1][1])/3
            c2x=(2*c1x)-self.data[0][0]
            c2y=(2*c1y)-self.data[0][1]
            self.control=((c1x,c1y),(c2x,c2y))
        if self.num_points > 2:
            self.auto_control_multi_bezier()
        
            
    def auto_control_multi_bezier(self):
        n=self.num_points-1
	x=[]
	y=[]	
	
	x.append(self.data[0][0]+(2*self.data[1][0]))
        for i in range(1,n-1):
	    x.append((4*self.data[i][0])+(2*self.data[i+1][0]))
	x.append((8*self.data[n-1][0]+self.data[n][0])/2)
	
	y.append(self.data[0][1]+(2*self.data[1][1]))
	for i in range(1,n-1):
	    y.append((4*self.data[i][1])+(2*self.data[i+1][1]))
	y.append((8*self.data[n-1][1]+self.data[n][1])/2)
	
	x=self.get_first_ctrl_points(x)
	y=self.get_first_ctrl_points(y)
	
	self.control=tuple(rhs)
	   
    def get_first_ctrl_points(self,rhs):
	n = len(rhs)
	x = [0]*n
	tmp = [0]*n
	b = 2.0
	x[0]=rhs[0] / b
	for i in range(1,n):
	    tmp[i] = 1 / b
	    if (i < n-1) :
		b=4.0-tmp[i]
	    else:
		b=3.5-tmp[i]		
	    x[i] = (rhs[i] - x[i - 1]) / b
	for i in range(n):
	    try:
		x[n - i - 1] -= tmp[n - i] * x[n - i]
	    except:
		print x,n,i
		raise
	return x
		
		
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
                
            
            