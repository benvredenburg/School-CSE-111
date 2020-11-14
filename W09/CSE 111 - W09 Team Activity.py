# Import pandas module for use.

import pandas as pd

# Define main function.

def main():
    df = pd.read_csv('W09water.csv', dtype={"meterNumber": "str", "meterSize": "float32",
                "readDate": "str", "numberOfDays": "int_", "usage": "int_",
                "accountType": "str", "numberOfDwellings": "int_"
            },
            parse_dates=["readDate"])
    print()

    # Display uniquew account types to user.
    account_types = df['accountType'].unique()
    print('Unique account types:')
    print(len(account_types), account_types)
    # Create a line break between sections.
    print()

    # Display unique meter numbers to user.
    meters = df['meterNumber'].unique()
    print('Unique Meter numbers:')
    print(len(meters), meters)
    # Create a line break between sections.
    print()

    # Compute total amount of water used and display to user.
    total_usage = df['usage'].sum()
    print('Total water used:', total_usage)

    # Filter data and compute usage for residences. Display to user.
    res_filter = df['accountType'] == 'Residence'
    residences = df[res_filter]
    water_used = residences['usage'].sum()
    print('Total water used by residences', water_used)

    # Filter data and compute usage for apartment complexes. Display to user.
    apt_filter = df['accountType'] == 'Apartment Complex'
    apartments = df[apt_filter]
    water_used = apartments['usage'].sum()
    print('Total water used by apartment complexes:', water_used)
    # Create a line break between sections.
    print()

    # Filter DataFrame to remove duplicate entries.
    total_meter_types = df.drop_duplicates(subset=['meterNumber'])

    # Display total number of meters per each unique account type.
    print('Account Types:')
    print(total_meter_types['accountType'].value_counts())
    print()

main()