import vector
import numpy

class Catmull():
    def __init__(self):
        self.data=[]
        self.length=0
        self.closed=0
        self.result=[]
        
    def set_passthru(self,points):
        self.data,self.length=points,len(points)
        if self.data[0]==self.data[self.length-1]:
            self.closed=1
        
    def yieldall(self,steps):
        for i in range(len(self.data)-1):
            self.build_curve_2pts(i,steps)
        return self.result

    def build_curve_2pts(self,i,steps):
        """
        Function to create control points p0 and p3. and to call curve_points() 
        with appropriate intervals of t
        """
        p1=self.data[i]
        p2=self.data[i+1]
        a=vector.Vector(p1,p2)
        a=a.get_unit_vector()
        if i == 0:
            ra=vector.reverse_vector(a)
            #Creating imaginary points p3,p0 at distance 10 for controls
            p0=vector.make_point_from_vector(p1,ra,10)
        else:
            p0=self.data[i-1]
        if (i+2) > (self.length-1):
            p3=vector.make_point_from_vector(p2,a,10)
        else:
            p3=self.data[i+2]
            
        #Get the intervals of 't'
        interv=1.0/(steps-1)
        for i in range(steps):            
            self.add_points(p0,p1,p2,p3,interv*i)
        
        
    def add_points(self,p0,p1,p2,p3,t):
        mat0=numpy.matrix([1.0,t,t*t,t*t*t])
        
        mat1=numpy.matrix([[0,2,0,0],    \
                           [-1,0,1,0],   \
                           [2,-5,4,-1],  \
                           [-1,3,-3,1]])
        mat2x=numpy.matrix([[p0[0]], \
                          [p1[0]], \
                          [p2[0]], \
                          [p3[0]]])
        mat2y=numpy.matrix([[p0[1]], \
                          [p1[1]], \
                          [p2[1]], \
                          [p3[1]]])
        rx=0.5*mat0*mat1*mat2x
        ry=0.5*mat0*mat1*mat2y
        temp=(rx,ry)
        self.result.append(temp)
            