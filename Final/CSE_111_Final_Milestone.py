import pandas as pd
import matplotlib.pyplot as plt

def main():
    try:

        # Create a line break between the terminal and the program.
        print()

        # Read the finalalarms.csv file and convert it to a dataframe.
        df = pd.read_csv('finalalarms.csv')

        # Convert date column to datetime64.
        df['date'] = pd.to_datetime(df['date'])
        df['building'] = df['building'].astype(int)

        # Filter by date range. 
        '''Always necessary'''
        '''limit of one week for user'''

        # Ask user for a date range.

        print('Please do not choose a date range over one week.')
        start = pd.to_datetime(input('enter start date: '))
        end = pd.to_datetime(input('enter end date: '))

        # Convert the start and end years
        # from integers to date strings.
        start = pd.to_datetime(start)
        end = pd.to_datetime(end)   

        df = filter_between_dates(df, start, end)

        
        choice1 = None

        while True:
            choice1 = input('Would you like to add a filter? Please enter (N) for no, (Y) for yes, or (Q) to quit: ').capitalize()

            if choice1 == 'Y':
                print("Filter options are:  OPERATOR,  BUILDING number, and  alarm TYPE. ")
                filter_choice = input('Which filter would you like to apply? ').capitalize()
                if filter_choice == 'Building':

                    # Ask user for a building to show.
                    building = int(input('which building would you like to show? '))

                    # Filter by building(?).
                    df = filter_by_building(df, building)

                elif filter_choice == 'Operator':
            
                    # Ask user for an operator to show.
                    operator = input('Which operator would you like to see? ').capitalize()

                    # Filter by operator.
                    df = filter_by_operator(df, operator)

                elif filter_choice == 'Type':
                    # Filter by alarm type(?).
                    # df = filter_by_type(df)
                    alarmType = input('Which alarm type would you like to see? ').upper()

                    df = filter_by_type(df, alarmType)

                    # pass
                    
            elif choice1 == 'N':
                print(df)
                break

            elif choice1 == 'Q':
                print('Have a nice day!')
                break
            
            else:
                print('Invalid choice.')
            
        


        # plt.show()
        # print(df.dtypes)
        
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
    # Filter the data frame to only show alarms from a specific
    # building.
    bldgNum = building
    bldg_filter = (df['building'] == bldgNum)
    bldg_filtered = df[bldg_filter]
    df = bldg_filtered
    return df
    # pass

def filter_by_operator(df, operator):
    # Filter the data frame to only show alarms from a specific
    # operator.
    name = operator
    op_filter = (df['operator'] == name)
    op_filtered = df[op_filter]
    df = op_filtered
    return df
    # pass

def filter_by_type(df, alarmType):
    # Filter the data frame to only show alarms from a specific
    # alarm type.

    alarmType = alarmType
    type_filter = (df['alarmType'] == alarmType)
    type_filtered = df[type_filter]
    df = type_filtered
    return df

    # pass

# Start here.

def show_alarms_by_building(bldg_df, building):
    
    # barplot = bldg_df.plot.bar(x='date', legend=False)
    # barplot.set_title(f'Number of alarms for building #{building}')
    # barplot.set_xlabel('')
    
    # plt.tight_layout()

    plot = bldg_df.plot.line(x='date')
    plot.set_title(f"Number of alarms for building #{building}")
    plot.set_xlabel("")
    plt.tight_layout()

    # pass
def show_alarms_by_operator(op_df, operator):
    plot = op_df.plot.line(x='date')
    plot.set_title(f"Number of alarms for operator: {operator}")
    plot.set_xlabel("")
    plt.tight_layout()
    # pass
def show_alarms_by_type():
    pass
def show_alarms_by_date():
    pass

main()