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
        price = df['price']
        increase_by = num / 100
        new_df = df * increase_by
    
def get_best_value(df):
    pass