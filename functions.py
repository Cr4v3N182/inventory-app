import pandas as pd
import uuid


def get_items():
    df = pd.read_csv("data.csv")
    return df.values.tolist()

def generate_unique_id():
    unique_id = str(uuid.uuid4())[:5].upper()  # Extract the first 5 characters
    return unique_id
