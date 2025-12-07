"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

import pandas as pd
import os
import re
def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """

    df = pd.read_csv('files/input/solicitudes_de_credito.csv', sep=';', index_col=0)

    acentos = str.maketrans('áéíóú', 'aeiou')
    columnas_texto = [
        'sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'línea_credito'
    ]
    for col in columnas_texto:
        df[col] = df[col].str.strip().str.lower()
        df[col] = df[col].str.translate(acentos)
        df[col] = df[col].str.replace('-', '', regex=False)
        df[col] = df[col].str.replace('_', '', regex=False)
        df[col] = df[col].str.replace('.', '', regex=False)
        df[col] = df[col].str.replace(' ', '', regex=False)


    ###
    df["barrio"] = df["barrio"].str.lower().str.replace("_", " ").str.replace("-", " ")
    #
    
    #comuna


    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(int)

    df["fecha_de_beneficio"] = pd.to_datetime(df["fecha_de_beneficio"], dayfirst=True, format="mixed")

    df["monto_del_credito"] = df["monto_del_credito"].str.strip().str.strip("$").str.replace(".00", "").str.replace(",", "").astype(int)


    #eliminacion nulos y duplicados
    df = df.dropna(how='any').drop_duplicates()

    #guardado datos
    os.makedirs('files/output', exist_ok=True)
    df.to_csv('files/output/solicitudes_de_credito.csv', sep=';', index=False)
    return df



for col in pregunta_01().columns[2:4]:
    print(f"Columna: {col}")
    vc = pregunta_01()[col].value_counts()
    for valor, cuenta in vc.items():
        print(f"  {valor!r}: {cuenta}")
    print()


