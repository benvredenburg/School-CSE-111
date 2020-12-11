import pandas as pd
import matplotlib.pyplot as plt



def main():
    try:

        # Create a line break between the terminal and the program.
        print()

        # Read the finalalarms.csv file and convert it to a dataframe.
        df = pd.read_csv('Final/finalalarms.csv')

        # Convert date column to datetime64 and building column into int.
        df['date'] = pd.to_datetime(df['date']).dt.date
        df['building'] = df['building'].astype(int)

         
        # Ask user for a date range.
        print('Please do not choose a date range over one week.')
        print()
        start = pd.to_datetime(input('enter start date in YYYY-MM-DD format: '))
        end = pd.to_datetime(input('enter end date in YYYY-MM-DD format: '))
        print()

        # Filter by provided date range. 
        df = filter_between_dates(df, start, end)

        # Create loop for adding any additional filters.
        choice1 = None
        while True:
            choice1 = input('Would you like to add a filter? Please enter (N) for no, (Y) for yes, or (Q) to quit: ').capitalize()
            print()

            if choice1 == 'Y':
                print("Filter options are:  OPERATOR,  BUILDING number, and  alarm TYPE. ")
                filter_choice = input('Which filter would you like to apply? ').capitalize()
                print()
                if filter_choice == 'Building':

                    # Ask user for a building to show.
                    building = int(input('which building (1 - 300) would you like to show? '))

                    # Filter by building.
                    df = filter_by_building(df, building)

                elif filter_choice == 'Operator':
            
                    # Ask user for an operator to show.
                    operator = input('Which operator would you like to see?\nAustin\nBenjamin\nJoseph\nMark\n').capitalize()

                    # Filter by operator.
                    df = filter_by_operator(df, operator)

                elif filter_choice == 'Type':

                    # Ask user for an alarm type.
                    alarmType = input('Which alarm type would you like to see?\n\nDoor Forced\nFire\nServer\n').upper()

                    # Filter by alarm type.
                    df = filter_by_type(df, alarmType)
            
            # Create a grouping a the number of alarms for each day of the date range
            # for the building, operator, and/or alarm type the user filtered by.
            elif choice1 == 'N':
                grouped_df = group_by(df)
                break
            
            # End program if user chooses to quit.
            elif choice1 == 'Q':
                print('Have a nice day!')
                break
            
            # Inform the user that they chose an incorrect choice at beginning of loop.
            else:
                print('Invalid choice.')
        
        # Display the dataframe, number of alarms for applied filters by day, and a graph
        # of the information in the latter.
        print(df)
        print(grouped_df)
        show_alarms_by_date(grouped_df)
        plt.show()
        
    except RuntimeError as ex:
        print(type(ex).__name__, ex, sep=": ")


def filter_between_dates(df, start, end):
    """Return a new DataFrame that contains only the rows where
    the readDate is between the specified start and end dates.
    """
    
    date_range_filter = (df['date'] >= start) & (df['date'] <= end)
    date_filter = df[date_range_filter]
    df = date_filter
    return df 

def filter_by_building(df, building):
    
    bldgNum = building
    bldg_filter = (df['building'] == bldgNum)
    bldg_filtered = df[bldg_filter]
    df = bldg_filtered
    return df

def filter_by_operator(df, operator):

    name = operator
    op_filter = (df['operator'] == name)
    op_filtered = df[op_filter]
    df = op_filtered
    return df

def filter_by_type(df, alarmType):

    alarmType = alarmType
    type_filter = (df['alarmType'] == alarmType)
    type_filtered = df[type_filter]
    df = type_filtered
    return df

def group_by(df):
    group = df.groupby("date")
    df = group.aggregate(alarms=("date", "count"))
    return df

def show_alarms_by_date(grouped_df):

    counts = list(grouped_df['alarms'])
    barplot = grouped_df.plot.bar(y="alarms", legend=False)
    barplot.set_title(f'Number of alarms by date:\n{counts}')
    plt.tight_layout()

if __name__ == "__main__":
    main()