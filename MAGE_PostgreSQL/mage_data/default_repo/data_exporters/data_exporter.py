import pandas as pd
from sqlalchemy import create_engine

@data_exporter
def export_data(df):
    engine = create_engine('postgresql://username:password@postgres:5432/postgres')
    df.to_sql('usuarios_destino', engine, if_exists='replace', index=False)

