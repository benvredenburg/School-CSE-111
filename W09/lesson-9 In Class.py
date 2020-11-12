import pandas as pd


def main():
    df = pd.read_csv('W09water.csv')

    df = pd.read_csv("W09water.csv", parse_dates=["readDate"])
    filter = (df["accountType"] == "Business") & (df["readDate"] >= "2018-01-01")
    filtered_df = df[filter]

    print(filtered_df)

    
    # print(df.dtypes)

    # column = df['accountType']
    # unique_acct_types = column.unique()
    # print(len(unique_acct_types))
    # print(unique_acct_types)
    # print()

    # column_meters = df['meterNumber']
    # unique_meter = column_meters.unique()
    # print(len(unique_meter))
    # print()

    # column_usage = df['usage']
    # total_usage = column_usage.sum()
    # print(total_usage)    

    # res_filter = df['accountType'] == 'Residence'
    # residences = df[res_filter]
    # res_water_usage = residences['usage'].sum()
    # print(res_water_usage)

    # apt_filter = df['accountType'] == 'Apartment Complex'
    # apartments = df[apt_filter]
    # apt_water_usage = apartments['usage'].sum()
    # print(apt_water_usage)

    # total_meter_types = df.drop_duplicates(subset=['meterNumber'])
    # print('Account Types:')
    # print(total_meter_types['accountType'].value_counts())
    # print()

    # start = pd.to_datetime('2015-01-01')
        # end = pd.to_datetime('2015-12-31')
        # filter_2015 = (df['readDate'] >= start) & (df['readDate'] <= end)
        # df2015 = df[filter_2015]

        # # Compute and display total usage from 2018.
        # water_used = df2015['usage'].sum()
        # # print('Water used during 2015:', water_used)

        # # Filter 2018 data to remove duplicate meter number entries.
        # total_meter_types = df2015.drop_duplicates(subset=['meterNumber'], keep='last')

        # # Compute and display the total number of dwellings in 2018.
        # num_dwellings = total_meter_types['numberOfDwellings'].sum()
        # # print('Number of dwellings in 2018:', num_dwellings)

        # # Filter 2018 data to show meters that serve dwellings.
        # dwelling_filter = df2015['numberOfDwellings'] > 0
        # dwelling_readings = df2015[dwelling_filter]

        # # Compute the total amount of water per dwelling in 2018.
        # total_usage_per_dwelling = dwelling_readings['usage'].sum()

        # # Compute and display average usage per dwelling in 2018.
        # avg_usage = round(total_usage_per_dwelling / num_dwellings, 5)
        # print('Average water used by each dwelling in 2015:', avg_usage)


        # start = pd.to_datetime('2016-01-01')
        # end = pd.to_datetime('2016-12-31')
        # filter_2016 = (df['readDate'] >= start) & (df['readDate'] <= end)
        # df2016 = df[filter_2016]

        # # Compute and display total usage from 2018.
        # water_used = df2016['usage'].sum()
        # # print('Water used during 2015:', water_used)

        # # Filter 2018 data to remove duplicate meter number entries.
        # total_meter_types = df2016.drop_duplicates(subset=['meterNumber'], keep='last')

        # # Compute and display the total number of dwellings in 2018.
        # num_dwellings = total_meter_types['numberOfDwellings'].sum()
        # # print('Number of dwellings in 2018:', num_dwellings)

        # # Filter 2018 data to show meters that serve dwellings.
        # dwelling_filter = df2016['numberOfDwellings'] > 0
        # dwelling_readings = df2016[dwelling_filter]

        # # Compute the total amount of water per dwelling in 2018.
        # total_usage_per_dwelling = dwelling_readings['usage'].sum()

        # # Compute and display average usage per dwelling in 2018.
        # avg_usage = round(total_usage_per_dwelling / num_dwellings, 5)
        # print('Average water used by each dwelling in 2016:', avg_usage)


        # start = pd.to_datetime('2017-01-01')
        # end = pd.to_datetime('2017-12-31')
        # filter_2017 = (df['readDate'] >= start) & (df['readDate'] <= end)
        # df2017 = df[filter_2017]

        # # Compute and display total usage from 2018.
        # water_used = df2017['usage'].sum()
        # # print('Water used during 2015:', water_used)

        # # Filter 2018 data to remove duplicate meter number entries.
        # total_meter_types = df2017.drop_duplicates(subset=['meterNumber'], keep='last')

        # # Compute and display the total number of dwellings in 2018.
        # num_dwellings = total_meter_types['numberOfDwellings'].sum()
        # # print('Number of dwellings in 2018:', num_dwellings)

        # # Filter 2018 data to show meters that serve dwellings.
        # dwelling_filter = df2017['numberOfDwellings'] > 0
        # dwelling_readings = df2017[dwelling_filter]

        # # Compute the total amount of water per dwelling in 2018.
        # total_usage_per_dwelling = dwelling_readings['usage'].sum()

        # # Compute and display average usage per dwelling in 2018.
        # avg_usage = round(total_usage_per_dwelling / num_dwellings, 5)
        # print('Average water used by each dwelling in 2018:', avg_usage)

        # start = pd.to_datetime('2018-01-01')
        # end = pd.to_datetime('2018-12-31')
        # filter_2018 = (df['readDate'] >= start) & (df['readDate'] <= end)
        # df2018 = df[filter_2018]

        # # Compute and display total usage from 2018.
        # water_used = df2018['usage'].sum()
        # # print('Water used during 2015:', water_used)

        # # Filter 2018 data to remove duplicate meter number entries.
        # total_meter_types = df2018.drop_duplicates(subset=['meterNumber'], keep='last')

        # # Compute and display the total number of dwellings in 2018.
        # num_dwellings = total_meter_types['numberOfDwellings'].sum()
        # # print('Number of dwellings in 2018:', num_dwellings)

        # # Filter 2018 data to show meters that serve dwellings.
        # dwelling_filter = df2018['numberOfDwellings'] > 0
        # dwelling_readings = df2018[dwelling_filter]

        # # Compute the total amount of water per dwelling in 2018.
        # total_usage_per_dwelling = dwelling_readings['usage'].sum()

        # # Compute and display average usage per dwelling in 2018.
        # avg_usage = round(total_usage_per_dwelling / num_dwellings, 5)
        # print('Average water used by each dwelling in 2018:', avg_usage)


        # start = pd.to_datetime('2019-01-01')
        # end = pd.to_datetime('2019-12-31')
        # filter_2019 = (df['readDate'] >= start) & (df['readDate'] <= end)
        # df2019 = df[filter_2019]

        # # Compute and display total usage from 2018.
        # water_used = df2019['usage'].sum()
        # # print('Water used during 2015:', water_used)

        # # Filter 2018 data to remove duplicate meter number entries.
        # total_meter_types = df2019.drop_duplicates(subset=['meterNumber'], keep='last')

        # # Compute and display the total number of dwellings in 2018.
        # num_dwellings = total_meter_types['numberOfDwellings'].sum()
        # # print('Number of dwellings in 2018:', num_dwellings)

        # # Filter 2018 data to show meters that serve dwellings.
        # dwelling_filter = df2019['numberOfDwellings'] > 0
        # dwelling_readings = df2019[dwelling_filter]

        # # Compute the total amount of water per dwelling in 2018.
        # total_usage_per_dwelling = dwelling_readings['usage'].sum()

        # # Compute and display average usage per dwelling in 2018.
        # avg_usage = round(total_usage_per_dwelling / num_dwellings, 5)
        # print('Average water used by each dwelling in 2019:', avg_usage)


    # filter = (df['meterNumber'] == input('enter a meter number: '))
        # df = df[filter]

        # df['year'] = df['readDate'].dt.year
        # # print(df)

        # total = df[['year', 'usage']].groupby('year').sum()
        # print(total)


main()