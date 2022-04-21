import matplotlib.pyplot as plt
import pandas as pd


def main():
    try:
        # Create a line break between the terminal and the program.
        print()
        # Read the water.csv file and convert the
        # readDate column from a string to a datetime64.
        df = pd.read_csv('CSE-111\W09water.csv1000', parse_dates=['readDate'])

        # Add a yearMonth column to the DataFrame.
        df = add_year_month_column(df)
        
        # Add a medianUsage column to the DataFrame.
        df = add_median_usage_column(df)


        # Repeat as necessary.   
        while True:

            # Get a meter number from the user.
            meter = input('Please enter a meter number ("q" to quit): ')
            print()
            if meter == "q":
                break

            ''' 
            If the user ever wants to pull dates by "YYYY/MM/DD" format, they can replace this section with the following
            lines of code:

            start = pd.to_datetime(input('enter start date: '))
            end = pd.to_datetime(input('enter end date: '))

            Beginning of aforementioned section.
            '''   

            # Get start and end years from the user.
            start_year = get_int('Please enter a starting year between 2015 and 2019, inclusive: ', 2015, 2019)
            end_year = get_int(f'Please enter a starting year between {start_year} and 2019, inclusive: ', start_year, 2019)
            print()

            # Convert the start and end years
            # from integers to date strings.
            start = pd.to_datetime(f'{start_year}-01-01')
            end = pd.to_datetime(f'{end_year}-12-31')   

            
            # End of section from above lines of comments.
            
            
            # Filter the DataFrame to the meter number
            # and years specifified by the user. 
            filtered_df = filter_between_dates(df, start, end)    
            filtered_df = filter_for_meter(filtered_df, meter)  
              
            print()
            print(filtered_df)
            print(df.dtypes)

            # Define two plots.
            show_meter_usage(filtered_df, meter)

            # Show all defined plots.
            show_comparison(filtered_df, meter)

            plt.show()
            print()



        
       
    except RuntimeError as ex:
        print(type(ex).__name__, ex, sep=": ")


def get_int(prompt, lower, upper):
    """Get an integer from the user, validate that the integer is
    between a lower and upper bound, and return the integer to the
    calling function. If the user does not enter an integer between
    lower and upper, inclusive, this function will prompt the user
    repeatedly until the user enters an integer between lower and upper.

    param prompt: A string to display to the user.
    param lower: The lowest (smallest) integer that the user may enter.
    param upper: The highest (largest) integer that the user may enter.
    """
    while True:
        try:
            integer = int(input(prompt))
            if integer < lower:
                print(f'{integer} is too low. Please enter another integer.')
            elif integer > upper:
                print(f'{integer} is too high. Please enter another integer.')
            else:
                break
        except ValueError as _:
            # print(ex)
            # print()
            print('Invalid character in integer')
    return integer


def insert_after(alist, existing, toinsert):
    """Insert an element into a list after an existing element.

    param alist: a Python list.
    param existing: an element that exists in alist.
    param toinsert: the element that this function will insert into
        alist after the existing element.
    """
    location = alist.index(existing)
    alist.insert(location + 1, toinsert)
    return alist


def add_median_usage_column(df):
    """Add to the DataFrame a column named medianUsage that
    contains the median usage grouped by accountType and yearMonth.
    Return the new DataFrame.
    """
    # unneccesary for current assignment as add_year_month() is already in main.
    # df = add_year_month_column(df)
    columns = df.columns.tolist()

    # Find the median usage grouped by accountType and yearMonth.
    median_df = df.groupby(["accountType", "yearMonth"]) \
            .aggregate(medianUsage=("usage", "median"))

    # Change the index so that joining the median_df
    # with the original data frame will work.
    df.set_index(["accountType", "yearMonth"], inplace=True)

    # Join the original data frame and the median data frame.
    joined_df = df.join(median_df)

    # The join sorts the data frame by the join key, which is
    # a different order than the CSV file, so sort the rows by
    # meterNumber and readDate like the CSV file, and then reset
    # the index as if the data were just read from the CSV file.
    joined_df.sort_values(["meterNumber", "readDate"], inplace=True)
    joined_df.reset_index(drop=False, inplace=True)

    # Reorder the columns to be similar to the CSV file.
    insert_after(columns, "usage", "medianUsage")
    joined_df = joined_df[columns]

    return joined_df


def add_year_month_column(df):
    """Add to the DataFrame a column named yearMonth that contains only
    the year and the month of the readDate and return the new DataFrame.
    """

    df['yearMonth'] = pd.to_datetime(df['readDate']).dt.to_period('M')
    return df


def filter_for_meter(df, meter):
    """Return a new DataFrame that contains only the rows
    where the meterNumber equals the parameter meter.
    """
    meterNum = 'M' + meter
    meter_filter = (df['meterNumber'] == meterNum)
    meter_filtered = df[meter_filter]
    df = meter_filtered
    return df


def filter_between_dates(df, start, end):
    """Return a new DataFrame that contains only the rows where
    the readDate is between the specified start and end dates.
    """
    
    date_range_filter = (df['readDate'] >= start) & (df['readDate'] <= end)
    date_filter = df[date_range_filter]
    df = date_filter
    return df 


def show_meter_usage(df, meter):
    """Define a vertical column plot that shows the year
    and month on the x-axis and the usage on the y-axis.

    param df: a DataFrame with at least these two
        columns: yearMonth, usage, that is already
        filtered to the rows for one meter number only.
    param meter: the meter number for which df is filtered.
    """
    
    barplot = df.plot.bar(x='yearMonth', y='usage', legend=False)
    barplot.set_title(f"Water Usage for Meter #{meter}")
    barplot.set_xlabel("")
    barplot.set_ylabel("x1000 gallons")
    plt.tight_layout()


def show_comparison(df, meter):
    """Define a line plot that shows the year and month on
    the x-axis and the usage and median usage on the y-axis.

    param df: a DataFrame with at least these three columns:
        yearMonth, usage, medianUsage, that is already
        filtered to the rows for one meter number only.
    param meter: the meter number for which df is filtered.
    """
    plot = df.plot.line(x='yearMonth', y=['usage', 'medianUsage'])
    plot.set_title(f"Water Usage and Median Water usage for Meter #{meter}")
    plot.set_xlabel("")
    plot.set_ylabel("x1000 gallons")
    plt.tight_layout()
    plot.legend(['usage', 'median'])

# Call the main function so that
# this program will start executing.
if __name__ == "__main__":
    main()