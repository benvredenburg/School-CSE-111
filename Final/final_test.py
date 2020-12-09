import pandas as pd
import pytest
from CSE_111_Final_Milestone_Master import filter_between_dates, filter_by_building, filter_by_operator, filter_by_type, group_by, show_alarms_by_date

def test_between_dates():
    
    df = pd.read_csv('finalalarms.csv', parse_dates=['date'])
    
    # assert df['date'] == date
    start = pd.to_datetime('2018-01-01')
    end = pd.to_datetime('2018-01-07')
    df = pd.DataFrame(filter_between_dates(df, start, end))
    for row in df.iterrows():
        assert row['date'] >= start and row['date'] < end

def test_filter_by_building():

    df = pd.read_csv('finalalarms.csv', parse_dates=['date'])

    building = '52'
    df = pd.DataFrame(filter_by_building(df, building))

    for row in df.iterrows():
        assert row['building'] == '52'

def test_filter_by_operator():
    df = pd.read_csv('finalalarms.csv', parse_dates=['date'])
    operator = 'benjamin'
    df = pd.DataFrame(filter_by_building(df, operator))

    for row in df.iterrows():
        assert row['operator'] == 'benjamin'

#     df = pd.read_csv('finalalarms.csv')
#     operator = 'benjamin'
#     for row in df.iterrows():
#         assert operator == 'benjamin'

def test_filter_by_type():
    df = pd.read_csv('finalalarms.csv', parse_dates=['date'])
    alarmType = 'fire'
    df = pd.DataFrame(filter_by_building(df, alarmType))

    for row in df.iterrows():
        assert row['alarmType'] == 'fire'

#     df = pd.read_csv('finalalarms.csv')
#     alarmType = 'fire'
#     for row in df.iterrows():
#         assert alarmType == alarmType

def test_group_by():
    df = pd.read_csv('finalalarms.csv', parse_dates=['date'])
    start = pd.datetime('2018-01-01')
    end = pd.datetime('2018-01-07')
    df = pd.DataFrame(filter_between_dates(df, start, end))

    grouped_df = pd.DataFrame(group_by(df))

    for row in df.iterrows():
        assert row['count'] == '349'

pytest.main(["Final/final_test.py"])

