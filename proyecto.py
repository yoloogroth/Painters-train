import pandas as pd
import streamlit as st
import re
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="painters train", page_icon=":sun:")
st.markdown("<h1 style='text-align: center; color: purple;'>PAINTERS TRAIN</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: Cyan;'>YOLOTZIN GROTH HERNANDEZ</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: LightGreen;'>zs20020311</h3>", unsafe_allow_html=True)

DATA_URL = 'https://raw.githubusercontent.com/yoloogroth/Painters-train/master/all_data_info.csv '

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows, encoding_errors='ignore')
    return data

@st.cache
def load_data_name(name):
    datafiltered = load_data(10000)
    filtrar_data_nombre = datafiltered[datafiltered['genre']==name]  
    return filtrar_data_nombre

@st.cache
def load_data_artist(artist):
    data = load_data(10000)
    filtrar_data_artista = data[data['artist'].str.match( artist, case=False)]
    return filtrar_data_artista


st.sidebar.image('https://raw.githubusercontent.com/yoloogroth/Painters-train/master/WhatsApp%20Image%202023-03-14%20at%208.52.39%20AM.jpeg ')

sidebar = st.sidebar
agree = sidebar.checkbox("Mostrar todas las pinturas")
titulo = sidebar.text_input('buscar por nombre de artista:')
btnFiltrarArtist = sidebar.button('Buscar')
data = load_data(10000)
selected = sidebar.selectbox("Seleccionar por genero", data['genre'].unique())
btnFiltrarGenero = sidebar.button('Filtrar por genero')


if agree:
    estado = st.text('Cargando...')
    data = load_data(10000)
    estado.text("¡Cargando pinturas! ")
    st.dataframe(data)

if btnFiltrarArtist:
    st.write ("busqueda: "+ titulo)
    filtrar = load_data_artist(titulo)
    filas = filtrar.shape[0]
    st.write(f'Total de pinturas del artista: {filas}')
    st.dataframe(filtrar)

if btnFiltrarGenero: 
    st.write("generos "+selected)
    filtrar = load_data_name(selected)
    filas = filtrar.shape[0]
    st.write(f'Total de pinturas: {filas}')
    st.dataframe(filtrar)

#histograma de painters
st.sidebar.title("Graficas:")
agree = st.sidebar.checkbox("Histograma")
if agree:
  fig_genre=px.bar(data,
                    x=data['artist'],
                    y=data['title'],
                    orientation="v",
                    title="Painters by artist",
                    labels=dict(y="", x=""),
                    color_discrete_sequence=["cyan"],
                    template="plotly_white")
  st.plotly_chart(fig_genre)

#diagrama de barras
if st.sidebar.checkbox('Grafica de barras'):
    st.subheader('grafica de barras ')

    fig, ax = plt.subplots()

    y_pos = data['pixelsx']
    x_pos = data['pixelsy']

    ax.barh(x_pos, y_pos,color = "Cyan")
    ax.set_ylabel("Artist")
    ax.set_xlabel("Pixel per paint")
    ax.set_title('grafica de barras')
    st.header('grafica de barras pixel for paint')
    st.pyplot(fig)

    st.markdown("___")

#diagrama de scatter
if st.sidebar.checkbox('scatter de las pinturas'):
    st.subheader('scatter de paints')
    imprint=data['pixelsx']
    years=data['pixelsy']
    rating=data['date']
    fig_age=px.scatter(data,
                   x=imprint,
                   y=rating,
                   color=years, 
                   title="Pixeles por siglo en el que nacio el artista",
                   labels=dict(Imprenta="imprint", years="years", print="Print"),
                   template="plotly_white")
    st.plotly_chart(fig_age)

