# Import math library

import math

# Receive inputs from the user for the width, aspect ratio, and diameter of the tire

width_input = input('Enter the width of the tire in cm (ex 205): ')
aspect_ratio_input = input('Enter the aspect ratio of the tire (ex 60): ')
diameter_input = input('Enter the diameter of the tire in inches (ex 15): ')

# Convert string text from user into positive numbers within variables

tire_w = abs(float(width_input))
tire_a = abs(float(aspect_ratio_input))
tire_d = abs(float(diameter_input))

# Calculate the volume of space inside the tire based on the use inputs

volume = round(math.pi * tire_w**2 * tire_a * (tire_w * tire_a + 2540 * tire_d) / 10000000, 1)

# Create message for user.

message = f"The volume of this tire is {volume} ML"

print (message)