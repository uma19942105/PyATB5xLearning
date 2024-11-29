from Nov.ex_19112024_Functions.Lab069_Functions_IQ import result
"""""
print (float(input("enter value for num1")))
print (float(input("enter value for num2")))
print (float(input("enter value for num3")))

def sum_three(num1=100,num2=200,num3=300):
        return num1+num2+num3
                 
                    result = sum_three(num1, num2, num3)
                
                     print(result)
                 result2=sum_three(n1,n2,n3)
print("sum is", result2)"""


def sum_of_three_default(num1=100, num2=200, num3=300):
    return num1 + num2 + num3


result = sum_of_three_default()
print(result)

num1 = int(input("enter num1 value"))
num2 = int(input("enter num2 value"))
num3 = int(input("enter  num3 value"))


def sum_three(n1=100, n2=200, n3=300):
    return n1 + n2 + n3


result = sum_three(num1, num2, num3)
print(result)