import pandas as pd

def get_items():
    df = pd.read_csv("data.csv")
    return df.values.tolist()
print(get_items())