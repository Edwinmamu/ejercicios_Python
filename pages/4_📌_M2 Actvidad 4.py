import streamlit as st

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 4")

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

import streamlit as st
import pandas as pd

# Datos de ejemplo
data = {
    'Deporte': ['Fútbol', 'Baloncesto', 'Béisbol', 'Tenis', 'Fútbol', 'Baloncesto', 'Tenis', 'Béisbol'],
    'País': ['Brasil', 'EE.UU.', 'EE.UU.', 'España', 'Argentina', 'España', 'Suiza', 'Japón'],
    'Popularidad': [95, 90, 85, 80, 92, 89, 75, 83],
    'Jugadores Famosos': ['Pelé', 'Michael Jordan', 'Babe Ruth', 'Rafael Nadal', 'Messi', 'Pau Gasol', 'Federer', 'Ohtani']
}

df = pd.DataFrame(data)

st.title("🏟️ Explorador de Deportes Populares")

st.subheader("📊 DataFrame original")
st.dataframe(df)

# Selección por índice con .iloc
st.subheader("🔍 Selección por índice (.iloc)")
start_row = st.number_input("Fila de inicio (iloc):", min_value=0, max_value=len(df)-1, value=0)
end_row = st.number_input("Fila final (iloc):", min_value=1, max_value=len(df), value=3)
st.write("Filas seleccionadas:")
st.dataframe(df.iloc[start_row:end_row])

# Selección por etiqueta con .loc
st.subheader("🔍 Filtro por condiciones (.loc)")
min_pop = st.slider("Popularidad mínima:", 0, 100, 80)
selected_sport = st.selectbox("Selecciona un deporte:", ['Todos'] + list(df['Deporte'].unique()))

filtered_df = df.loc[df['Popularidad'] >= min_pop]
if selected_sport != 'Todos':
    filtered_df = filtered_df.loc[filtered_df['Deporte'] == selected_sport]

st.write("Filtrado por popularidad y deporte:")
st.dataframe(filtered_df)

# Modificación de datos con .loc
st.subheader("✏️ Modificar datos con .loc")
row_to_edit = st.number_input("Índice de fila a modificar:", 0, len(df) - 1, 0)
new_popularity = st.slider("Nueva popularidad:", 0, 100, int(df.loc[row_to_edit, 'Popularidad']))
if st.button("Actualizar popularidad"):
    df.loc[row_to_edit, 'Popularidad'] = new_popularity
    st.success(f"Popularidad actualizada para la fila {row_to_edit} ✅")
    st.dataframe(df)

# Mostrar tabla final
st.subheader("📦 DataFrame actualizado")
st.dataframe(df)


