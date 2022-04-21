# Import required module.

import random

# Define main function.

def main():

    # Create list of numbers.

    randnums = [16.2, 75.1, 52.3]

    # Print list 'randnums'.

    print(f'randnums {randnums}')

    # Call append_random_numbers function to add 3 numbers to list 'randnums'.

    append_random_numbers(randnums, 3)

    # Print list 'randnums'.

    print(f'randnums {randnums}')

# Define append_randum_numbers function.

def append_random_numbers(ls, n=1):

    # Append a number of random numbers 'n' into the list 'ls' between 0 - 100.

    for _ in range(n):
        num = random.uniform(0, 100)
        rounded = round(num, 1)
        ls.append(rounded)

# Call main function.

main()
