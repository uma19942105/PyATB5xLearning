#method overloading is not supported
class Calc:


    #*arg= multiple arguments
    def sum(self,*args):
        for a in args:
            print(a)

calc_ref=Calc()
result = calc_ref.sum(3,4)
result = calc_ref.sum(1, 2)
result = calc_ref.sum(1,2,3)
print(result)

#when it does not return anything
calc_ref =Calc()
calc_ref.sum(1)
print("multiple arg")
calc_ref.sum(1, 2)
print("multiple arg")
calc_ref.sum(1,2,3)