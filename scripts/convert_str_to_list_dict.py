import pandas as pd
import ast


# Función para convertir str en diccionarios o listas en caso de serlo.
def convert_list_dict(value: any) -> dict | list | None:
    """
    Convierte un posibles diccionarios o listas de diccionarios con (type:str), A su forma real (type:dict|list).
    Si el valor es NaN, devuelve None. Si el valor ya es un diccionario o lista, lo devuelve sin cambios.

    Parameters:
    --------
    val: Any
        El valor a verificar y convertir. Puede ser str, dict, list o NaN.

    Returns:
    --------
    dict |  list | None:
        dict|list si la conversión es exitosa, None si ya era nulo o el valor original.
    """
    
    if pd.isna(value):
        return None

    if isinstance(value, str): 
        try:
            # Reemplazar 'Null' por 'None' para que sea un valor valido en Python.
            value = value.replace('Null', 'None')

            # Evaluar el str como un diccionario o lista usando ast.literal_eval
            return ast.literal_eval(value)
        except (ValueError, SyntaxError) as e:
            print(f"Error convirtiendo el valor: {value}\nError: {e}") # Para depuracion.
            return value
    
    return value  # Si ya es un dict | list, lo devolvemos sin cambios.