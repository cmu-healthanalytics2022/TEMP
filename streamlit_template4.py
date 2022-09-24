# %%
import pandas as pd
import streamlit as st
import graphs
import eda
import matplotlib.pyplot as plt
import os


import requests
# Save datagenerators as file to colab working directory
# If you are using GitHub, make sure you get the "Raw" version of the code
url = 'https://raw.githubusercontent.com/cmu-healthanalytics2022/TEMP/main/graphs.py'
r = requests.get(url)
# make sure your filename is the same as how you want to import 
with open('graphs.py', 'w') as f:
    f.write(r.text)
# now we can import
import graphs
url2 = 'https://raw.githubusercontent.com/cmu-healthanalytics2022/TEMP/main/eda.py'
r2 = requests.get(url2)
# make sure your filename is the same as how you want to import 
with open('eda.py', 'w') as f2:
    f2.write(r2.text)
# now we can import
import eda
#import seaborn as sns
# %%
st.set_page_config(
    page_title="Predicting Medicare Costs with the SAS AI Workbench",
    page_icon="SAS_LOGO4.jpeg",
    layout="wide",
    initial_sidebar_state="expanded",
)
"""
# Monitoring and Surveillance Solution: Predicting Medicare Costs
[![Follow](https://img.shields.io/badge/Connect-follow?style=social&logo=github)](https://github.com/ManuelFigallo/)
[![Follow](https://img.shields.io/badge/Connect-follow?style=social&logo=linkedin)](https://www.linkedin.com/in/mfigallo/)
"""

# ----------- Data -------------------

@st.cache  
def loadX3Data():
	dfx3 = pd.read_csv(os.path.join(os.path.abspath(''), 'data', 'X3.csv'))
	return dfx3

@st.cache
def get_data():
    return pd.read_csv('https://raw.githubusercontent.com/cmu-healthanalytics2022/TEMP/main/Medicare_DUALS_SJTB_COVID_v1.csv')


@st.cache
def get_raw_data():
    """
    This function return a pandas DataFrame with the raw data.
    """

    raw_df = pd.read_csv('https://raw.githubusercontent.com/cmu-healthanalytics2022/TEMP/main/Medicare_DUALS_SJTB_COVID_v1.csv')
    return raw_df

@st.cache
def get_raw_data2():
    """
    This function return a pandas DataFrame with the raw data.
    """

    raw_df = pd.read_csv('https://raw.githubusercontent.com/cmu-healthanalytics2022/TEMP/main/Medicare_DUALS_SJTB_COVID_v1.csv')
    return raw_df

@st.cache
def get_cleaned_data():
    """
    This function return a pandas DataFrame with the cleaned data.
    """

    clean_data = pd.read_csv('https://raw.githubusercontent.com/cmu-healthanalytics2022/TEMP/main/Medicare_DUALS_SJTB_COVID_v1.csv')
    #clean_data = pd.read_csv(os.path.join(os.path.abspath(''), 'data', 'houses_to_rent_v2_fteng_v2.csv'))
    return clean_data

@st.cache
def get_cleaned_data1():
    """
    This function return a pandas DataFrame with the cleaned data.
    """

    clean_data1 = pd.read_csv('https://raw.githubusercontent.com/cmu-healthanalytics2022/TEMP/main/Medicare_DUALS_SJTB_COVID_v1.csv')
    return clean_data1

@st.cache
def get_cleaned_data2():
    """
    This function return a pandas DataFrame with the cleaned data.
    """

    #clean_data = pd.read_csv(os.path.join(os.path.abspath(''), 'data', 'houses_to_rent_v2_fteng.csv'))
    clean_data1 = pd.read_csv('https://raw.githubusercontent.com/cmu-healthanalytics2022/TEMP/main/Medicare_DUALS_SJTB_COVID_v1.csv')
    return clean_data1

# ----------- Global VARS ---------------

#raw_df = get_raw_data()
raw_df = get_raw_data2()
clean_df = get_cleaned_data()
#clean_df1 = get_cleaned_data1()
clean_df1 = get_cleaned_data2()

# ----------- Global Sidebar ---------------

condition = st.sidebar.selectbox(
    "Select the visualization",
    ("INTRO", "GEO", "TABLE1", "EDA")
)

# ------------- Introduction ------------------------

if condition == 'INTRO':
    #st.image(os.path.join(os.path.abspath(''), 'data', 'dataset-cover.jpg'))
    #st.image('data/dataset-cover4.jpg')
    st.subheader('Introduction for Streamlit')    
    ## Notes for GITHUB
    st.write("""
    This introduction page can be modified in many ways.
    """)
    
# ------------- Descriptive Hypothesis ------------------------

