#Imports
import numpy as np
import os
import pandas as pd
import plotly.express as px
import streamlit as st
import math
import json

#Set layout
st.set_page_config(layout="wide")

#Background


#Setup containers
container0 = st.container()
container1 = st.container()
container2 = st.container()
container3 = st.container()
container4 = st.container()
container5 = st.container()
container6 = st.container()

#Introduction
with container0:
    st.header("Anime and Manga Comparison")



#Plot 1
with container1:
    st.subheader("Sources that Animes are Based On")

    #Count
    manga = 7.5 
    org = 2.5 

    data = [manga, org]

    name = ['Anime', 'Manga']

    fig = px.pie(
        values = data, names = name,
        color_discrete_sequence = [
            'orange',
            'purple'
        ]
    )

    st.plotly_chart(fig, theme = "streamlit", use_container_width = True)



#Columns
with container2:
    #Create columns
    col1, col2, col3 = st.columns(3)

    #Plot 2
    with col1:
        st.header("Plot 2")

    #Plot 3
    with col2:
        st.header("Plot 3")

    #Plot 4
    with col3:
        st.header("Plot 4")



#Columns
with container3:
    #Create columns
    col5, col4 = st.columns((2,1))

    #Plot 5
    with col4:
        st.header("Plot 5")

    #Columns
    with col5:
        with container4:
            col6, col7 = st.columns(2)

            #Plot 6
            with col6:
                st.header("Plot 6")

            #Plot 7
            with col7:
                st.header("Plot 7")    

            with container5:
                st.header("Plot 8") 