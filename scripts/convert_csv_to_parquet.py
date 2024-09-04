import pandas as pd


#Asegurate de tener instaladas las librerias necesarias de requirements.txt.
def convert_csv_to_parquet(
    csv_file: str,
    parquet_file: str,
    columns_to_drop: list = None,
    dtype_conversion: dict = None,
    fillna_values: dict = None
) -> None:
    '''
    Convierte un CSV a formato .parquet, opcionalmente puedes eliminar columnas, especificar tipo de dato de las columnas y rellenar valores nulos.

    Parameters:
    -----------
    csv_file : str
        Ruta del archivo CSV.
    parquet_file : str
        Ruta donde se guarda el parquet.
    columns_to_drop : list, opcional
        Lista de las columnas que se eliminaran del dataset antes de transformarlo.
    dtype_conversion dict, opcional
        Diccionario especificando las columnas a convertir con su tipo de dato. (column: type)
    fillna_values: dict = None
        Diccionario especificando las columnas que van a rellenarse sus valores nulos con valores establecidos por el usuario. (column: value)
        
    Returns:
    --------
    None
    '''
    
    df = pd.read_csv(csv_file)
    
    
    if columns_to_drop is not None:
        df = df.drop(columns=columns_to_drop)
    
    if fillna_values:
        df.fillna(value=fillna_values, inplace=True)
        
    if dtype_conversion is not None:
        for column, dtype in dtype_conversion.items():
            if column in df.columns:
                try:
                    df[column] = df[column].astype(dtype)
                except ValueError:
                    print(f"Warning: Conversion de columna '{column}' a '{dtype}' fallo. se intentara con pd.to_numeric.")
                    df[column] = pd.to_numeric(df[column], errors='coerce')
                except TypeError:
                    # Handle cases where dtype is not valid
                    print(f"Error: Tipo '{dtype}' no es valido para la columna '{column}'.")
      
        
    df.to_parquet(parquet_file, engine='pyarrow', compression='snappy', index=False)




convert_csv_to_parquet(
    r'C:\Users\mauri\OneDrive\Escritorio\MLops\data\raw\movies_dataset.csv',
    r'C:\Users\mauri\OneDrive\Escritorio\MLops\data\raw\movies_dataset.parquet',
    columns_to_drop=['video','imdb_id','adult','original_title','poster_path','homepage'],
    fillna_values={'revenue': 0, 'budget': 0},
    dtype_conversion={'popularity': 'float64', 'budget':'int64','id':'int64'}
)

convert_csv_to_parquet(
    r'C:\Users\mauri\OneDrive\Escritorio\MLops\data\raw\credits.csv',
    r'C:\Users\mauri\OneDrive\Escritorio\MLops\data\raw\credits.parquet'
)