

# Streamlit se ejecuta siempre desde scripts (.py) y desde el cmd en la carpeta donde está el .py y con el conda activate eda_env ejecutado antes
# pip install streamlit en la terminal
# Para lanzar la web ejecutar el comando: "streamlit run st_app.py". Después se actualiza en la web en un botón cada vez que guardamos el .py

import streamlit as st
import pandas as pd

# streamlit docs

import streamlit as st

st.set_page_config(
    page_title="Streamlit de APintos2",
    page_icon=":cat:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.header("MY ST APP")
st.sidebar.text("Menu")

# menu = st.sidebar.selectbox(
#     "Seleccione una opcion del menu",
#     ('Home', 'Data', "Viz")
# )

home = st.sidebar.button("Home")
data = st.sidebar.button("Data")
viz = st.sidebar.button("Viz")


df = pd.read_csv("https://raw.githubusercontent.com/JLGOrtega/datasets/master/BostonHousing.csv")


if data:
    st.header("Data")
    st.text("A continuación mostramos data:")
    st.dataframe(df) # La carga del df arriba del botón porque cada vez que pulsas un botón se ejecuta todo lo de dentro de él


elif viz:
    st.header("Viz")

    col1, col2 = st.columns(2)
    
    with col1:
        st.scatter_chart(data=df, x="rm", y="age", color="rad", size="medv")

    with col2:
        st.line_chart(data=df, x="lstat", y="age")

    col3, col4 = st.columns(2)

    with col3:
        st.bar_chart(data=df, x="lstat", y="age")

    with col4:
        st.map(data=df, latitude="rm", longitude="age")

# tb se pueden usar plotly (st.plotly_chart), matplotlib (st.pyplot), etc.

else:
    st.header("Welcome page")
    with st.expander("Ver más"):
        st.text("Bienvenid@s a nuestra Streamlit App!")
    image_url = "https://upload.wikimedia.org/wikipedia/commons/8/8c/British_Shorthair_cat._Female._18_months_old.jpg"
    st.image(image_url)

