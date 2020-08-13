"""
Lauren Ingram
ENTD200 Winter 2017
Instructor: ****** *****
Week 6
Completed April 13, 2017

Original Project Requirements:
Problem 1: Write a program that will calculate the problem and stop after the condition has been met.

a=number of loops (start with zero but will increase by 1 after each completed loop)
b=a+1
c=a+b

Condition: If c is less than 5, then the loop will continue; else, it will end.
Print a string variable that states the number of loops required to meet the condition for Problem 1."""
a=1
c=0

while c < 5:
    
    print (c, " is less than 5")
    b = a + 1
    c = a + b
    a = a + 1

else:
   print (c, " is not less than 5")
   print (a, "loops completed")

