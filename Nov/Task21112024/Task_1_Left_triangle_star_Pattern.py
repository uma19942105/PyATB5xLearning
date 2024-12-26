
"""for i in range(0,5):
    for j in range(0,i+1):
        print("*", end='')
    print()"""

for i in range(1,6):
    for k in range(9-i):
        print(" ",end="")
    for l in range(i):
        print("*",end="")
    print()