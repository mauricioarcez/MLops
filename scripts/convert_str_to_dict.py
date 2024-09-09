import pandas as pd
import ast


# Función para convertir str en diccionarios en caso de serlo.
def convert_dict(value: any) -> dict | str | None:
    """
    Convierte un posible diccionario con (type:str), A su forma verdadera (type:dict).
    Si la fila de entrada es NaN, devuelve None. Si el valor ya es un diccionario, lo devuelve
    sin cambios. Para entradas str, intenta analizarlas como diccionario. Si no es un diccionario ni un nulo, devuelve su forma original de str.

    Parameters:
    --------
    val: Any
        El valor a verificar y convertir, puede ser str, dict o Nan.

    Returns:
    --------
    dict |  str | None:
        dict si la conversión es exitosa, str si no puede convertirse en diccionario, None si ya era nulo.
    """
    
    
    if pd.isna(value):
        return None

    if isinstance(value, str): 
        try:
            # Reemplazar 'Null' por 'None' para que sea un dict válido
            value = value.replace('Null', 'None')

            # Asegurarse de que el valor empiece y termine con { }
            if value.startswith('{') and value.endswith('}'):
                # Evaluar el str como un diccionario usando ast.literal_eval
                return ast.literal_eval(value)
            
            # Si el valor no es un dict válido, devolver la cadena original
            return value
        except (ValueError, SyntaxError) as e:
            #print(f"Error convirtiendo el valor: {value}\nError: {e}") # Usar para ver por que no puede convertirse.
            return value
    
    return value  # Si ya es un diccionario, lo devolvemos sin cambiar