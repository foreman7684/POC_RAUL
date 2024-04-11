import streamlit as st
from snowflake.snowpark.functions import col
from base64 import b64encode

# Título de la aplicación
st.title('Subida de Archivos a Snowflake')

cnx = st.connection("snowflake")
session = cnx.session()

# Crear un selector de archivos
uploaded_file = st.file_uploader("Elige un archivo")

if uploaded_file is not None:
    file_name = uploaded_file.name
    file_type = uploaded_file.type
    file_value = b64encode(uploaded_file.getvalue()).decode('utf-8')
    my_insert_stmt = """ insert into POC_RAUL.public.REPOSITORIO_ARCHIVOS_INTERNET(NOMBRE_ARCHIVO,EXTENSION,ARCHIVO)
    values ('""" + file_name + """','""" +file_type+"""','""" +file_value+"""')"""
    session.sql(my_insert_stmt).collect()
    # Aquí puedes procesar tu archivo como necesites
    # Por ejemplo, mostrar un mensaje de confirmación
    st.success('Archivo cargado con éxito!')
