# Import csv module for use.

import csv

# Create empty dictionary to be filled with student names and ID's.

students = {}

# Open sample csv and store a reference to the opened file in a variable named infile.

with open('students.csv', 'rt') as infile:

    # Use csv module to create a reader object that will read from the opened file.
    
    reader = csv.reader(infile, delimiter=',')

    # Skip the heading of the csv file.

    next(reader)

    # Read each row in the csv file one at a time as a list.

    for row in reader:

        # From the current row, add a student's I-number and name to the blank dictionary established above.

        students[row[0]] = row[1]

# Get an I-number from the user.

inum = str(input('Please enter an I-Number (xx-xxx-xxxx): '))

# Remove dashes from user input.

inum = inum.replace('-', '')

# Check to see if the user input is formatted correctly.

if inum.isdigit():
    if len(inum) < 9:
        print('Invalid I-Number: too few digits')
    elif len(inum) > 9:
        print('Invalid I-Number: too many digits')
    else:
        # If the user input is valid, find the I-Number in the list of I-numbers.
        if inum in students:
            # Retrieve the student name that corresponds to the I-number that the user entered.
            name = students[inum]

            # Print student name.
            print(name)
        else:
            print('No such student')
else:
    print('Invalid character in I-Number')
