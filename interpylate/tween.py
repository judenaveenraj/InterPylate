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
            EASEIN: self.easein ,
            #EASEOUT: self.easeout,
            #EASEINOUT: self.easeinout,
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
    
    def easein(self,t,b,c,d):
        t/=d*1.0
        print (d*t*t)+ b, t, c ,b ,d, c*t*t
        return int(numpy.round(d*t*t+b))