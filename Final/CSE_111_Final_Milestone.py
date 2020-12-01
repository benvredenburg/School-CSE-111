import pandas as pd
import matplotlib as pyplot

def main():
    try:
        # Create a line break between the terminal and the program.
        print()

        # Read the finalalarms.csv file and convert it to a dataframe.
        df = pd.read_csv('finalalarms.csv')


        # Add column for segment based on building number.
        # df = add_segment_column(df)

        # Add column for SLA based on alarm point, type, and time to clear(?).
        # df = add_sla_column(df)

        # Filter by segment(?).
        # seg_df = filter_by_segment(df)

        # Ask user for a building to show.
        building = int(input('which building would you like to show? '))

        # Filter by building(?).
        bldg_df = filter_by_building(df, building)

        # Filter by operator(?).
        # op_df = filter_by_operator(df)

        # Filter by date(?).
        # date_df = filter_by_date(df)

        # Filter by alarm type(?).
        # type_df = filter_by_type(df)

        # Filter by whether alarm went SLA(?)
        # sla_df = filter_by_sla(df)



        # show_alarms_by_date(date_df, )
        # show_alarms_by_operator(op_df, )
        # show_alarms_by_segment(seg_df, )
        # show_alarms_by_building(bldg_df, )
        # show_alarms_by_type(type_df, )
        # show_alarms_by_sla(sla_df, )
        
        print(bldg_df)
    except RuntimeError as ex:
        print(type(ex).__name__, ex, sep=": ")

def add_segment_column():
    # Add a column to the data frame that uses the building
    # number in the 'building' column. Buildings 1 - 100 should
    # be labeled as AMER, 101 - 200 should be labeled as EMEA,
    # and buildings 201 - 300 should be labeled as APAC.
    pass

def add_sla_column():
    # Add a column to the data frome the compares the alarm point
    # with the time to clear to determine if the cell gets a pass
    # or fail label. Server room has an SLA of 5:00, everything else
    # has an SLA of 10:00.
    pass

def filter_by_segment(df, segment):
    # Filter the data frame to only show alarms from a specific
    # segment.
    pass

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
    pass

def filter_by_date(df, start, end):
    # Filter the data frame to only show alarms from a specific
    # date range.
    pass

def filter_by_type(df, alarmType):
    # Filter the data frame to only show alarms from a specific
    # alarm type.
    pass

def filter_by_sla(df, sla):
    # Filter the data frame to only show alarms from a specific
    # that failed or passed SLA.
    pass

main()