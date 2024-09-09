import pandas as pd
import json

# Convertir posibles listas de diccionarios categorizadas como str en listas
def convert_listdict(value: any) -> list | str | None:
    """
    Convierte una posible lista de diccionarios en formato (type:str) en una lista de diccionarios (type:list).
    Si la entrada es NaN, devuelve None. Si el valor ya es una lista, lo devuelve sin cambios.
    Para entradas str, intenta analizarla como JSON después de reemplazar comillas simples por comillas dobles.
    Si la cadena no es una lista válida, devuelve su forma original de str.

    Parameters:
    --------
    val: Any
        El valor a verificar y convertir, puede ser str, list o Nan.

    Returns:
    --------
    list | str | None:
        list si la conversión es exitosa, str si no puede convertirse en lista, None si ya era nulo.
    """
    
    if pd.isna(value):
        return None

    if isinstance(value, str):
        try:
            # Reemplazar comillas simples por dobles para un JSON válido
            value = value.replace("'", '"')
            # Convertir la cadena a un objeto JSON (lista de diccionarios)
            converted = json.loads(value)
            if isinstance(converted, list) and all(isinstance(item, dict) for item in converted):
                return converted
            else:
                # Si el JSON no es una lista de diccionarios, devolver la cadena original
                return value
        except (ValueError, json.JSONDecodeError) as e:
            #print(f"Error convirtiendo el valor: {val}\nError: {e}") # Usar para ver por que no puede convertirse.
            return value
    
    return value  # Si ya es una lista, lo devolvemos sin cambiar