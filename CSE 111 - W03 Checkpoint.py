# Create list

heights = [
    1.72, 1.50, 1.96, 2.01, 1.75,
    2.11, 1.60, 1.65, 2.05, 1.50,
    1.80, 1.83, 2.05, 1.79, 1.84
]

# Call functions and pass list of heights into each function.

l = len(heights)
mn = min(heights)
mx = max(heights)
s = sum(heights)

# Round the value returned from the sum function to two decimal places and store in s.

s = round(s, 2)

# Display results.

print(f'len: {l}')
print(f'min: {mn}')
print(f'len: {mx}')
print(f'len: {s}')