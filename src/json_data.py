import pandas as pd

def create_df(filename):
    df = pd.read_json(f'data/{filename}')
    return df

def increase_price(df, num):
    if num == 0:
        return df
    
def get_best_value(df):
    pass