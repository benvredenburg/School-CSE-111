# Import necessary modules for use.

import csv
import math
from datetime import date, datetime


def main():

    # Print header for Gender, Age (years), Weight (kg), Height (cm), BMI, BMR.

    print('Gender, Age (years), Weight (kg), Height (cm), BMI, BMR')

# Open the fitness.csv file for reading.

    with open('fitness.csv', 'rt') as fitness:

        # Use the csv module to get a reader object.

        reader = csv.reader(fitness)

# Process each row in the csv file by doing the following:
    # 1. Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions as necessary
    # 2. Print the gender, age in years, weight in kilograms, height
    # in centimeters, body mass index, and basal metabolic rate.

        next(reader)

# Read each row in the csv file one at a time as a list.

        for row in reader:

            gender = row[0]
            age = row[1]
            weight = float(row[2])
            height = float(row[3])

            birthdate = compute_age(age)
            kilos = round(kg_from_lb(weight), 2)
            centimeter = round(cm_from_in(height), 1)
            bmi = round(body_mass_index(kilos, centimeter), 1)
            bmr = round(basal_metabolic_rate(gender, kilos, centimeter, birthdate), 1)

            print(f'{gender}, {birthdate}, {kilos}, {centimeter}, {bmi}, {bmr}')


def compute_age(birth):
    """Compute and return a person's age in years.

    param birth: a person's birthdate stored as
        a string in this format: YYYY-MM-DD
    """
    birthdate = datetime.strptime(birth, "%Y-%m-%d").date()
    now = date.today()
    diff = now - birthdate
    years = math.floor(diff.days / 365.25)
    return years


def kg_from_lb(lb):
    """Convert a mass in pounds to kilograms."""
    kg = lb * 0.45359237
    return kg


def cm_from_in(inch):
    """Convert a length in inches to centimeters."""
    cm = inch * 2.54
    return cm


def body_mass_index(weight, height):
    """Calculate and return a person's body mass
    index (bmi). weight and height must be in
    kilograms and centimeters, respectively.
    """
    bmi = 10000 * weight / height ** 2
    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Calculate and return a person's basal metabolic
    rate (bmr). weight must be in kilograms, height
    must be in centimeters, and age must be in years.
    """
    if gender == 'F':
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
    else:
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    return bmr


# Call the main function so that
# this program will start executing.

main()