elif condition == 'GEO':
    st.subheader('Geographic Analysis Visualizations in Streamlit')
    ## FALTA O CHECK ON GITHUB
    st.write("""
    This page contains sample visualizations. You can also visualize your cluster in a geographic map.
    """)
    import streamlit as st
    import folium
    from folium import plugins
    from folium.plugins import HeatMap
    import pandas as pd
    import streamlit.components.v1 as components
    import numpy as np
    from glob import glob
    import numpy as np
    import folium
    from folium import plugins
    from folium.plugins import HeatMap
    lon, lat = 30.0913075, -90.7642336
    zoom_start = 5
    #https://raw.githubusercontent.com/cmu-healthanalytics2022/TEMP/main/df_ca_map_test1_BKP1.csv
    data0 = pd.read_csv('https://raw.githubusercontent.com/cmu-healthanalytics2022/TEMP/main/df_ca_map_test1_BKP1.csv')
    #data0 = pd.read_csv('D:\Python\Projects\snippets\Cloud_Data_Processing\df_ca_map_test1_BKP1.csv')
    data0['Speed_limit'] = data0['Speed_limit'].astype(str)
    data0['Year'] = data0['Year'].astype(str)
    # Ensure you're handing it floats
    data0['Latitude'] = data0['Latitude'].astype(float)
    data0['Longitude'] = data0['Longitude'].astype(float)
    # Filter the DF for rows, then columns, then remove NaNs
    data = data0[data0['Speed_limit']=='40'] # Reducing data size so it runs faster
    data = data0[data0['Year']=='2007'] # Reducing data size so it runs faster
    data = data[['Latitude', 'Longitude']]
    # Create weight column, using date
    data['Weight'] = data0['Date'].str[3:5]
    data['Weight'] = data['Weight'].astype(float)
    data = data.dropna(axis=0, subset=['Latitude','Longitude', 'Weight'])
    m = folium.Map([30.0913075, -90.7642336], tiles='cartodbpositron', zoom_start=9)
    HeatMap(data).add_to(m)
    m    
    #st.title("END VIZ - CANCER ALLEY 555")

# ------------- Descriptive Hypothesis ------------------------

elif condition == 'TABLE1':
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

# ------------- EDA ------------------------

elif condition == 'EDA':

    st.header('EDA')
    st.markdown('EDA is "Exploratory Data Analysis" for Medicare costs data.')

    'EDA VIZ for # Medicare Dual Benes in St John The Baptist Parish'

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

    type_of_data = st.radio(
        "Type of Data",
        ('Cleaned Data', 'Raw Data'),
        help='Data source that will be displayed in the charts'
    )

    if type_of_data == 'Raw Data':
        data = raw_df.copy()
    else:
        data = clean_df1.copy()

#    with st.beta_container():
    with st.container():
        st.header('Descriptive Statistics\n')
        #col1, col2 = st.beta_columns([1, 3])
        col1, col2 = st.columns([1, 3])
        col1.dataframe(eda.summary_table(data))
        col2.dataframe(data.describe())

    st.header('Data Visualization')

    height, width, margin = 450, 1500, 10

    st.subheader('Medicare Utilization Distribution')

    select_city_eda = st.selectbox(
        'Select the County/Parish/Facility Name',
        ['All'] + [i for i in data['Facility Name'].unique()]
    )

    if select_city_eda == 'All':
        fig = graphs.plot_histogram(data=data, x="Length of Stay", nbins=50, height=height, width=width, margin=margin)
    else:
        fig = graphs.plot_histogram(
            data = data.loc[data['Facility Name'] == select_city_eda], x="Length of Stay", nbins=50, height=height, width=width, margin=margin)
                      
    st.plotly_chart(fig)

    st.subheader('Scatterplot')

    select_numerical = st.selectbox(
        'Select the Numerical Variable',
        ['Length of Stay', 'CARES Funding (in $) per beds', 'Total Hospital Revenue ($)', 'Medicare Allowed Amount ($)']
    )

    fig = graphs.plot_scatter(data=data, x=select_numerical, y="Length of Stay", height=height, width=width, margin=margin)

    st.plotly_chart(fig)

    st.subheader('Categorical Graphs')

    select_graph = st.radio(
        'Select the Type of Graph',
        ('Boxplot', 'Countplot')
    )

    #select_variable = st.selectbox(
    #    'Select the Variable',
    #    [i for i in data.columns if data[i].dtype == object and i != ('city', 'floor')]
    #)
    select_variable = st.selectbox(
        'Select the Variable',
        ('Gender', 'Race', 'Facility Name'),
    )

    if select_graph == 'Boxplot':
        fig = graphs.plot_boxplot(data=data, x=select_variable, y="Length of Stay", color=select_variable, height=height, width=width, margin=margin)
    elif select_graph == 'Countplot':
        fig = graphs.plot_countplot(data=data, x=select_variable, height=height, width=width, margin=margin)

    st.plotly_chart(fig)

    st.subheader('Length of Stay per Variable')

    option = st.selectbox(
        'Select the Column',
        ('Total Charges', 'Total Costs', 'Percent Black at the facility'),
    )

    fig = graphs.plot_bar(data=data.groupby(option).mean().reset_index(), x=option, y='Length of Stay', height=height, width=width, margin=margin)

    st.plotly_chart(fig)

    st.subheader('Correlation Matrix')
    data2=data[['Length of Stay',
                'APR Severity of Illness Code',
                'Total Charges',
                'Total Costs']]
    
    corr_matrix = data2.corr()

    fig = graphs.plot_heatmap(corr_matrix=corr_matrix, height=height, margin=margin)

    st.plotly_chart(fig)