import pandas as pd
from pandas import DataFrame

def desanidar_columnas(df:DataFrame,
                       columna:str,
                       nombre_nueva_tabla: str,
                       indice_increment:int=0) -> DataFrame:
    """
    Desanida una columna en un DataFrame, genera un ID único que relaciona
    la tabla original con nombre_nueva_tabla desanidada.
    Antes de aplicar esta funcion tienes que aplicar la funcion convert_listdict() , o la funcion convert_dict() segun su caso.
    o verificar que el tipo de dato de la columna ya este transformado.

    Parameters:
    ----------
    df (DataFrame):
        DataFrame original, donde se insertara el indice.
    columna (str):
        Nombre de la columna del df a desanidar. Verificar que el tipo de dato este en list, o dict.
    nombre_nueva_tabla (str):
        Nombre de la tabla donde se pondran los datos desanidados.
    nombre_exploded (str):
        Nombre de la tabla donde se pondran los datos de la funcion exlpoded.
    indice_increment (int):
        Valor opcional a sumar al índice para crear el id único.

    Return:
    --------
    nombre_nueva_tabla (DataFrame): Nuevo DataFrame desanidado, con el nombre asignado
    """
    df = df
    
    # Crear el ID único en el DataFrame original
    df[f'{columna}_id'] = df.index + indice_increment

    # Explode para desanidar la columna de listas
    df_exploded = df.explode(columna)

    # Normalizar los datos y creacion de la columna desanidada
    nombre_nueva_tabla = pd.json_normalize(df_exploded[columna])
    # Asignar el ID único para relacionar las tablas
    nombre_nueva_tabla[f'{columna}_id'] = df_exploded[f'{columna}_id'].values

    return nombre_nueva_tabla