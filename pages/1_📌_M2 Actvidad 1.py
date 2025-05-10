import streamlit as st
import pandas as pd
import csv 
import sqlite3
import numpy as np



# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 1")

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

# Mostrar título en la aplicación
st.title("Nuevas Tecnologias"
" Actividad 1 - Creación de DataFrames")

# Agregar una descripción debajo del título
st.write("En esta actividad, aprenderemos a crear y manipular DataFrames usando la librerías")

libros = {
    "título": ["El señor de los anillos", "Matar a un ruiseñor", "El principito", "Don Quijote de la Mancha"],
    "autor": ["J.R.R. Tolkie", "Harper Lee", "Antoine de Saint-Exupéry", "Miguel de Cervantes"],
    "año de publicación": [1954, 1960, 1943, 1605],
    "género": ["Fantasía épica", "Ficción literaria", "Fábula", "Novela clásica"]
}

df_libros = pd.DataFrame(libros)

st.write("### DataFrame de Libros")
st.dataframe(df_libros)




st.title(" Creación de DataFrames con Lista de Diccionarios")
st.write("En esta actividad, trabajaremos con una lista de diccionarios para representar información sobre ciudades.")

ciudades = [
    {"nombre": "Medellin", "población": 22634570, "país": "Colombia"},
    {"nombre": "Ciudad de Mexico", "población": 929944, "país": "Mexico"},
    {"nombre": "París", "población": 2148000, "país": "Francia"},
    {"nombre": "Buenos Aires", "población": 2890151, "país": "Argentina"}
]

df_ciudades = pd.DataFrame(ciudades)

st.write("### Información de Ciudades")
st.dataframe(df_ciudades)




st.title("Creación de DataFrames con Lista de Listas")
st.write("En esta actividad, representaremos información de productos en inventario usando una lista de listas.")

productos = [
    ["smartwatch", 1200, 15],
    ["Smartphone", 800, 30],
    ["Tv", 500, 25],
    ["Tablet", 150, 50]
]

df_productos = pd.DataFrame(productos, columns=["Nombre", "Precio", "Cantidad en Stock"])

st.write("### Productos en Inventario")
st.dataframe(df_productos)




st.title("Creación de DataFrames con Series")
st.write("En esta actividad, combinaremos Series de Pandas para formar un DataFrame con información de personas.")

nombres = pd.Series(["Ana", "Carlos", "Beatriz", "David"])
edades = pd.Series([28, 35, 22, 40])
ciudades = pd.Series(["Madrid", "Buenos Aires", "Ciudad de México", "Santiago"])

datos_personas = {
    "Nombre": nombres,
    "Edad": edades,
    "Ciudad": ciudades
}

df_personas = pd.DataFrame(datos_personas)

st.write("### Datos de Personas")
st.dataframe(df_personas)




st.title("Carga de Datos desde un CSV")
st.write("En esta actividad, leeremos un archivo CSV y mostraremos su contenido en un DataFrame.")

# Define los nombres de las columnas
column_names = ["Nombre", "Edad", "Ciudad"]

data = [
    ["Ana", 25, "Madrid"],
    ["Juan", 30, "Barcelona"],
    ["Pedro", 35, "Sevilla"]
]

# Crear el archivo CSV
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(column_names)  # Escribir encabezados
    writer.writerows(data)  # Escribir datos

st.write("### Datos desde CSV")

# Leer el CSV y mostrarlo con Streamlit
df = pd.read_csv("data.csv")
st.dataframe(df)




st.title("Carga de Datos desde un Archivo Excel")
st.write("En esta actividad, leeremos un archivo Excel y mostraremos su contenido en un DataFrame.")

# Datos de ejemplo
data = {
    "producto": ["Laptop", "Mouse", "Teclado"],
    "precio": [1200, 25, 45],
    "stock": [10, 50, 30]
}

# Crear el DataFrame
df = pd.DataFrame(data)

# Guardar en un archivo Excel
df.to_excel("static\data.xlsx", index=False, engine="openpyxl")


# Leer el archivo Excel 
df_excel = pd.read_excel("static\data.xlsx", engine="openpyxl")

st.write("### Datos desde Excel")
st.dataframe(df_excel)




st.title("Actividad - Carga de Datos desde JSON")
st.write("En esta actividad, leeremos un archivo JSON y mostraremos su contenido en un DataFrame.")

# Leer el archivo JSON y convertirlo en DataFrame
df_json = pd.read_json("data.json")

st.write("### Datos de Usuarios desde JSON")
st.dataframe(df_json)





st.title("Actividad - Carga de Datos desde una URL")
st.write("En esta actividad, leeremos un archivo CSV directamente desde una URL y lo mostraremos en un DataFrame.")

# URL del archivo CSV
csv_url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"

# Leer el CSV desde la URL
df_url = pd.read_csv(csv_url)

st.write("### Datos desde URL")
st.dataframe(df_url)




st.title("Actividad - Carga de Datos desde SQLite")
st.write("En esta actividad, crearemos una base de datos SQLite, insertaremos datos y los mostraremos en un DataFrame.")

# Conectar a la base de datos (se crea si no existe)
conn = sqlite3.connect("estudiantes.db")
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute("""
    CREATE TABLE IF NOT EXISTS estudiantes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        calificacion REAL
    )
""")
conn.commit()

# Insertar datos si la tabla está vacía
cursor.execute("SELECT COUNT(*) FROM estudiantes")
if cursor.fetchone()[0] == 0:
    cursor.executemany("INSERT INTO estudiantes (nombre, calificacion) VALUES (?, ?)", [
        ("Ana", 85.5),
        ("Juan", 90.0),
        ("Pedro", 78.2)
    ])
    conn.commit()

# Leer los datos en un DataFrame
df_sqlite = pd.read_sql("SELECT * FROM estudiantes", conn)

st.write("### Datos desde SQLite")
st.dataframe(df_sqlite)

# Cerrar conexión
conn.close()





st.title("Actividad - Carga de Datos desde NumPy")
st.write("En esta actividad, crearemos un array de NumPy, lo convertiremos en un DataFrame y lo mostraremos en Streamlit.")

# Crear un array bidimensional de 3x3 con datos numéricos
array_numpy = np.array([
    [1, 2.5, 100],
    [2, 3.8, 200],
    [3, 5.1, 300]
])

# Convertir el array en un DataFrame
df_numpy = pd.DataFrame(array_numpy, columns=["ID", "Valor", "Cantidad"])

st.write("### Datos desde NumPy")
st.dataframe(df_numpy)




