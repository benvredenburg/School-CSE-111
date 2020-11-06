# Enable datetime

import datetime

# Determine day of week.

weekday = datetime.datetime.now().isoweekday()

# Receive subtotal

subtotal = float(input('Subtotal: $'))

# Define Tax and Discount rates.

tax_rate = 0.06
discount = 0.1

# Determine if customer receives the discount.

if subtotal > 50 and (weekday == 2 or weekday ==3):
    discount = round(subtotal * discount, 2)
    subtotal -= discount

# Determine the total.

tax = round(subtotal * tax_rate, 2)
total = round(subtotal + tax, 2)

# Display total to user.

print(f'Total: ${total}')