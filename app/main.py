from fastapi import FastAPI
import pandas as pd

app = FastAPI()


# Cargamos el Dataframe movies procesado luego del etl.
df = pd.read_parquet('data/processed/movies/movies_dataset_etl.parquet')

# Cargamos el Dataframe credits procesado luego del etl.
df_cast = pd.read_parquet('data/processed/credits/cast_desanidado.parquet')
df_crew = pd.read_parquet('data/processed/credits/crew_desanidado.parquet')


# Diccionario para mapear meses en español a números
meses = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4,
    "mayo": 5, "junio": 6, "julio": 7, "agosto": 8,
    "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
}

# Diccionario para mapear dias en español a números. 
dias = {
    "lunes": 0, "martes": 1, "miercoles": 2, "jueves": 3,
    "viernes": 4, "sabado": 5, "domingo": 6
}



@app.get("/")
async def root():
    return {"message": "/docs/ para ver la api."}



@app.get("/cantidad_filmaciones_mes/{mes}")
async def cantidad_filmaciones_mes(mes: str) -> dict:
    '''
    Devuelve la cantidad de peliculas estrenadas en el mes indicado.
    
    Parameters.
    -----------
    mes (str):
        Nombre del mes en español. (ej: Enero)
        
    Returns
    --------
    JSON message (dict):
        La cantidad de peliculas estrenadas en el mes.
    '''
    # Convertir el mes a minúsculas para evitar problemas de capitalización
    mes = mes.lower()
    
    # Verificar que el mes está en el diccionario
    if mes not in meses:
        return {"error": "Mes no válido. Introduzca un mes en español."}
    
    # Obtener el número del mes a travez del diccionario creado.
    numero_mes = meses[mes]
    
    # Contar cuántas películas fueron estrenadas en ese mes
    cantidad = df[df['release_date'].dt.month == numero_mes].shape[0]
    
    return {"message": f"{cantidad} películas fueron estrenadas en los meses de {mes.capitalize()}"}



@app.get("/cantidad_filmaciones_dia/{dia}")
async def cantidad_filmaciones_dia(dia: str) -> dict:
    '''
    Devuelve la cantidad de peliculas estrenadas en el nombre del día indicado.
    
    Parameters.
    -----------
    dia (str):
        Nombre del día en español, sin tildes. (Ej: Martes)
        
    Returns
    --------
    JSON message (dict):
        La cantidad de peliculas estrenadas en el día.
    '''
    # Convertir el dia a minúsculas para evitar problemas de capitalización
    dia = dia.lower()
    
    # Verificar que el día está en el diccionario
    if dia not in dias:
        return {"error": "Día no válido. Introduzca un día en español, sin tildes. Entre Lunes y Domingo."}
    
    # Obtener el número del mes a travez del diccionario creado.
    numero_dia = dias[dia]
    
    # Contar cuántas películas fueron estrenadas en ese día.
    cantidad = df[df['release_date'].dt.dayofweek == numero_dia].shape[0]
    
    return {"message": f"{cantidad} películas fueron estrenadas en los días {dia.capitalize()}"}



@app.get('/score_titulo/{titulo}')
async def score_titulo(titulo: str) -> dict:
    '''
    Retorna el titulo, año de estreno y la popularidad de la pelicula ingresada.
    
    Parameters
    ---------
    titulo (str):
        El titulo de la pelicula en ingles/español. (ej: Toy Story)
        
    Returns
    -------
    JSON message (dict):
        El titulo de la pelicula si existiese, su año de estreno y su popularidad.
    
    '''
    # Para evitar problemas de capitalización. Verifica que el dataframe tambien este en minusculas.
    titulo = titulo.lower()
    
    # Busca el titulo en el DataFrame
    pelicula = df[df['title'] == titulo]
    
    if pelicula.empty:
        return {"message": f"No se encontró la película '{titulo}. Verifica los espacios o el nombre correcto en ingles/español.'"}
    
    anio = pelicula['release_year'].values[0]
    score = pelicula['popularity'].values[0]
    
    return {"message": f"La pelicula {titulo} fue estrenada en el año {anio} con un score/popularidad de {score}."}



