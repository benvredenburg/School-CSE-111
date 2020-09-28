# Import Modules.

import random
import textwrap

# Open text file.

with open('quotes.txt', 'rt') as infile:

    # Read quotes within file.

    quotes = infile.readlines()

    # Request number of quotes from user.

num = int(input('How many quotes would you like? '))

    # Display requested quotes to user.

for _ in range(num):
        
        # Choose a quote at random.

    quote = random.choice(quotes)

        # Wrap quotes displayed to user.

    wrapped = textwrap.wrap(quote, 60)

        # Line break.

    print()

        # Display quote(s) to user.
        
    for line in wrapped:
        print(line)