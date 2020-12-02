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
        # df['building'] = df.astype({'building': int})
        df['building'] = df['building'].astype(int)

        # Filter by date(?). 
        '''Always necessary'''
        # date_df = filter_by_date(df)
        
        # Ask user for a building to show.
        building = int(input('which building would you like to show? '))

        # Filter by building(?).
        bldg_df = filter_by_building(df, building)
        
        # Ask user for an operator to show.
        operator = input('Which operator would you like to see? ').capitalize()

        # Filter by operator.
        op_df = filter_by_operator(df, operator)

        

        # Filter by alarm type(?).
        # type_df = filter_by_type(df)

        # Filter by whether alarm went SLA(?)
        # sla_df = filter_by_sla(df)



        # show_alarms_by_date(date_df, )
        show_alarms_by_operator(op_df, operator)
        # show_alarms_by_segment(seg_df, )
        show_alarms_by_building(bldg_df, building)
        # show_alarms_by_type(type_df, )
        # show_alarms_by_sla(sla_df, )


        plt.show()
        # print(df)
        print(bldg_df)
        print(op_df)
        # print(df.dtypes)


        
    except RuntimeError as ex:
        print(type(ex).__name__, ex, sep=": ")








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

def filter_by_date(df, start, end):
    # Filter the data frame to only show alarms from a specific
    # date range.
    pass

def filter_by_type(df, alarmType):
    # Filter the data frame to only show alarms from a specific
    # alarm type.
    pass



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