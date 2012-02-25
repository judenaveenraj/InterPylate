import numpy

class Bezier():
    def __init__(self):
        self.data=[]
        self.control=[]
	self.num_points=0
	self.t=[]
	self.result=[]
	
	
    def set_passthru(self,points):
        self.data=points
        self.num_points=len(points)
        
    def yieldall(self,steps):
	if not self.control:	   
	    self.set_auto_control()
	    
	#For only two points and bezier and with control points
	if len(self.data) == 2:
	    step=self.t[0]
	    interv=1.0/(step-1)
	    self.result=tuple(self.make_points_with_control(i*interv) for i in range(step))
	    
	#For more than two points and bezier and with control points
	elif (len(self.data)>2):
	    #for step in self.t:
	    #			interv=1.0/(step-1)
	    for c in range(len(self.data)-1):
		step=self.t[c]
		interv=1.0/(step-1)
		for i in range(step):
		    self.result.append(self.make_points_with_control(i*interv,c))
	print "res",self.result
	return tuple(self.result)
    
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
	"""Called when multiple points are present, 
	bezier requested, without control points
	"""
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
	fcp=[]
	scp=[]
	rhs=[]
	for i in range(n):
	    #First Control Points
	    fcp.append((x[i],y[i]))
	    #Second Control Points
	    if (i<(n-1)):
		temp=(2*self.data[i + 1][0] - x[i + 1], 2*self.data[i + 1][1] - y[i + 1])
		scp.append(temp)
	    else:
		temp=((self.data[n][0] + x[n - 1]) / 2, (self.data[n][1] + y[n - 1]) / 2)
		scp.append(temp);
	for a,b in zip(fcp,scp):
	    rhs.append((a,b))
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
	for i in range(1,n):
	    try:
		x[n - i - 1] -= tmp[n - i] * x[n - i]
	    except:
		print x,n,i
		raise
	return x
	
    def make_points_with_control(self,t,point_id=-1):	
        if self.data and self.control:
	    
	    if (point_id == -1):
		bx=(numpy.power((1-t),3)*self.data[0][0])+(3*numpy.power((1-t),2)
                            *t*self.control[0][0])+(3*(1-t)*numpy.power(t,2)*
		            self.control[1][0])+(numpy.power(t,3)
                            *self.data[1][0])
		by=(numpy.power((1-t),3)*self.data[0][1])+(3*numpy.power((1-t),2)
		            *t*self.control[0][1])+(3*(1-t)*numpy.power(t,2)*
		            self.control[1][1])+(numpy.power(t,3)
		                *self.data[1][1])
	    if (point_id >= 0):
		data=[self.data[point_id],self.data[point_id+1]]
		control=self.control[point_id]
		bx=(numpy.power((1-t),3)*data[0][0])+(3*numpy.power((1-t),2)
		                                      *t*control[0][0])+(3*(1-t)*numpy.power(t,2)*control[1][0])+(numpy.power(t,3)*data[1][0])
		by=(numpy.power((1-t),3)*data[0][1])+(3*numpy.power((1-t),2)
		                                      *t*control[0][1])+(3*(1-t)*numpy.power(t,2)*control[1][1])+(numpy.power(t,3)*data[1][1])
	#print bx,by
	temp=(bx,by)
        return temp