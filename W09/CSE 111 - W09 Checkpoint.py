# Import pandas module for use.

import pandas as pd

# Define main function.

def main():
    df = pd.read_csv('W09water.csv', dtype={"meterNumber": "str", "meterSize": "float32",
                "readDate": "str", "numberOfDays": "int_", "usage": "int_",
                "accountType": "str", "numberOfDwellings": "int_"
            },
            parse_dates=["readDate"])

    # Display DataFrame's .dtype attribute.
    print(df.dtypes)
    print()

    # Call the .describe() function and display summary from the function.
    print(df.describe())
    print()

    # Call the print function to print the DataFrame.
    print(df)
    print()

    # Filter the DataFrame to include only residences.
    res_filter = (df['accountType'] == 'Residence')
    filtered_results = df[res_filter]
    print(filtered_results)


main()
