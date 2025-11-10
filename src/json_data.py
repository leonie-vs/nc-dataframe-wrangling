import pandas as pd

def create_df(filename):
    df = pd.read_json(f'data/{filename}')['doughnut_data'].apply(pd.Series)
    return df

def increase_price(df, num):
    if num == 0:
        return df
    else:
        perc = num / 100 
        new_df = df.copy()
        new_df['price'] = ((df['price'] * perc) + df['price']).round(2)
        return new_df

def get_best_value(df):
    new_df = df.copy()
    new_df['cost_per_calorie'] = df['price'] / df['calories']
    return df[new_df['cost_per_calorie'] == new_df['cost_per_calorie'].min()]
