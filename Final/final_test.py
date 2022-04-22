import pandas as pd
import pytest
from CSE_111_Final_Milestone_Master import filter_between_dates, filter_by_building, filter_by_operator, filter_by_type, group_by, show_alarms_by_date

def test_between_dates():
    
    df = pd.read_csv('Final/finalalarms.csv', parse_dates=['date'])
    start1 = pd.to_datetime('2018-01-01')
    end1 = pd.to_datetime('2018-01-07')
    start2 = pd.to_datetime('2018-01-08')
    end2 = pd.to_datetime('2018-01-14')
    start3 = pd.to_datetime('2018-12-25')
    end3 = pd.to_datetime('2018-12-31')
    df1 = pd.DataFrame(filter_between_dates(df, start1, end1))
    df2 = pd.DataFrame(filter_between_dates(df, start2, end2))
    df3 = pd.DataFrame(filter_between_dates(df, start3, end3))
    for row in df1.iterrows():
        cells = row[1]
        assert cells['date'] >= start1 and cells['date'] <= end1
        
    for row in df2.iterrows():
        cells = row[1]
        assert cells['date'] >= start2 and cells['date'] <= end2
    
    for row in df3.iterrows():
        cells = row[1]
        assert cells['date'] >= start3 and cells['date'] <= end3

def test_filter_by_building():

    df = pd.read_csv('Final/finalalarms.csv', parse_dates=['date'])
    building1 = 52
    building2 = 261
    building3 = 157
    df1 = pd.DataFrame(filter_by_building(df, building1))
    df2 = pd.DataFrame(filter_by_building(df, building2))
    df3 = pd.DataFrame(filter_by_building(df, building3))
    for row in df1.iterrows():
        cells = row[1]
        assert cells['building'] == building1

    for row in df2.iterrows():
        cells = row[1]
        assert cells['building'] == building2

    for row in df3.iterrows():
        cells = row[1]
        assert cells['building'] == building3
    
def test_filter_by_operator():

    df = pd.read_csv('Final/finalalarms.csv', parse_dates=['date'])
    operator1 = 'Benjamin'
    operator2 = 'Austin'
    operator3 = 'Joseph'
    df1 = pd.DataFrame(filter_by_operator(df, operator1))
    df2 = pd.DataFrame(filter_by_operator(df, operator2))
    df3 = pd.DataFrame(filter_by_operator(df, operator3))
    for row in df1.iterrows():
        cells = row[1]
        assert cells['operator'] == operator1

    for row in df2.iterrows():
        cells = row[1]
        assert cells['operator'] == operator2

    for row in df3.iterrows():
        cells = row[1]
        assert cells['operator'] == operator3

def test_filter_by_type():

    df = pd.read_csv('Final/finalalarms.csv', parse_dates=['date'])
    alarmType1 = 'FIRE'
    alarmType2 = 'DOOR FORCED'
    alarmType3 = 'SERVER'
    df1 = pd.DataFrame(filter_by_type(df, alarmType1))
    df2 = pd.DataFrame(filter_by_type(df, alarmType2))
    df3 = pd.DataFrame(filter_by_type(df, alarmType3))
    for row in df1.iterrows():
        cells = row[1]
        assert cells['alarmType'] == alarmType1
    
    for row in df2.iterrows():
        cells = row[1]
        assert cells['alarmType'] == alarmType2

    for row in df3.iterrows():
        cells = row[1]
        assert cells['alarmType'] == alarmType3

def test_group_by():

    df = pd.read_csv('Final/finalalarms.csv', parse_dates=['date'])
    start1 = pd.to_datetime('2018-01-01')
    end1 = pd.to_datetime('2018-01-01')
    df1 = pd.DataFrame(filter_between_dates(df, start1, end1))
    start2 = pd.to_datetime('2018-06-01')
    end2 = pd.to_datetime('2018-06-01')
    df2 = pd.DataFrame(filter_between_dates(df, start2, end2))
    start3 = pd.to_datetime('2018-12-31')
    end3 = pd.to_datetime('2018-12-31')
    df3 = pd.DataFrame(filter_between_dates(df, start3, end3))
    grouped_df1 = pd.DataFrame(group_by(df1))
    grouped_df2 = pd.DataFrame(group_by(df2))
    grouped_df3 = pd.DataFrame(group_by(df3))
    for row in grouped_df1.iterrows():
        cells = row[1]
        assert cells['alarms'] == 65
        
    for row in grouped_df2.iterrows():
        cells = row[1]
        assert cells['alarms'] == 26

    for row in grouped_df3.iterrows():
        cells = row[1]
        assert cells['alarms'] == 65

pytest.main(["Final/final_test.py"])

# Test 04/22/22