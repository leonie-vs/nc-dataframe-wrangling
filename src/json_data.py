import pandas as pd
import json

def create_df(filename):
    df = pd.read_json(f'data/{filename}')
    return df

def increase_price(df):
    pass

def get_best_value(df):
    pass