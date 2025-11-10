from src.json_data import create_df, increase_price, get_best_value
import pandas as pd

# Test 1
def test_create_df_returns_dataframe_from_json_file():
    df = create_df('doughnuts.json')
    assert isinstance(df, pd.DataFrame)

# Test 2
