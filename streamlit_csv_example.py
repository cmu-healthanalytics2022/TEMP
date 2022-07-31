import streamlit as st
import pandas as pd


@st.cache
def get_data():
    return pd.read_csv('https://raw.githubusercontent.com/cmu-healthanalytics2022/TEMP/main/Medicare_DUALS_SJTB_COVID_v1.csv')


'# Medicare Dual Benes in St John The Baptist Parish'

df = get_data()

min_LOS = int(df['Length of Stay'].min())
max_LOS = int(df['Length of Stay'].max())

diagnosis = df['CCS Diagnosis Description'].unique()

'## By Diagnosis'
diagn = st.selectbox('Diagn', diagnosis)
df[df['CCS Diagnosis Description'] == diagn]


'## By LOS'
LOS = st.slider('Length of Stay', min_LOS, max_LOS)
df[df['Length of Stay'] == LOS]