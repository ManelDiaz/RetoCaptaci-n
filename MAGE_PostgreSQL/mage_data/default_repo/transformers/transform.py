import pandas as pd

@transformer
def transform(data):
    if isinstance(data, pd.DataFrame):
        if 'edad' in data.columns:
            data['edad'] = data['edad'] + 2
    return data
