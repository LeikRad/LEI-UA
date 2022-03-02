
# This program should find the phase of a fictional substance
# for given temperature and pressure conditions, but it has several bugs!
# 
# a) Try to run the program with Python3 and see what happens.
#    There's a syntax error near the end.  Fix it.
# b) Try again.  It'll crash with a runtime error.  Find the cause and fix it.
# c) There is also a semantic error: for T=300 and P=100, phase should be SOLID.
#    Fix it to agree with the phase diagram.  Test in several conditions!
# d) Adjust the format string to output temperature with 1 decimal place
#    and pressure with 3. 

from typing import get_args


print("Kryptonite phase classifier")

# Input.  (You can fix the runtime error by changing something here!)
T = float(input("Temperature (K)? "))
P = float(input("Pressure (kPa)? "))

if (T < 400):
    if (P < 0.125*T):
        phase = "Gas"
    else:
        phase = "Solid"
else:
    if (P < 50):
        phase = "Gas"
    else:
        phase = "Liquid"


# Output.  (There's a subtle syntax error here!)
print("At {:.1f} K and {:.3f} kPa, Kryptonite is in the {} phase.".format(T, P, phase))

