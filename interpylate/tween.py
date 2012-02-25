import curve
import numpy
from locals import *
class Tween(curve.Curve):
    def __init__(self,input=None):
        self.fun=None
        self.tween=None
        self.result=[]
        if type(input)==tuple:
            self.type=0
            self.data=input
            self.t=(i for i in range(len(input)))
            
        elif isinstance(input,curve.Curve):
            self.type=1
            self.data=input.result
            self.t=input.t
            self.t=[sum((self.t[j] for j in range(i+1))) for i in range(len(self.t))]
            
            
    def set_tween(self,tween):
        self.tween=tween
        self.fun={
            EASEIN_QUAD: self.easeinquad ,
            EASEOUT_QUAD: self.easeoutquad,
            EASEINOUT_QUAD: self.easeinoutquad,
	    EASEIN_CUBIC: self.easeincubic,
	    EASEOUT_CUBIC: self.easeoutcubic,
	    EASEINOUT_CUBIC: self.easeinoutcubic,
	    
	}
        
    def yieldall(self):
        lb=0
        self.result=[]
        for i in range(len(self.t)):
            print "im in"
            ub=self.t[i]
            dur=ub-lb
            print lb,ub
            try:
                for n in range(dur):
                    self.result.append(self.data[self.fun[self.tween](n,lb,ub,dur)])
            except IndexError:
                self.result.append(self.t[len(self.t)-1])
            lb=ub
        return self.result
    
    def easeinquad(self,t,b,c,d):
        t/=float(d)
	return int(numpy.round( d* (t*t) + b ))
    
    def easeoutquad(self,t,b,c,d):
        t/=float(d)
        return int(numpy.round( (d) * (-( (t-1)*(t-1)) + 1) + b))
    
    def easeinoutquad(self,t,b,c,d):
	t/=float(d/2)
	print "t:",t
        if (t < 1):
	    return int(numpy.round(d/2 * (t*t) + b))
	t=t-1
	return int(numpy.round( d/2 * (-((t-1)*(t-1)) + 1) + b + d/2))
    
    def easeincubic(self,t,b,c,d):
        t/=float(d)
        print (d*t*t*t)+ b, t, c ,b ,d, c*t*t
        return int(numpy.round(d*(t*t*t)+b))
    
    def easeoutcubic(self,t,b,c,d):
        t/=float(d)
        return int(numpy.round(d* (((t-1)*(t-1)*(t-1)) + 1) + b))
    
    def easeinoutcubic(self,t,b,c,d):
	t/=float(d/2)
	if (t < 1):
	    return int(numpy.round(d/2*t*t*t + b))
	t=t-1
	return int(numpy.round( (d/2*(((t-1)*(t-1)*(t-1)) + 1)) + b + d/2))
    
    