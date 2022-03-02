# coding: utf-8
# This program finds the maximum of two numbers.
# It uses the built-in max function.
# Can you do it with conditional statements (if / if-else) instead?

x1 = float(input("number? "))
x2 = float(input("number? "))
x3 = float(input("number? "))

# Use conditional statements instead of max function!
#if (x1 > x2):
#    tempX = x1
#else:
#    tempX = x2

#if (tempX > x3):
#    mx = tempX
#else:
#    mx = x3

#print("Maximum:", mx)
#

mx=x1

if(mx < x2):
    mx = x2
if(mx < x3):
    mx = x3

print(mx)