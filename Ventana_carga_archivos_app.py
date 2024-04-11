import streamlit as st

# Título de la aplicación
st.title('Subida de Archivos a Snowflake')

# Crear un selector de archivos
uploaded_file = st.file_uploader("Elige un archivo")

if uploaded_file is not None:
    # Aquí puedes procesar tu archivo como necesites
    # Por ejemplo, mostrar un mensaje de confirmación
    st.success('Archivo cargado con éxito!')

    # Opcional: Muestra información sobre el archivo cargado
    file_details = {
        "FileName": uploaded_file.name,
        "FileType": uploaded_file.type,
        "FileSize": uploaded_file.size
    }
