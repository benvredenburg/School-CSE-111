def main():
    # Create a line break between terminal and program.
    print()

    # Create and print a list named fruit.
    fruit = ['pear', 'banana', 'apple', 'mango']
    print(f'Original: {fruit}')

    # Create a line break between objectives.
    print()

    # Reverse and print the fruit list.
    fruit.reverse()
    print(f'Reversed: {fruit}')

    # Create a line break between objectives.
    print()

    # Add orange to the end of the list.
    fruit.append('orange')
    print(f'Append orange: {fruit}')

    # Create a line break between objectives.
    print()

    # Locate Apple and insert cherry before it.
    position = fruit.index('apple')
    fruit.insert(position, 'cherry')
    print(f'Insert cherry: {fruit}') 

    # Create a line break between objectives.
    print()

    # Remove banana.
    fruit.remove('banana')
    print(f'Remove banana: {fruit}')

    # Create a line break between objectives.
    print()

    # pop the last fruit from the list.
    last = fruit.pop()
    print(f'Pop: {last} {fruit}')

    # Create a line break between objectives.
    print()

    # Sort the fruit list.
    fruit.sort()
    print(f'Sorted: {fruit}')

    # Create a line break between objectives.
    print()

    # Clear the fruit list.
    fruit.clear()
    print(f'Cleared: {fruit}')

    # Create a line break between program and terminal
    print()
    
main()