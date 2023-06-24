"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():

    with open('clusters_report.txt', 'r') as file:
        lines = file.readlines()

    # Eliminar las líneas en blanco y las líneas de separación
    lines = [line.strip() for line in lines if line.strip() != '' and not line.startswith('-')]

    # Crear un diccionario con las columnas del DataFrame
    columns = ['Cluster', 'Cantidad_de_palabras_clave', 'Porcentaje_de_palabras_clave', 'Principales_palabras_clave']
    data_dict = {column: [] for column in columns}

    # Agregar los datos al diccionario
    for line in lines:
        values = line.split(maxsplit=3)
        if len(values) == 4:
            for i, value in enumerate(values):
                if i == 3:
                    keywords = value.split(', ')
                    data_dict[columns[i]].append(keywords)
                else:
                    data_dict[columns[i]].append(value)

    # Crear el DataFrame a partir del diccionario
    df = pd.DataFrame(data_dict)

    # Reemplazar los espacios por guiones bajos en los nombres de las columnas
    df.columns = df.columns.str.replace(' ', '_').str.lower()
    return df

#print(ingest_data())