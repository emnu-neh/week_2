import pandas as pd
def remove_outliers(df):
    columns = df.select_dtypes(include=['float64', 'int64']).columns
    for column in columns:
        Q1 =df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]    
        return df
    
def replace_null_value(df,columns_with_missing_values):
    for column in columns_with_missing_values:
        if df[column].dtype in ['float64','int64']:
            df[column].fillna(df[column].mean(),inplace=True)
        elif df[column].dtype == 'object':
            df[column].fillna(df[column].mode()[0],inplace=True)
        elif pd.api.types.is_datetime64_any_dtype(df[column]): 
            df[column].fillna(method='ffill', inplace=True)
    return df