@app.get('/votos_titulo/{titulo}')
async def votos_titulo(titulo: str) -> dict:
    '''
    Retorna el titulo, la cantidad de votos recibidos en TMDB y el valor promedio de las votaciones.
    el titulo deberá contar con al menos 2000 valoraciones en TMDB para mostrar los resultados.
    
    Parameters:
    ----------
    titulo (str):
        El titulo de la pelicula en ingles/español. (ej: Toy Story)
        
    Returns:
    --------
    JSON message (dict):
        El titulo de la pelicula si existiese, su año de estreno, su cantidad de votos en TMDB y el promedio de votos.
        Si, solo si el titulo cuenta con mas de 2000 votos.
    '''
    # Para evitar problemas de capitalización. Verifica que el dataframe tambien este en minusculas.                    
    titulo = titulo.lower()
    
    # Busca el titulo en el DataFrame
    pelicula = df[df['title'] == titulo]
    
    if pelicula.empty:
        return {"message": f"No se encontró la película '{titulo}. Verifica los espacios o el nombre correcto en ingles/español.'"}
    
    votos = pelicula['vote_count'].values[0]
    
    if votos < 2000:
        return {"message": "La pelicula cuenta con menos de 2000 valoraciones, elige otra pelicula."}
    
    anio = pelicula['release_year'].values[0]
    promedio = pelicula['vote_average'].values[0]

    return {"message": f"La película {titulo} fue estrenada en el año {anio}. La misma cuenta con un total de {votos} valoraciones, con un promedio de {promedio}"}



@app.get('/obtener_actor/{actor}')
async def get_actor(actor: str) -> dict:
    '''
    Muestra la cantidad de peliculas en las que participo el actor y las ganancias totales generadas  
    por las peliculas que participo, con su promedio de retorno total. La funcion no considera directores.
    
    Parameters:
    -----------
    actor (str):
        Nombre y apellido real del actor a verificar.
        
    Returns:
    ---------
    JSON message (dict): 
        El actor X ha participado de X filmaciones, el mismo ha conseguido un retorno de X veces la inversion. Con un promedio de X por filmación
    '''
    # Para evitar problemas de capitalización. Verifica que el dataframe tambien este en minusculas. 
    actor = actor.lower()
    
    # Filtra el dataset por el actor ingresado.
    filtro_actor = df_cast[df_cast['name'] == actor]
    
    if filtro_actor.empty:
        return {"message": f"El actor {actor} no se encontró en la base de datos."}
    
    # Cuenta sus peliculas con el id del dataframe original.
    cantidad_peliculas = filtro_actor['id_df'].nunique()
    
    # Array con los id de las peliculas .
    array_peliculas = filtro_actor['id_df'].unique()
    
    # Coincidencias del actor con los id.
    coincidencias = df[df['id'].isin(array_peliculas)]
    
    # Suma de retornos del actor.
    retorno = round(coincidencias['return'].sum(),2)
    # Promedio
    promedio = round(coincidencias['return'].mean(),2)
    
    
    return {"message": f"El actor {actor} ha participado de {cantidad_peliculas} filmaciones, el mismo ha conseguido un retorno de {retorno} veces la inversion. Con un promedio de {promedio} por filmación"} 



@app.get('/obetener_director/{director}')
async def get_director(director: str) -> dict:
    '''
    Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno.
    Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma
    
    Parameters:
    --------
    director (str): 
        Nombre  y apellido real del director a verificar.
        
    Returns:
    --------
    
    '''
    # Para evitar problemas de capitalización. Verifica que el dataframe tambien este en minusculas. 
    director = director.lower()
    
    return {"message": f"{director}"}