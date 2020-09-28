"""
The time in seconds that a pendulum takes to swing
back and forth once is given by this formula:
             ____
            / n
    t = 2π / ----
          √  9.81

where t is the time in seconds,
π is PI the ratio of the circumference divided by
    the diameter of a circle (use math.pi), and
n is the length of the pendulum in meters.

Write a program that prompts a user to enter the length of a
pendulum in meters and then computes and prints the time in
seconds that it takes for that pendulum to swing back and forth.
"""

# Enable math module. 

import math

# Receive input from user for length of the pendulum.

n = float(input('Length of pendulum (meters): '))

# Compute time to swing back and forth.

t = 2 * math.pi * math.sqrt(n / 9.81)

print(f'{t:10.2f}')
