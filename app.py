import streamlit as st
import pandas as pd 
import plotly_express as px 

# Título de la aplicación
st.title('Análisis de Vehículos Usados en EE.UU.')

# Cargar los datos
@st.cache_data
def load_data():
    data = pd.read_csv('vehicles_us.csv')
    data['date_posted'] = pd.to_datetime(data['date_posted'])
    data['model_year'] = data['model_year'].fillna(data['model_year'].median())
    data['cylinders'] = data['cylinders'].fillna(data['cylinders'].median())
    data['odometer'] = data['odometer'].fillna(data['odometer'].median())
    data['paint_color'] = data['paint_color'].fillna('unknown')
    data['is_4wd'] = data['is_4wd'].fillna(0)
    data.drop_duplicates(inplace=True)
    return data

vehicles_df = load_data()

# Encabezado
st.header('Distribución de Precios y Condiciones de Vehículos')

# Botón para histograma
if st.button('Mostrar Histograma de Precios'):
    fig_price = px.histogram(vehicles_df, x='price', nbins=50, title='Distribución de Precios de Vehículos')
    st.plotly_chart(fig_price)

# Botón para gráfico de dispersión
if st.button('Mostrar Gráfico de Dispersión de Precios vs. Año del Modelo'):
    fig_scatter = px.scatter(vehicles_df, x='model_year', y='price', title='Precios vs. Año del Modelo')
    st.plotly_chart(fig_scatter)

# Casillas de verificación (opcional)
if st.checkbox('Mostrar Histograma de Precios'):
    fig_price = px.histogram(vehicles_df, x='price', nbins=50, title='Distribución de Precios de Vehículos')
    st.plotly_chart(fig_price)

if st.checkbox('Mostrar Gráfico de Dispersión de Precios vs. Año del Modelo'):
    fig_scatter = px.scatter(vehicles_df, x='model_year', y='price', title='Precios vs. Año del Modelo')
    st.plotly_chart(fig_scatter)
