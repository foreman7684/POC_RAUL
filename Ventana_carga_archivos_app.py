import streamlit as st
from snowflake.snowpark.functions import col

# Título de la aplicación
st.title('Subida de Archivos a Snowflake')

cnx = st.connection("snowflake")
session = cnx.session()

# Crear un selector de archivos
uploaded_file = st.file_uploader("Elige un archivo")

if uploaded_file is not None:
    file_name = {
        "FileName":uploaded_file.name
    }
    my_insert_stmt = """ insert into POC_RAUL.public.REPOSITORIO_ARCHIVOS_INTERNET(NOMBRE_ARCHIVO)
    values ('""" +file_name+"""')"""
    # Aquí puedes procesar tu archivo como necesites
    # Por ejemplo, mostrar un mensaje de confirmación
    st.success('Archivo cargado con éxito!')
