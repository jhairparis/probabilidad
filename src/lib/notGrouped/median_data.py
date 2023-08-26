from pandas import DataFrame

def median_no_grouped(base:DataFrame, column:str):
    return base[column].median()
