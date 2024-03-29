import csv


YEAR_KEY = "Year"
FATALITIES_KEY = "Fatalities"
INJURIES_KEY = "Injuries"
CRASHES_KEY = "Crashes"
FATAL_CRASHES_KEY = "Fatal Crashes"
DISTRACT_KEY = "Distraction Affected Fatal Crashes"
PHONE_KEY = "Fatal Crashes involving Cell Phone Use"
SPEED_KEY = "Fatal Crashes involving Excessive Speed"
DUI_KEY = "Fatal Crashes while Driving under the Influence"
FATIGUE_KEY = "Fatal Crashes involving Fatigue or Illness"


def main():
    # Create break between terminal and starting line for visibility.
    print()
    try:
        # Prompt the user for a filename and open that text file.
        filename = input("Name of file that contains NHTSA data: ")
        print()

        # Prompt the user for a percentage. Loop on invalid values.
        try:
            while True:
                perc_reduc = float(input("Percent reduction of texting while driving [0 - 100]: "))
                if perc_reduc < 0:
                    print(f'Error: {perc_reduc} is too low. Please enter a number between 0 and 100.')
                elif perc_reduc > 100:
                    print(f'Error: {perc_reduc} is too high. Please enter a number between 0 and 100.')
                else:
                    break
            print()
        # Display exception and start over from beginning.
        except ValueError as err:
            print(err)
            print('You have entered an invalid character into your number. Please review your number and try again.')
            print()
            main()


        # Open the text file that the user requested.
        with open(filename, "rt") as infile:
            print(f"With a {perc_reduc}% reduction in using a cell phone while",
                    "driving, approximately this number of injuries and",
                    "deaths would have been prevented in the USA.", sep="\n")
            print()
            print("Year, Injuries, Deaths")

            # Create a DictReader object to read each line from the CSV
            # file. This code doesn't include the next(reader) command to
            # skip the first line of the file because the DictReader object
            # uses the column headers on the first line of the file.
            reader = csv.DictReader(infile)

            # Process each row in the CSV file.
            for row in reader:
                year = row[YEAR_KEY]

                # Call the estimate_reduction function.
                injur, fatal = estimate_reduction(row, PHONE_KEY, perc_reduc)

                # Print the estimated reductions in injuries and fatalities.
                print(year, injur, fatal, sep=", ")
    # Display exception and return to beginning.
    except FileNotFoundError as err:
        print(f'The file {filename} was not found. Please check your file name and try again.')
        print('Please choose a different file.')
        print()
        main()
    # Display exception and return to beginning.
    except PermissionError as err:
        print(err)
        print(f'I am sorry, you do not have the correct permissions to view {filename}. Please check your file name and try again.')
        print()
        main()
    


def estimate_reduction(row, behavior_key, perc_reduc):
    """Estimate and return the number of injuries and deaths that would
    not have occurred on U.S. roads and highways if drivers had reduced
    a dangerous behavior by a given percentage.

    Params:
        row: a CSV row of data from the U.S. National Highway Traffic
            Safety Administration (NHTSA)
        behavior_key: heading from the CSV file for the dangerous
            behavior that drivers could reduce
        perc_reduc: percent that drivers could reduce a dangerous
            behavior
    """
    behavior = int(row[behavior_key])
    fatal_crashes = int(row[FATAL_CRASHES_KEY])
    ratio = perc_reduc / 100 * behavior / fatal_crashes

    fatalities = int(row[FATALITIES_KEY])
    injuries = int(row[INJURIES_KEY])

    reduc_fatal = int(round(fatalities * ratio, 0))
    reduc_injur = int(round(injuries * ratio, 0))
    return reduc_injur, reduc_fatal


# Call the main function so that
# this program will start executing.
main()
