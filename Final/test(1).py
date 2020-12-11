import pandas as pd
import pytest
from CSE_111_Final_Milestone_Master import filter_between_dates, filter_by_building, filter_by_operator, filter_by_type, group_by, show_alarms_by_date

def test_between_dates():
    
    df = pd.read_csv('Final/finalalarms.csv')
    start1 = '2018-01-01'
    end1 = '2018-01-07'
    df = pd.DataFrame(filter_between_dates(df, start1, end1))
    for row in df.iterrows():
        assert row['date'] >= start1 and row['date'] <= end1

def test_filter_by_building():

    df = pd.read_csv('Final/finalalarms.csv')
    building = '52'
    df = pd.DataFrame(filter_by_building(df, building))
    for row in df.iterrows():
        assert row['building'] == '52'

def test_filter_by_operator():
    df = pd.read_csv('Final/finalalarms.csv')
    operator = 'benjamin'
    df = pd.DataFrame(filter_by_building(df, operator))
    for row in df.iterrows():
        assert row['operator'] == 'benjamin'

def test_filter_by_type():
    df = pd.read_csv('Final/finalalarms.csv')
    alarmType = 'fire'
    df = pd.DataFrame(filter_by_building(df, alarmType))
    for row in df.iterrows():
        assert row['alarmType'] == 'fire'

def test_group_by():
    df = pd.read_csv('Final/finalalarms.csv')
    start = '2018-01-01'
    end = '2018-01-07'
    df = pd.DataFrame(filter_between_dates(df, start, end))
    grouped_df = pd.DataFrame(group_by(df))
    for row in grouped_df.iterrows():
        assert row['count'] == '349'

pytest.main(["Final/final_test.py"])

