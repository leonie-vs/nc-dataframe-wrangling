import pandas as pd

def create_df(filename):
    df = pd.read_json(f'data/{filename}')['doughnut_data'].apply(pd.Series)
    return df

df = create_df('doughnuts.json')
print(df)

def increase_price(df, num):
    if num == 0:
        return df
    else:
        perc = num / 100 
        new_df = df.copy()
        new_df['price'] = ((df['price'] * perc) + df['price']).round(2)
        return new_df

df2 = increase_price(df, 10)
print(df2)

def get_best_value(df):
    pass