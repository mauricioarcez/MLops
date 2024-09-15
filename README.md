# Proyecto: Sistema de Recomendación de Películas

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
- [Resultados y Conclusiones](#resultados-y-conclusiones)
- [Contribución y Colaboración](#contribución-y-colaboración)
- [Licencia](#licencia)

## Instalación y Requisitos
Para ejecutar este proyecto, asegúrate de tener instalado:
- Python 3.11
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
    python -m venv venv
    ```

4. **Activa el entorno virtual**:
    - **En Windows**:
        ```bash
        venv\Scripts\activate
        ```
    - **En macOS/Linux**:
        ```bash
        source venv/bin/activate
        ```

5. **Instala las dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

## Estructura del Proyecto

La estructura del proyecto es la siguiente:

tu_proyecto/
├── app/                      # Código principal de la aplicación.
│   └── main.py               # Archivo principal para ejecutar la API.
├── data/                     # Datasets del proyecto. Antes y despues de procesar.
│   ├── raw/                  # Datos en bruto (sin procesar).
│   └── processed/            # Datos procesados listos para ser consumidos por la API.
├── notebooks/                # Notebooks Jupyter de los ETL, EDA, y pruebas del modelo.
│   ├── etl.movies.ipynb      # Notebooks para la transformación del CSV de las peliculas.
│   ├── etl.credits.ipynb     # Notebooks para la transformación del CSV de los creditos.
│   └── eda.ipynb             # Notebooks para el análisis exploratorio de datos luego del ETL.
│   └── model_test.ipynb      # Implementacion y pruebas del modelo luego del EDA.
├── scripts/                  # Todas las funciones utilizadas en el proyecto.
│   └── *                     # Funciones de desanidado, pre-procesamiento, conversion, etc.
├── requirements.txt          # Archivo con las dependencias del proyecto.
├── README.md                 # Este archivo con la documentacion del proyecto.
└── .gitignore                # Archivos y carpetas a ignorar por Git.
└── runtime.txt               # Especificacion de la version de Python.


