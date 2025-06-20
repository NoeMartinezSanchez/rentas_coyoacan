import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(page_title="Análisis de Renta en Coyoacán", layout="centered")
st.title("📊 Análisis de Renta de Departamentos en Coyoacán")

# Cargar archivo Excel
uploaded_file = st.file_uploader("Sube tu archivo Excel (xlsx)", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file, engine="openpyxl")
    
    # Mostrar datos
    st.subheader("Datos de Renta")
    st.dataframe(df.head())
    
    # Resumen estadístico
    st.subheader("📌 Resumen Estadístico")
    st.write(df.describe())
    
    # Gráfico de precios
    st.subheader("📈 Precios de Renta por Colonia")
    fig, ax = plt.subplots(figsize=(10, 5))
    df.groupby("Colonia")["Precio_Renta"].mean().sort_values().plot(
        kind="bar", 
        color="skyblue",
        ax=ax
    )
    ax.set_ylabel("Precio Promedio (MXN)")
    ax.set_title("Precio Promedio de Renta por Colonia")
    st.pyplot(fig)
    
    # Filtros interactivos
    st.subheader("🔍 Filtrar Datos")
    colonia = st.selectbox("Selecciona una colonia:", df["Colonia"].unique())
    filtered_df = df[df["Colonia"] == colonia]
    st.write(filtered_df)

else:
    st.warning("Por favor, sube un archivo Excel para analizar.")