from src.json_data import create_df, increase_price, get_best_value
import pandas as pd

# Test 1
def test_create_df_returns_dataframe_from_json_file():
    df = create_df('doughnuts.json')
    assert isinstance(df, pd.DataFrame)

# Test 2
def test_increase_price_returns_same_df_when_passed_zero():
    df = create_df('doughnuts.json')
    df2 = increase_price(df, 0)
    assert df.equals(df2)

# Test 3
def test_increase_price_changes_price_by_given_percentage():
    df = create_df('doughnuts.json')
    df2 = increase_price(df, 50)
    assert df2.loc[0, 'price'] == (df.loc[0, 'price'] * 1.50).round(2)
