import pandas as pd

def transform_sales_data(data):
    "Cleans and aggregates sales data"
    data = data.drop_duplicaltes()
    data['sale_amount'] = data['quantity']* data['unit_price']
    summary = data.groupby('product').agg({'sale_amount':'sum'}).reset_index()
    return summary