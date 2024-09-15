Proyecto: Sistema de Recomendación de Películas
Descripción
Este repositorio contiene el desarrollo de una API diseñada para integrarse con servicios de streaming, ofreciendo funcionalidades como la recomendación de películas, y la obtención de información sobre actores y directores junto con la cantidad de películas en las que han participado.

El proyecto emplea un enfoque integral de Data Engineering y Data Science, combinando un modelo de Machine Learning que recomienda películas basándose en la similitud entre ellas. Para ello, se utilizan técnicas de procesamiento de lenguaje natural (NLP), específicamente la similitud del coseno, y un exhaustivo análisis estadístico de los datos mediante librerías avanzadas de Python.

El objetivo principal es desplegar un sistema eficiente de recomendaciones en la plataforma Render, optimizado para su funcionamiento en el plan gratuito. El sistema está diseñado para procesar y analizar grandes volúmenes de datos de forma efectiva, brindando recomendaciones personalizadas y actualizadas en tiempo real.

Introducción
Instalación y Requisitos
Estructura del Proyecto
Uso y Ejecución
Datos y Fuentes
Metodología
Resultados y Conclusiones
Contribución y Colaboración
Licencia
1. Introducción
Este proyecto está centrado en crear un sistema de recomendación de películas, utilizando técnicas avanzadas de procesamiento de texto y análisis de similitud. El sistema toma descripciones de películas y recomienda títulos similares basados en sus características.

2. Instalación y Requisitos
Requisitos del Sistema
Python 3.11
Pip para la instalación de dependencias
Dependencias
Todas las dependencias están listadas en requirements.txt. Instálalas con el siguiente comando:

bash
Copiar código
pip install -r requirements.txt
Librerías Clave
pandas
scikit-learn
fastapi
psutil
3. Estructura del Proyecto
La estructura del proyecto es la siguiente:

bash
Copiar código
├── app/
│   └── main.py                # Archivo principal para correr la API
├── data/
│   ├── raw/                   # Datos crudos
│   └── processed/             # Datos procesados
├── notebooks/
│   ├── etl.movies.ipynb       # Notebook de ETL para películas
│   ├── etl.credits.ipynb      # Notebook de ETL para créditos
│   └── eda.ipynb              # Análisis exploratorio de datos
├── scripts/                   # Scripts de funciones y procesos
│   └── *.py
├── requirements.txt           # Lista de dependencias
└── README.md                  # Documentación del proyecto
4. Uso y Ejecución
Clonar el repositorio:
bash
Copiar código
git clone <url-del-repositorio>
Instalar las dependencias:
bash
Copiar código
pip install -r requirements.txt
Ejecutar la API:
Para ejecutar la API de recomendación de películas, utiliza el siguiente comando:

bash
Copiar código
uvicorn app.main:app --reload
La API estará disponible en localhost:8000. Puedes hacer solicitudes para obtener recomendaciones basadas en el título de la película o su descripción.

5. Datos y Fuentes
Los datos utilizados en este proyecto provienen de fuentes públicas de películas. Los datasets se encuentran en formato Parquet y contienen información detallada de cada película:

movies_dataset.parquet: Información básica de cada película.
credits_dataset.parquet: Datos del elenco y equipo de producción.
6. Metodología
La metodología aplicada para este proyecto se basa en las siguientes etapas:

Preprocesamiento de datos: Limpieza, transformación y tokenización del texto.
Vectorización: Uso de TF-IDF para convertir descripciones de películas en vectores.
Reducción de Dimensiones: Aplicación de TruncatedSVD para reducir el número de características.
Similitud del Coseno: Cálculo de la similitud entre las películas en base a las descripciones vectorizadas.
7. Resultados y Conclusiones
El sistema de recomendación fue capaz de identificar películas similares basadas en su descripción textual. Los resultados muestran que la combinación de TF-IDF y similitud del coseno ofrece una buena aproximación para generar recomendaciones de películas, aunque se podrían explorar mejoras en la selección de características.

8. Contribución y Colaboración
Si deseas contribuir a este proyecto, puedes seguir estos pasos:

Haz un fork del repositorio.
Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
Haz commit de tus cambios (git commit -m 'Agrega nueva funcionalidad').
Haz push a la rama (git push origin feature/nueva-funcionalidad).
Abre un Pull Request para revisión.
9. Licencia
Este proyecto está licenciado bajo la licencia MIT. Puedes ver más detalles en el archivo LICENSE.
