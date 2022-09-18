# %%
import pandas as pd
import streamlit as st
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
      
# ----------- Global Sidebar ---------------

condition = st.sidebar.selectbox(
    "Select the visualization",
    ("INTRO", "GEO")
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
