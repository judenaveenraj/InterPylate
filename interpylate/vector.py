import numpy

class Vector():
    def __init__(self,p1,p2):
        self.x=p2[0]-p1[0]
        self.y=p2[1]-p1[1]
        self.d=numpy.sqrt(numpy.sum([numpy.square(self.x),numpy.square(self.y)]))
        self.ux=self.x/self.d
        self.uy=self.y/self.d
        
    def get_unit_vector(self):
        return (self.ux,self.uy)
    
def reverse_vector(v):
    return (v[0]*-1,v[1]*-1)
    
def make_point_from_vector(p,uv,d):
    """
    Function returns point obtained from applying
    unit vector 'uv' to source point 'p' at a distance 'd'
    """
    return (p[0]+(uv[0]*d),p[1]+(uv[1]*d))
