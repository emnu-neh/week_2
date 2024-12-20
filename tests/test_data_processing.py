import pandas as pd
import pytest
import os
from scripts.data_cleaning import remove_outliers, replace_null_value

def test_remove_outliers():
    data={
          'A': [1, 2, 3, 100],  # 100 is an outlier
        'B': [10, 20, 30, 40] 
    }
    df = pd.DataFrame(data)
    filtered_df = remove_outliers(df)

    assert len(filtered_df) == 3
    assert 100 not in filtered_df['A'].values

def test_replace_null_value():
    data = {
        'A': [1, 2, None, 4],
        'B': ['x', None, 'y', 'z'],
        'C': [pd.Timestamp('2022-01-01'), None, pd.Timestamp('2022-01-03'), None]
    }
    df = pd.DataFrame(data)
    columns_with_missing_values = ['A', 'B', 'C']
    updated_df = replace_null_value(df, columns_with_missing_values)
    
    # Verify numeric column replacement
    assert updated_df['A'].isnull().sum() == 0
    assert updated_df['A'].iloc[2] == 2.3333333333333335  # Mean of [1, 2, 4]
    
    # Verify object column replacement
    assert updated_df['B'].isnull().sum() == 0
    assert updated_df['B'].iloc[1] == 'x'  # Mode of ['x', 'y', 'z']
    
    # Verify datetime column replacement
    assert updated_df['C'].isnull().sum() == 0
    assert updated_df['C'].iloc[1] == pd.Timestamp('2022-01-01')