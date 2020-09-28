# Problem: Write a Python program that asks for a person's age and computes and outputs the slowest and fastest rates necessary to strengthen their heart.

# Receive age input from user.

age_input = abs(round(float(input('What is your age? '))))

# Calculate the maximum heart rate for the user based off their age input

max_rate = 220 - age_input

# Calulate the range the user should keep their heart rate at during exercise in order to strengthen their heart.

slowest_speed = round((max_rate * 0.65))
fastest_speed = round((max_rate * 0.85))

# Create output message for user

output = \
    f'When you exercise to strengthen your heart, you should keep\n' \
    f'your heart rate between {slowest_speed} and {fastest_speed} BPM'

# Display output message to user

print(output)