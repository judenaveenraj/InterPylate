import numpy
import catmull
import bezier

class Curve:
    def __init__(self,mode):
	self.obj=None
        self.mode=self.get_mode(mode)
        self.passthru=()
        self.num_points=0
        self.data=[]
        self.control=[]
        self.rhs=[]
	self.t=[]
	self.result=None
	
	
    def set_passthru(self,points):
	if (self.mode==1):
	    self.obj.set_passthru(points)
	if (self.mode==2):
	    self.obj.set_passthru(points)
        
        
    def set_control(self,points):
	if(self.mode==1):
	    self.obj.control=points
        
    def get_mode(self,mode):
        if mode is "bezier":
            print "mode is 1"
	    self.obj=bezier.Bezier()
            return 1
	if mode is "catmull":
	    print "mode is 2: Catmull Rom"
	    self.obj=catmull.Catmull()
	    return 2
    
    def make_it_easy(self):
	if(self.mode==1):
	    self.obj.set_auto_control()
		
    def get_control(self):
        if (self.mode==1):
	    return self.obj.control

    
    def set_steps(self,steps_tuple):
	self.obj.t=steps_tuple
	
    def yieldall(self,steps=None):
	if steps:
	    self.obj.t=[steps for i in range(len(self.obj.data)-1)]
	print self.obj.t
	if len(self.obj.t) is not (len(self.obj.data)-1):
	    raise BaseException(str(len(self.obj.t))+"Length of interval tuples should (n-1) of number of points")
        
        if self.mode==1:
	    print "made it"
	    return self.obj.yieldall(steps)
	elif self.mode==2:
	    return self.obj.yieldall(steps)
            
    def set_closed(self,c=False):
	try:
	    if c==True:
		if self.mode==2:
		    self.obj.set_closed(1)
		else:
		    raise BaseException, "Cannot perform operation on spline type"
	except BaseException as err:
	    print err
	    raise
	    