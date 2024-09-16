# Proyecto: API de Recomendación de Películas

## Descripción

Este repositorio contiene el desarrollo de una **API** diseñada para integrarse con servicios de streaming, ofreciendo funcionalidades como la **recomendación de películas**, y la obtención de información sobre **actores** y **directores** junto con la cantidad de películas en las que han participado.

El proyecto emplea un enfoque integral de **Data Engineering** y **Data Science**, combinando un modelo de **Machine Learning** que recomienda películas basándose en la **similitud entre ellas**. Para ello, se utilizan técnicas de **procesamiento de lenguaje natural (NLP)**, específicamente la **similitud del coseno**, y un exhaustivo **análisis estadístico de los datos** mediante librerías avanzadas de Python.

El objetivo principal es **desplegar** un sistema eficiente de recomendaciones en la plataforma **Render**, optimizado para su funcionamiento en el plan gratuito. El sistema está diseñado para procesar y analizar grandes volúmenes de datos de forma efectiva, brindando recomendaciones personalizadas y actualizadas en tiempo real.

## Tabla de Contenido
- [Introducción](#Descripción)
- [Instalación y Requisitos](#instalación-y-requisitos)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Uso y Ejecución](#uso-y-ejecución)
- [Datos y Fuentes](#datos-y-fuentes)
- [Metodología](#metodología)
- [Despliegue](#despliegue)
- [Resultados y Links al proyecto](#resultados-y-links-al-proyecto)
- [Contribución y Colaboración](#contribución-y-colaboración)
- [Licencia](#licencia)

## Instalación y Requisitos
Para ejecutar este proyecto, deberas tener instalado y descargado:
- Python 3.11
- Datasets en formato CSV sin procesar descargados, [**Link**](https://drive.google.com/drive/folders/1X_LdCoGTHJDbD28_dJTxaD4fVuQC9Wt5)
- Librerías necesarias (consultar `requirements.txt`)

### Instalación

1. **Clona el repositorio**:
    ```bash
    git clone https://github.com/tu_usuario/tu_proyecto.git
    ```

2. **Navega al directorio del proyecto**:
    ```bash
    cd tu_proyecto
    ```

3. **Crea un entorno virtual** (recomendado para gestionar las dependencias del proyecto de manera aislada):
    ```bash
    python -m venv tu_entorno
    ```

4. **Activa el entorno virtual**:
    - **En Windows**:
        ```bash
        tu_entorno\Scripts\activate
        ```
    - **En macOS/Linux**:
        ```bash
        source tu_entorno/bin/activate
        ```

5. **Crea el archivo `.gitignore`** y excluye los archivos y carpetas innecesarios del control de versiones:
    ```bash
    touch .gitignore
    ```

    Abre el archivo `.gitignore` y agrega las siguientes líneas para excluir la carpeta `data/raw/` (Archivos crudos que solo consumiran espacio)y `tu_entorno`:

    ```bash
    # Ignorar la carpeta de datos crudos
    data/raw/

    # Ignorar el entorno virtual
    tu_entorno/
    ```

5. **Instala las dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

## Estructura del Proyecto

La estructura del proyecto es la siguiente:

- **app/**: Contiene el archivo principal de la API, donde se encuentran los decoradores y las funciones que serán consumidos por los endpoints.
  
- **data/**: Almacena los archivos de datos utilizados en el proyecto, tanto antes como después del procesamiento.
  - **raw/**: Archivos de datos sin procesar (esta carpeta debe añadirse al `.gitignore`).
  - **processed/**: Datos procesados, listos para ser consumidos por la API o el modelo.

- **notebooks/**: Contiene los notebooks de Jupyter donde se realiza el ETL, EDA, y entrenamiento del modelo. Necesarios para cada archivo CSV.
    - **etl**: Aplica transformaciones y limpieza de los archivos. 
    - **eda**: Aplica Análisis Exploratorio de los datos para encontrar datos interesantes.
    - **modelo**: Se entrena el modelo de recomendación.

- **scripts/**: Incluye funciones reutilizables y escalables para tareas como desanidado, preprocesamiento y conversiones de datos.

- **requirements.txt**: Lista de dependencias y bibliotecas necesarias para ejecutar el proyecto.

- **README.md**: Documentación del proyecto con instrucciones detalladas de uso y despliegue.

- **runtime.txt**: Archivo que especifica la versión de Python necesaria para el despliegue en Render.

## Uso y Ejecución

1. Asegúrate de tener los archivos de datos crudos en el directorio `data/raw/`:
    - `movies_dataset.csv`
    - `credits.csv`

2. Ejecuta el notebook `/etl_movies_dataset.ipynb`, Configura las rutas propias:
    - Este notebook convierte el archivo CSV a formato `parquet`, aplica transformaciones y guarda los datos procesados en `data/processed/movies/`.

3. Ejecuta el notebook `/etl_credits.ipynb`, Configura las rutas propias:
    - Este notebook convierte el archivo CSV a formato `parquet`, aplica transformaciones y guarda los datos procesados en `data/processed/credits/`.

4. Ejecuta el notebook `/eda.ipynb`, Configura las rutas propias:
    - Este notebook realiza un análisis exploratorio de datos y preprocesa la información para el modelo de recomendación. Los resultados se almacenan en `data/processed/`.

5. Ejecuta el notebook `/model_test.ipynb`, Configura las rutas propias:
    - Este notebook entrena el modelo de recomendación y guarda el modelo entrenado en formato `.pkl`, ubicado en `data/processed/`.

6. Inicia la aplicación FastAPI en local utilizando el siguiente comando:
   ```bash
   fastapi dev app/main.py

## Datos y Fuentes

- [**Datasets**](https://drive.google.com/drive/folders/1X_LdCoGTHJDbD28_dJTxaD4fVuQC9Wt5): Carpeta con los 2 archivos con datos que requieren ser procesados (movies_dataset.csv y credits.csv), hay datos que estan anidados (un diccionario o una lista como valores en la fila).

- [**Diccionario de datos**](https://docs.google.com/spreadsheets/d/1QkHH5er-74Bpk122tJxy_0D49pJMIwKLurByOfmxzho/edit?gid=0#gid=0): Diccionario con algunas descripciones de las columnas disponibles en el dataset.

## Metodología

### Optimización de Recursos
- Dado que desplegaremos el proyecto en un servicio gratuito de Render, es esencial optimizar al máximo el tamaño de los archivos y el uso de memoria. Para lograr esto, se han aplicado las siguientes transformaciones:
  1. **Conversión de archivos CSV a formato `parquet`**: Este formato ofrece beneficios en términos de memoria debido a su almacenamiento columnar.
     - En la carpeta `scripts` encontrarás el procedimiento y el uso de la función de conversión en `convert_csv_to_parquet.py`.
  2. **Eliminación de valores nulos, duplicados, películas no publicadas, y columnas no utilizadas**: Estas acciones ayudan a reducir el tamaño de los datos y mejorar la eficiencia.

### Desanidado de Columnas
- Los archivos contienen columnas anidadas en formato string, que son diccionarios o listas de diccionarios y dificultan el acceso a la información.
  1. **Desanidamiento de columnas**: Convertir estas columnas anidadas para mejorar el acceso a la información por parte de la API y su velocidad de respuesta.
     - En la carpeta `scripts` encontrarás el procedimiento y el uso de la función de conversión a lista en `convert_str_to_list.py` y la función de desanidado en `desanidar_columnas.py`.
  2. **Creación de tablas adicionales**: La lógica de desanidamiento crea tablas adicionales que se conectan con un `ID` único a la tabla original. Se han creado las siguientes tablas adicionales:
     - `genres_desanidado`
     - `pc_desanidado`
     - `pctry_desanidado`
     - `slan_desanidado`
     - `cast_desanidado`
     - `crew_desanidado`

### Exportación Solo de Tablas Necesarias
- Aunque hemos desanidado todas las columnas en tablas, no todas serán utilizadas. Podemos eliminar las que no sean necesarias.
  1. Desde el proceso de `ETL`, el nuevo DataFrame se exporta a `EDA`. Desde `EDA`, el DataFrame se exporta al notebook de `Modelo`, y desde allí a la API.

### Análisis Exploratorio de Datos (EDA)
- Para optimizar el DataFrame y mejorar la calidad de los datos, se han aplicado diversas técnicas de visualización y análisis estadístico. Estas incluyen:
  1. **Distribución de los Datos y Relleno de Valores Faltantes**: Se ha utilizado la mediana para rellenar valores faltantes debido a la presencia de altos valores atípicos (outliers).
  2. **Agrupamiento de Datos Numéricos en Categóricos**: Se ha realizado la conversión de datos numéricos en categorías para facilitar una mejor clasificación.
  3. **Visualización de Datos**: Se han creado gráficos de barras horizontales y verticales para una representación clara de la cantidad de datos.
  4. **Eliminación de Columnas No Necesarias**: Se han eliminado columnas que eran útiles para otras funciones de la API pero no para el modelo, con el fin de optimizar el espacio.
  5. **Análisis de Tendencias Temporales**: Se han analizado las tendencias a lo largo del tiempo para identificar patrones en los datos.
  6. **Gráfico de Líneas por Popularidad**: Se han generado gráficos de líneas agrupados por popularidad para observar tendencias en la popularidad de las películas.
  7. **Agrupación por Idiomas**: Se ha agrupado la información por idiomas, excluyendo aquellos con menos de 1000 películas para evitar datos irrelevantes.
  8. **Transformación Logarítmica de Datos Numéricos**: Se ha aplicado una transformación logarítmica para visualizar distribuciones sesgadas y analizar los cuartiles.
  9. **Matriz de Correlación**: Se ha creado una matriz de correlación para variables numéricas tanto normales como logarítmicas, utilizando mapas de calor para identificar relaciones entre variables.
  10. **Preprocesamiento de Lenguaje Natural (NLP)**: Se ha utilizado la librería NLTK para el procesamiento de texto.
  11. **Técnicas de NLP Adicionales**: Se han aplicado expresiones regulares, tokenización, eliminación de nombres propios, stop-words y lematización para limpiar y preparar el texto.
  12. **Asignación de Pesos a Variables Importantes**: Se ha realizado una prueba para añadir peso a las variables más importantes para la predicción, evaluando el impacto de cada peso en el modelo.

### Modelado del Sistema de Recomendación
- Una vez que tenemos los títulos de las películas y la variable predictora, los pasos siguientes son entrenar el modelo, evaluar su uso de memoria y analizar los resultados. El proceso incluye:

  1. **Creación y Entrenamiento del Vectorizador TF-IDF**: 
     - Se utiliza el vectorizador TF-IDF (Term Frequency-Inverse Document Frequency) para convertir el texto de las variables predictoras en una representación numérica que refleja la importancia de cada término en el contexto de las películas.
  
  2. **Reducción de Dimensionalidad**:
     - Se aplica **TruncatedSVD** (Singular Value Decomposition truncada) para reducir la dimensionalidad del espacio vectorial. Esta técnica reduce el número de características al conservar las dimensiones más importantes, simplificando el modelo y mejorando la eficiencia.

  3. **Uso de la Técnica de Similitud del Coseno**:
     - La similitud del coseno se utiliza para comparar la similitud entre los títulos de las películas. Para reducir la complejidad, se compara solo la matriz de similitud del coseno con el título ingresado, en lugar de la matriz completa.

  4. **Verificación del Uso de Memoria y Espacio**:
     - Se analiza el uso de memoria y espacio durante las pruebas para encontrar las configuraciones más eficientes para los componentes de TruncatedSVD y los parámetros del vectorizador, sin comprometer la calidad de las recomendaciones.

  5. **Ajuste de Pesos en Variables Predictoras**:
     - Se ajustan los pesos de variables como géneros, descripciones, compañías y actores para mejorar la precisión de las recomendaciones. Se prueban diferentes combinaciones de pesos para optimizar el rendimiento del modelo.

  6. **Guardado del Modelo Entrenado**:
     - El modelo entrenado y la matriz resultante se guardan en formato `.pkl`. Esto evita la necesidad de reentrenar el modelo en cada ejecución y permite realizar comparaciones rápidas con las 5 similitudes más cercanas.

### Creación de las Funciones en la API
- La implementación de la API en FastAPI se ha realizado con el siguiente enfoque:

  1. **Definición de Rutas y Funciones**:
     - Se han creado rutas específicas en el archivo `app/main.py` para manejar las solicitudes de información. Por ejemplo:
       - `@app.get("/recomendaciones/{titulo}")`: Ruta para obtener recomendaciones basadas en el título de una película.
       - `@app.get('/votos_titulo/{titulo}')`: Ruta para obtener la cantidad de votos recibidos en TMDB y el valor promedio de votaciones.
     - Las funciones correspondientes consultan los DataFrames procesados y devuelven respuestas en formato JSON.

## Despliegue

Para desplegar el proyecto en Render, sigue estos pasos:

1. **Crea una cuenta en [Render](https://render.com)** y conecta tu repositorio de GitHub.

2. **Define el comando de inicio** en Render:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 10000

3. **Consultar la Documentación**:
   - Consulta la [documentación de Render](https://render.com/docs) si necesitas más detalles o asistencia.

## Resultados y links al proyecto

- **Link a la API**: [API en Render](https://mlops-8vmz.onrender.com/docs)
- **Link al video explicativo en YouTube**: [Video Explicativo](URL_DEL_VIDEO) (poner video)

### Foto de la Recomendación
![Descripción de la imagen](https://drive.google.com/uc?export=view&id=1Tn8N49GXxno9dciR-6fwdYwfSb90liuW)






