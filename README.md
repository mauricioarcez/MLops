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

app/: Contiene el archivo principal de la API con la lógica de recomendación.
data/: Contiene los archivos de datos utilizados en el proyecto.
    ├── raw/: Datos sin procesar.
    ├── processed/: Datos procesados y utilizados en el modelo.
notebooks/: Incluye los notebooks de Jupyter con el análisis exploratorio (EDA) y transformaciones.
scripts/: Código fuente del proyecto, incluyendo scripts y funciones de transformación.
    ├── convert_csv_to_parquet.py: Script para convertir archivos CSV a formato Parquet.
    ├── etl.py: Script de ETL para transformar y limpiar datos.
requirements.txt: Lista de dependencias y librerías necesarias para ejecutar el proyecto.
README.md: Archivo de documentación del proyecto con instrucciones de uso y despliegue.



