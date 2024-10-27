import pandas as pd

def extract_sales_date(file_path):
    "Extract data from CSV file into a DataFrame"
    data = pd.read_csv(file_path)
    return data
