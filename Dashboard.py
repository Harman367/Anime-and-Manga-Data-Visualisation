#Imports
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go
from ast import literal_eval
import plotly.figure_factory as ff

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

    fig.update_layout(font_size = 20)
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
    fig.update_layout(barmode='group', height = 650, margin_b = 150, colorway = ['#F47521', '#5b0bb5'], yaxis_title = "Score", yaxis_range=[0,10])
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

#Plot 5
def plot5():
    values = []

    values.append(df_anime['total'].sum())
    values.append(df_manga['total'].sum())
    values.append(df_anime['watching'].sum())
    values.append(df_manga['reading'].sum())
    values.append(df_anime['completed'].sum())
    values.append(df_manga['completed'].sum())
    values.append(df_anime['on_hold'].sum())
    values.append(df_manga['on_hold'].sum())
    values.append(df_anime['dropped'].sum())
    values.append(df_manga['dropped'].sum())
    values.append(df_anime['plan_to_watch'].sum())
    values.append(df_manga['plan_to_read'].sum())

    colors = [       
    'rgba(244, 117, 33 , 0.75)',
    'rgba(244, 117, 33 , 0.75)',
    'rgba(100, 20, 200, 0.5)',
    'rgba(0, 0, 255, 0.5)',
    'rgba(0, 255, 0, 0.5)',
    'rgba(255, 0, 0, 0.5)',
    'rgba(255, 0, 255, 1)',
    'rgba(0, 255, 255, 0.5)',
    'rgba(139, 128, 0, 1)',
    'rgba(255, 125, 125, 0.5)',
    'rgba(125, 255, 125, 0.5)',
    'rgba(125, 125, 255, 0.5)'
    ]

    fig = go.Figure(data=[go.Sankey(
        node = dict(
        pad = 20,
        thickness = 25,
        line = dict(color = 'black', width = 2),
        label = ["Total", "Anime", "Manga", "Watching / Reading", "Completed", "On hold", "Dropped", "Plan to watch / read"],
        color = '#5b0bb5'
        ),
        link = dict(
        source = [0, 0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
        target = [1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7],
        value = values,
        color = colors
    ))])

    fig.update_layout(font_size = 18)
    st.plotly_chart(fig, theme = "streamlit", use_container_width = True)

#Plot 6
def plot6():
    timeline = []

    for i in range(10):
        timeline.append(dict(Task = df_sales['Manga series'][i], Start = str(df_sales['Start'][i]), Finish = str(df_sales['End'][i]), Type = 'Manga'))

    timeline.append(dict(Task = df_sales['Manga series'][0], Start = "1999", Finish = "2023", Type = 'Anime'))
    timeline.append(dict(Task = df_sales['Manga series'][1], Start = "1986", Finish = "1996", Type = 'Anime'))
    timeline.append(dict(Task = df_sales['Manga series'][2], Start = "2008", Finish = "2009", Type = 'Anime'))
    timeline.append(dict(Task = df_sales['Manga series'][3], Start = "2023", Finish = "2023", Type = 'Anime'))
    timeline.append(dict(Task = df_sales['Manga series'][4], Start = "1996", Finish = "2023", Type = 'Anime'))
    timeline.append(dict(Task = df_sales['Manga series'][5], Start = "2002", Finish = "2017", Type = 'Anime'))
    timeline.append(dict(Task = df_sales['Manga series'][6], Start = "1993", Finish = "2011", Type = 'Anime'))
    timeline.append(dict(Task = df_sales['Manga series'][7], Start = "1993", Finish = "1996", Type = 'Anime'))
    timeline.append(dict(Task = df_sales['Manga series'][8], Start = "2023", Finish = "2023", Type = 'Anime'))
    timeline.append(dict(Task = df_sales['Manga series'][9], Start = "2019", Finish = "2023", Type = 'Anime'))

    colors = {
        'Manga': '#5b0bb5',
        'Anime': '#F47521'
    }

    fig = ff.create_gantt(timeline, colors = colors, index_col = "Type", show_colorbar = True, group_tasks = True, title = "")
    st.plotly_chart(fig, theme = "streamlit", use_container_width = True)

#Plot 7
def plot7():
    sales = []

    for i in range(10):
        sales.append(dict(Manga = df_sales['Manga series'][i], Sales = (df_sales['Approximate sales'][i] - df_sales['Average sales per volume'][i]), Type = "Sales"))
        sales.append(dict(Manga = df_sales['Manga series'][i], Sales = df_sales['Average sales per volume'][i], Type = "Volume"))

    fig = px.bar(sales, x="Manga", y="Sales", color="Type", color_discrete_sequence = ['#5b0bb5', '#F47521'])
    fig.update_layout(yaxis_title = "Sold Copies (Millions)")
    st.plotly_chart(fig, theme = "streamlit", use_container_width = True)

#Plot 8
def plot8():
    input = []

    for i in range(50):
        input.append(dict(Scored = df_anime['scored_by'][i], Score = df_anime['score'][i], Type = "Anime"))
        input.append(dict(Scored = df_manga['scored_by'][i], Score = df_manga['score'][i], Type = "Manga"))
        

    fig = px.scatter(input, x = "Scored", y = "Score", color = "Type", color_discrete_sequence = ['#5b0bb5', '#F47521'])
    fig.update_layout(yaxis_title = "Average Score", xaxis_title = "Scored By")
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
        st.write("Shounen: Young Male")
        st.write("Seinen: Young Adult Male")
        st.write("Shoujo: Young Female")
        st.write("Josei: Young Adult Female")



#Container
with container3:
    st.subheader("Top 50 Anime and Manga Scores vs Number of People who Scored")
    plot8()


#Columns
with container4:
    col6, col7 = st.columns(2)

    #Plot 6
    with col6:
        st.subheader("Publication of Top 10 Manga Sales and thier Anime release")
        plot6()

    
    with col7:
        
        #Plot 5
        st.subheader("Status of Anime and Manga Consumers")
        plot5()

#Plot 7
with container5: 
    st.subheader("Top 10 Manga Sales and Average Sales per Volume")
    plot7()    