import csv

# Create an empty dictionry to store product information with the product number as the key.

product = {}

# Open a file named products.csv and store a reference to the opened file in a variable named infile.

with open('W02products.csv', 'rt') as infile:

# Use the csv module to create a reader object that will read from the opened file.

    reader = csv.reader(infile, delimiter=',')

# Skip heading of table.

    next(reader)

# Read each row of the table in succession.

    for row in reader:

# From the current row, add a products' number, name, description, category, and price to the dictionary.

        product[row[0]] = row[1] + ', ' + '$' + row[4]

# Receive a product number from the user.

pnum = str(input('Please enter a product number: '))

# Determine if number is formatted correctly.

if pnum.isalnum():
    while len(pnum) != 5: 
        if any(c.isalpha() for c in pnum):
            print('Invalid character in Product Number')
            pnum = str(input('Please enter a product number: '))
        elif len(pnum) < 5:
            print('Invalid Product Number: too few digits')
            pnum = str(input('Please enter a product number: '))
        elif len(pnum) > 5:
            print('Invalid Product Number: too many digits')
            pnum = str(input('Please enter a product number: '))
    else:
# The user input is a valid product number. Find the product Number in the list of product Numbers.
        if pnum in product:
# Retrieve the product information that corresponds to the product Number that the user entered.
            info = product[pnum]

# Print the product information.
            print(info)
            
        else:
            print('No such Product')
