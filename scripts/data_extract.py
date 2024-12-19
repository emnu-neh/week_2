import pandas as pd
def excel_data_loader(path):
    df = pd.read_excel(path,engine='openpyxl')
    return df
