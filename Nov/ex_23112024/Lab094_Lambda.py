#write program to calculate even or odd
def find_even_odd(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")

find_even_odd(5)
n=int(input("Enter number\n"))
check_even_odd =lambda num:"Even" if num%2==0 else "odd"
print(check_even_odd(17))
