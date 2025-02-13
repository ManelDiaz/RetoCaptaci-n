def transform(data):
    df = data.copy() 

    df['nombre'] = df['nombre'].str.upper()
    df['apellido'] = df['apellido'].str.upper()
    df['edad'] = df['edad'].astype(int)
    df['salario'] = df['salario'].round().astype(int)

    return df