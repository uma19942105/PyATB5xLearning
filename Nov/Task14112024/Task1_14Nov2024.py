#Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides, determine if the triangle is equilateral
# (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.
#below is my task
len1= int(input("Length of side A"))
len2= int(input("Length of side B"))
len3= int(input("Length of side C"))
if len1==len2 and len1==len3 and len2==len3:
    print("Equilateral")
elif (len2>len1 and len2==len3 or len2>len3 and len3==len1 or len3>len1 and len1==len2 or
      len3>len2 and len2==len1 or len1>len2 and len2==len3 or len3>len2 and len2==len1):
    print("isosceles")
else:
     print("scalene")

# Task explained by Promod in class:
