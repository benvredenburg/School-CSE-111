def main():
    try:
            
        # Get the odometer readings from the user.
        start = float(input('Enter the beginning odometer reading: '))
        end = float(input('Enter the ending odometer reading: '))


        # Get the gallons of gasoline used from the user.
        gallons = float(input('Enter the number of gallons: '))

        # Compute the miles per gallon.
        mpg = (end - start) / gallons

        # Display the results for the user.
        print(mpg)
    
    except ValueError as ex:
        print('Invalid number. Please enter a number.')

main()