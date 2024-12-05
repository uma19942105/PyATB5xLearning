#method overloading
# Python does not support method loading in the traditiona lmethod
class MathUtils:
    def add(self, a,b):
        return a+b

    def add(self, a=1,b=1,c=1):
        return a+b+c

    def add(self,a=0,b=2, c=5,d=0):
        return a+b+c+d

math = MathUtils()
op1=math.add(1,2)
op2=math.add(1,2,23)
