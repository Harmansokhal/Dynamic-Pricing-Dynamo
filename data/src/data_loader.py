import pandas as pd

def load_product_data(file_path):
    """
    Load product data from CSV file.
    """
    df = pd.read_csv(file_path)
    return df
