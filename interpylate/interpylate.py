
class NumError(Exception):
    def __init__(self,value,correct_num):
        self.param=value
        self.correct_num=correct_num
    def __str__(self):
        #print 'Number of values in each tuple must be the same: Tuple',self.param,'must contain',self.correct_num,'items!!!'
        return str("Number of values in each tuple must be the same: Tuple',self.param,'must contain',self.correct_num,'items!!!")
    
class InterPylate():
    def __init__(self,*val):
        self.val=val
        self.no=len(val[0])
        self.v_no=len(val)
        self.mode=0
        self.steps=0
        self.interval=0.0
        self.num_check(*val)
        print self.no, self.v_no
        
    def num_check(self,*val):
        try:
            for item in val:
                if len(item)!=self.no:
                    raise NumError(item,self.no)
        except NumError,err:
            print err
        
    def set_mode(self,interp_type):
        if interp_type is "linear":
            self.mode=1
    
    def yieldall(self,steps):
        if self.mode is 1:
            return self.LinearYield(steps)
            
    def LinearYield(self,steps):
        print self.val[1][0]-self.val[0][0]
        diff=self.val[1][0]-self.val[0][0]
        self.interval=1.0/steps
        ret=[]
        print self.interval, steps
        while self.steps<=steps:
            a=int(self.val[0][0]*(1-(self.interval*self.steps))+(self.val[1][0]*(self.interval*self.steps)))
            b=int(self.val[0][1]*(1-(self.interval*self.steps))+(self.val[1][1]*(self.interval*self.steps)))
            self.steps+=1
            ret.append((a,b))
        self.interp_done()
        print tuple(ret)
        return tuple(ret)
            
    def interp_done(self):
        self.steps=0
   