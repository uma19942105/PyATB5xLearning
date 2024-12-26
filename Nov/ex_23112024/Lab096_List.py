#list
 #collection of items
 # they can have different data types
 #python does ot have concept of array
from traceback import print_list

my_list=[1,2,3 ]
my_list1=[1,True,"Pramod",12.34]
print(my_list)

print(my_list)
print(len(my_list))
print(my_list[0])
print(my_list[1])
print(my_list[2])
# print(my_list[4]) # list index out of range


my_list[0] = "Pramod"
my_list[1] = "Dutta"
my_list[2] = "Dutta2"
print(my_list)

print(" -- ")

for item in my_list1:
    print(item)

print(" --- ")

for i in range(1, 5): # range( start, stop-1)
    print(i ,end=" ")

# range(1,5) -> returns List [1,2,3,4]