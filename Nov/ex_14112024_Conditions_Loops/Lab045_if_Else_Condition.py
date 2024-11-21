#problem to find the max between 2
#logic building formula
#1. user inputs-> 2 integers
#2. o/p -> int 1 which ever is greate max  n umber it will  return
#3.31.4 or 45.34- floart
num1=float(input("Enter num1=\n"))
num2=float(input("Enter num2=\n"))
if num1>num2:
    print("num1 is greater")
else:
    print("num2 is greater")

    #edge cases found by tester only
    #if both are equal
    # if a string is entered ( wil handle in future)
    # -ve value
    #checking the -ve numbers,strings what is the output