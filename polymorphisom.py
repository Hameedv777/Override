class sum:
    def __init__(self,fnum,snum):
        self.fn=fnum
        self.sn=snum
    def Display(self):
        print("Sum is ", self.fn+self.sn)
class Deffrnt:
    def __init__(self,fnum,snum) :
        self.fn=fnum
        self.sn=snum
    def Display(self):
        print("Diffrence is ", self.fn-self.sn)
class Multiply:
    def __init__(self,fnum,snum) :
        self.fn=fnum
        self.sn=snum
    def Display(self):
        print("Value  Mutiplcation ",self.fn*self.sn)
class Division:
    def __init__(self,fnum,snum) :
        self.fn=fnum
        self.sn=snum
    def Display(self):
        print("Divion result  is " ,self.fn/self.sn)
x=sum(10,20)
x.Display()
y=Deffrnt(20,5)
y.Display()
z=Multiply(20,5)
z.Display()
a=Division(20,5)
a.Display()


        




        
            

        
