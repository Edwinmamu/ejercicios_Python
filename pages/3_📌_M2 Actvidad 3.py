import streamlit as st

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 3")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad es una introducción práctica a Python y a las estructuras de datos básicas.
En ella, exploraremos los conceptos fundamentales de Python y aprenderemos a utilizar variables,
tipos de datos, operadores, y las estructuras de datos más utilizadas como listas, tuplas,
diccionarios y conjuntos.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Comprender los tipos de datos básicos en Python
- Aprender a utilizar variables y operadores
- Dominar las estructuras de datos fundamentales
- Aplicar estos conocimientos en ejemplos prácticos
""")

st.header("Solución")
st.title("Actividad 1 - Practica de filtrado en Pandas (Google Colab)")
st.markdown('<p>Actividad 1: <a href="https://colab.research.google.com/drive/1GPy1pR8pu5E7Wr3ZmmoZ4mcI782nGLKk?usp=sharing" target="_blank" style="color: #0066cc; font-weight: bold; text-decoration: none;">GoogleColab</a></p>', unsafe_allow_html=True)



# 📌_M2_Actividad_3.py

import streamlit as st
import pandas as pd
import numpy as np
import random
from faker import Faker
import datetime

# Configurar Faker para Colombia
fake = Faker('es_CO')

# Establecer semillas
np.random.seed(123)
random.seed(123)
fake.seed_instance(123)

# Crear datos
n = 50
data = {
    'id': range(1, n + 1),
    'nombre_completo': [fake.name() for _ in range(n)],
    'edad': np.random.randint(15, 76, n),
    'region': random.choices(
        ['Caribe', 'Andina', 'Pacífica', 'Orinoquía', 'Amazonía'],
        weights=[0.3, 0.4, 0.15, 0.1, 0.05],
        k=n
    ),
    'municipio': random.choices(
        [
            'Barranquilla', 'Santa Marta', 'Cartagena',
            'Bogotá', 'Medellín', 'Tunja', 'Manizales',
            'Cali', 'Quibdó', 'Buenaventura',
            'Villavicencio', 'Yopal',
            'Leticia', 'Puerto Inírida'
        ],
        k=n
    ),
    'ingreso_mensual': np.random.randint(800000, 12000001, n),
    'ocupacion': random.choices(
        [
            'Estudiante', 'Docente', 'Comerciante', 'Agricultor',
            'Ingeniero', 'Médico', 'Desempleado', 'Pensionado',
            'Emprendedor', 'Obrero'
        ],
        k=n
    ),
    'tipo_vivienda': random.choices(['Propia', 'Arrendada', 'Familiar'], k=n),
    'fecha_nacimiento': [
        fake.date_of_birth(minimum_age=15, maximum_age=75) for _ in range(n)
    ],
    'acceso_internet': random.choices([True, False], weights=[0.7, 0.3], k=n)
}

# Crear DataFrame
df_nuevo = pd.DataFrame(data)

# Introducir algunos valores nulos
df_nuevo.loc[3:5, 'ingreso_mensual'] = np.nan
df_nuevo.loc[15:17, 'ocupacion'] = np.nan

# Asegurar que fecha_nacimiento es datetime
df_nuevo['fecha_nacimiento'] = pd.to_datetime(df_nuevo['fecha_nacimiento'])

# Título
st.title("Atividad 2 - Aplicación de Filtros Dinámicos - Streamlit")

# Sidebar
st.sidebar.header("Configuración de Filtros")

# Inicializar el DataFrame filtrado
df_filtrado = df_nuevo.copy()

# 1. Filtro por rango de edad
if st.sidebar.checkbox("Filtrar por rango de edad"):
    min_edad, max_edad = st.sidebar.slider(
        "Selecciona el rango de edad:",
        15, 75, (20, 40)
    )
    df_filtrado = df_filtrado[df_filtrado['edad'].between(min_edad, max_edad)]

# 2. Filtro por municipios específicos
if st.sidebar.checkbox("Filtrar por municipios"):
    municipios = [
        'Barranquilla', 'Santa Marta', 'Cartagena',
        'Bogotá', 'Medellín', 'Tunja', 'Manizales',
        'Cali', 'Quibdó', 'Buenaventura',
        'Villavicencio', 'Yopal',
        'Leticia', 'Puerto Inírida'
    ]
    municipios_seleccionados = st.sidebar.multiselect("Selecciona municipios:", municipios)
    if municipios_seleccionados:
        df_filtrado = df_filtrado[df_filtrado['municipio'].isin(municipios_seleccionados)]

# 3. Filtro por ingreso mensual mínimo
if st.sidebar.checkbox("Filtrar por ingreso mensual mínimo"):
    ingreso_minimo = st.sidebar.slider(
        "Selecciona ingreso mínimo (COP):",
        800000, 12000000, 2000000, step=50000
    )
    df_filtrado = df_filtrado[df_filtrado['ingreso_mensual'] > ingreso_minimo]

# 4. Filtro por ocupación
if st.sidebar.checkbox("Filtrar por ocupación"):
    ocupaciones = [
        'Estudiante', 'Docente', 'Comerciante', 'Agricultor',
        'Ingeniero', 'Médico', 'Desempleado', 'Pensionado',
        'Emprendedor', 'Obrero'
    ]
    ocupaciones_seleccionadas = st.sidebar.multiselect("Selecciona ocupaciones:", ocupaciones)
    if ocupaciones_seleccionadas:
        df_filtrado = df_filtrado[df_filtrado['ocupacion'].isin(ocupaciones_seleccionadas)]

# 5. Filtro por tipo de vivienda no propia
if st.sidebar.checkbox("Filtrar personas sin vivienda propia"):
    df_filtrado = df_filtrado[~(df_filtrado['tipo_vivienda'] == 'Propia')]

# 6. Filtro por nombres que contienen una cadena
if st.sidebar.checkbox("Filtrar por nombre"):
    texto = st.sidebar.text_input("Contiene en el nombre:", value="")
    if texto:
        df_filtrado = df_filtrado[df_filtrado['nombre_completo'].str.contains(texto, case=False, na=False)]

# 7. Filtro por año de nacimiento específico
if st.sidebar.checkbox("Filtrar por año de nacimiento"):
    anios = list(range(1949, 2010))
    anio_seleccionado = st.sidebar.selectbox("Selecciona año:", anios)
    df_filtrado = df_filtrado[df_filtrado['fecha_nacimiento'].dt.year == anio_seleccionado]

# 8. Filtro por acceso a internet
if st.sidebar.checkbox("Filtrar por acceso a internet"):
    acceso = st.sidebar.radio("¿Tiene acceso a internet?", ["Sí", "No"])
    if acceso == "Sí":
        df_filtrado = df_filtrado[df_filtrado['acceso_internet'] == True]
    else:
        df_filtrado = df_filtrado[df_filtrado['acceso_internet'] == False]

# 9. Filtro por ingresos nulos
if st.sidebar.checkbox("Filtrar por ingresos nulos"):
    df_filtrado = df_filtrado[df_filtrado['ingreso_mensual'].isnull()]

# 10. Filtro por rango de fechas de nacimiento
if st.sidebar.checkbox("Filtrar por rango de fechas de nacimiento"):
    fecha_inicio = st.sidebar.date_input("Fecha inicial:", datetime.date(1949, 1, 1))
    fecha_fin = st.sidebar.date_input("Fecha final:", datetime.date(2009, 12, 31))
    if fecha_inicio <= fecha_fin:
        df_filtrado = df_filtrado[df_filtrado['fecha_nacimiento'].between(fecha_inicio, fecha_fin)]

# Mostrar resultados
st.subheader("🔍 Resultado del filtrado:")
st.dataframe(df_filtrado)

# Mostrar cantidad de resultados
st.write(f"Se encontraron **{df_filtrado.shape[0]}** registros.")
