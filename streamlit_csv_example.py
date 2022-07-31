import streamlit as st
import pandas as pd


@st.cache
def get_data():
    return pd.read_csv('https://datahub.io/core/gdp/r/gdp.csv')


'# World GDP'

df = get_data()

min_year = int(df['Year'].min())
max_year = int(df['Year'].max())

countries = df['Country Name'].unique()

'## By country'
country = st.selectbox('Country', countries)
df[df['Country Name'] == country]


'## By year'
year = st.slider('Year', min_year, max_year)
df[df['Year'] == year]