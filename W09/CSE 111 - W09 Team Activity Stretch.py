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
    print('Uniquew account types:')
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

    # Filter data to remove duplicate meter number entries.
    total_meter_types = df.drop_duplicates(subset=['meterNumber'])

    # Display total number of meters per each unique account type.
    print('Account Types:')
    print(total_meter_types['accountType'].value_counts())
    print()

    # Filter data to show only readings from 2018.
    start = pd.to_datetime('2018-01-01')
    end = pd.to_datetime('2018-12-31')
    filter_2018 = (df['readDate'] >= start) & (df['readDate'] <= end)
    df2018 = df[filter_2018]

    # Compute and display total usage from 2018.
    water_used = df2018['usage'].sum()
    print('Water used during 2018:', water_used)

    # Filter 2018 data to remove duplicate meter number entries.
    total_meter_types = df2018.drop_duplicates(subset=['meterNumber'], keep='last')

    # Compute and display the total number of dwellings in 2018.
    num_dwellings = total_meter_types['numberOfDwellings'].sum()
    print('Number of dwellings in 2018:', num_dwellings)

    # Filter 2018 data to show meters that serve dwellings.
    dwelling_filter = df2018['numberOfDwellings'] > 0
    dwelling_readings = df2018[dwelling_filter]

    # Compute the total amount of water per dwelling in 2018.
    total_usage_per_dwelling = dwelling_readings['usage'].sum()

    # Compute and display average usage per dwelling in 2018.
    avg_usage = round(total_usage_per_dwelling / num_dwellings, 2)
    print('Average water used by each dwelling in 2018:', avg_usage)

main()