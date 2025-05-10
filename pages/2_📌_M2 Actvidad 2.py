import streamlit as st
import pandas as pd
import io

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 2")

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

df = pd.read_csv('datasets/estudiantes_colombia.csv')


st.dataframe(df)


st.title("Ver las primeras 5 filas")
st.write (df.head(5))


st.title("Ver las ultimas 5 filas")
st.write(df.tail(5))



st.subheader("Ver Informacion (Resumen tecnico)")
info_df = pd.DataFrame({
    "Columna": df.columns,
    "Tipo de dato": df.dtypes.values,
    "Valores nulos": df.isnull().sum().values,
    "Valores únicos": df.nunique().values
})
st.dataframe(info_df)



st.title("Estadísticas descriptivas de columnas numéricas")
st.write(df.describe())


st.title("Seleccion columnas especificas")
st.write (df [["nombre", "edad", "promedio"]])


st.title("Filtrar estudiantes por promedio")

st.header("Filtrar por Promedio")
promedio_min = st.slider(
    "Selecciona el promedio mínimo:",
    min_value=float(df["promedio"].min()),
    max_value=float(df["promedio"].max()),
    value=4.0,
    step=0.1
)

df_filtrado = df[df["promedio"] >= promedio_min]
st.write(f"Estudiantes con promedio mayor o igual a {promedio_min}: {len(df_filtrado)}")
st.dataframe(df_filtrado)