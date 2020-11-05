from chemistry import parse_formula, molar_mass, FormulaError

# Define main function:
def main():
    
    try:
        while True:
            # Get molecule from user.
            user_molecule = input('Please input a molecule: ')
            break
    # Call parse_formula to convert user input into dictionary.
        elem_dict = parse_formula(user_molecule)

        # Call molar_mass to compute the molar mass of the user input.
        molar_mass(elem_dict)

        mass = round(molar_mass(elem_dict), 5)

        # print(elem_dict)
        print(f'{mass} grams/mole')

        mass_grams = float(input('Mass in grams of the substance: '))
        
        while True:
            moles = mass_grams / mass
            break

        print(f'{round(moles, 5)} moles')
    
    except FormulaError as ex:
        print()
        print(ex)
        print()
        print('There is an error in your formula. Please check that you have entered the formula in correctly and try again.')
        print()
    except ValueError as ex:
        print()
        print(ex)
        print()
        print('There is an invalid character in your number. Please check that you have entered the number in correctly and try again.')
        print()


main()

