#Imports
import numpy as np
import os
import pandas as pd
import plotly.express as px
import streamlit as st
import math
import json
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from ast import literal_eval

#Load files into dataframes
df_anime = pd.read_csv('Clean_Dataset/anime_clean.csv')
df_manga = pd.read_csv('Clean_Dataset/manga_clean.csv')
df_sales = pd.read_csv('Clean_Dataset/manga_sales.csv', encoding = 'cp1252')

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

#Plots

#Plot 1
def plot1():
    sources = df_anime.source.unique()
    values = []

    for source in sources:
        values.append(df_anime['source'].value_counts()[source])


    fig = px.pie(
        values = values, names = sources,
        color_discrete_sequence = [
            'orange',
            'purple',
            'blue',
            'green',
            'red',
            'pink'
        ], height = 800
    )
    st.plotly_chart(fig, theme = "streamlit", use_container_width = True)

#Plot 2
def plot2():
    st.image("word_cloud.jpg")

#Plot 3
def plot3():
    sorted = df_anime.sort_values(by = ['score'], ascending=False)
    sorted = sorted.loc[sorted['source'] == 'manga']
    sorted = sorted.head(10)

    findmanga = [90125, 25, 44, 23390, 44, 44, 26, 44, 102, 44]
    mangas = [8.92, 9.05, 8.62, 8.57, 8.62, 8.62, 8.7, 8.62, 8.52, 8.62]



    fig = go.Figure(data=[
        go.Bar(name='Anime', x=sorted['title_english'], y=sorted['score']),
        go.Bar(name='Manga', x=sorted['title_english'], y=mangas)
    ])

    # Change the bar mode
    fig.update_layout(barmode='group', height = 650, margin_b = 150, colorway = ['#F47521', '#5b0bb5'], yaxis_title = "Score")
    st.plotly_chart(fig, theme = "streamlit", use_container_width = True)

#Plot 4
def plot4():
    categories = ['Shounen', 'Seinen', 'Shoujo', 'Josei', 'Kids']

    anime_cat_count = [0,0,0,0,0]
    manga_cat_count = [0,0,0,0,0]


    for demographic in df_anime['demographics']:
        
        output = np.array(literal_eval(demographic))

        for i in output:
            if i in categories:
                index = categories.index(i)
                anime_cat_count[index] += 1

    for demographic in df_manga['demographics']:
        
        output = np.array(literal_eval(demographic))

        for i in output:
            if i in categories:
                index = categories.index(i)
                manga_cat_count[index] += 1


    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r = anime_cat_count,
        theta = categories,
        fill = 'toself',
        name ='Anime',
        fillcolor = '#5b0bb5',
        opacity = 0.5
    ))

    fig.add_trace(go.Scatterpolar(
        r = manga_cat_count,
        theta = categories,
        fill = 'toself',
        name = 'Manga',
        fillcolor = '#F47521',
        opacity = 0.5
    ))

    fig.update_layout(
    polar = dict(
        radialaxis = dict(
        visible = True,
        range = [0, 170]
        )),
    showlegend = True, height = 750, font_size = 30
    )
    st.plotly_chart(fig, theme = "streamlit", use_container_width = True)

#Introduction
with container0:
    st.header("Anime and Manga Comparison")



#Plot 1
with container1:
    st.subheader("Top 10 Anime Rating vs Manga Rating")
    plot3()



#Columns
with container2:
    #Create columns
    col1, col2, col3 = st.columns(3)

    #Plot 2
    with col1:
        st.subheader("Most Common Genres in Highest Rated Animes and Manga")
        plot2()

    #Plot 3
    with col2:
        st.subheader("Sources that Animes are Based On")
        plot1()

    #Plot 4
    with col3:
        st.subheader("Spread of Demographics")
        plot4()




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