import requests
import streamlit as st
# data
import pandas as pd
import numpy as np
from streamlit_lottie import st_lottie

#For Visualization
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_option_menu import option_menu

# Display lottie animations
def load_lottieurl(url):

    # get the url
    r = requests.get(url)
    # if error 200 raised return Nothing
    if r.status_code !=200:
        return None
    return r.json()
# Extract Lottie Animations
lottie_home1 = load_lottieurl("https://assets7.lottiefiles.com/private_files/lf30_F6EtR7.json")
lottie_dataset = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_jz1m61i7.json")
lottie_home= load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_mvpvrmrg.json")

#Title
st.set_page_config(page_title='NETFLIX',  layout='wide')

#header
#t1, t2 = st.columns((0.4,1)) 



#Hydralit Navbar
# define what option labels and icons to display
Menu = option_menu(None, ["Home", "Dataset",  "EDA"], 
    icons=['house', 'cloud-upload', "bar-chart-line","clipboard-check"], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "black", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "red"},
    }
)

  

# Home Page
if Menu == "Home":
      # Display Introduction
    st.markdown("""
    <article>
  <header class="bg-gold sans-seSans Serif">
    <div class="mw9 center pa4 pt5-ns ph7-l">
      <h3 class="f2 f1-m f-headline-l measure-narrow lh-title mv0">
        <span class="bg-black-90 lh-copy white pa1 tracked-tight">
        </span>
      </h3>
      <h4 class="f3 fw1 Sans Serif i"></h4>
      <h5 class="f6 ttu tracked black-80">By Razan Tayba</h5>
      </div>
      </p>
      </div>
      </article>""",unsafe_allow_html=True)
#Upload Image
    from PIL import Image
    title_container = st.container()
    col1, mid, col2 = st.columns([20,100,20])
    with title_container:
      with mid:
        st_lottie(lottie_home1, key = "NETFLIX",width = 600)
    from PIL import Image
    title_container = st.container()
    col1, mid, col2 = st.columns([20,100,20])
    with title_container:
      with mid:
        st.write('Netflix, Inc. is an American subscription streaming service and production company based in Los Gatos, California. Launched on August 29, 1997, it offers a film and television series library through distribution deals as well as its own productions, known as Netflix Originals 📽️ 🎬')

if Menu == "Dataset":
#data
# 2 Column Layouts of Same Size
    col4,col5 = st.columns([1,1])

    # First Column - Shows Description of EDA
    with col4:
        st.markdown("""
        <h3 class="f2 f1-m f-headline-l measure-narrow lh-title mv0">
         Data information
         </h3>
         <p class="f5 f4-ns lh-copy measure mb4" style="text-align: justify;font-family: Sans Serif">
          Before implementing the machine learning model, it is important at the initial stage to explore the data and understand and try to gather as many insights from it. 
         </p>
            """,unsafe_allow_html = True)

# Display customer churn animation
    with col5:
        st_lottie(lottie_dataset, key = "EDA", height = 400, width = 700)
    df=pd.read_csv('netflix_titles.csv')
    st.dataframe(df)

# EDA page
df=pd.read_csv('netflix_titles.csv')
if Menu == "EDA":
  st.header("Visualizations")

#Visualization
  g1,g2,g3= st.columns((9,1,1))
  k1,k2,k3=st.columns((0.5,9,0.5))
  s1,s2=st.columns((9,1))
  w1,w2=st.columns((1,1))
  h1,h2= st.columns((9,1))

# **I- Which country has added the most content to Netflix? (international projects separately)**
  with g1:
        st.markdown("""
        <h3 class="f2 f1-m f-headline-l measure-narrow lh-title mv0">
         I- Which country has added the most content to Netflix? (international projects separately)
         </h3>
         <p class="f5 f4-ns lh-copy measure mb4" style="text-align: justify;font-family: Sans Serif">
          
         </p>
            """,unsafe_allow_html = True)
  df['date'] = pd.to_datetime(df['date_added'])
  df['year'] = df['date'].apply(lambda datetime: datetime.year)
  df['month'] = df['date'].apply(lambda datetime: datetime.month)

  data_dict1 = {'Country': df.groupby('country').size().sort_values(ascending=False)[:20].index,
             'Number of content': df.groupby('country').size().sort_values(ascending=False)[:20].values
             }

  df_1 = pd.DataFrame(data=data_dict1, columns=['Country', 'Number of content'])
  fig = px.bar(df_1, x="Country",
                   y="Number of content",
                   title="Which country has added the most content to Netflix? (international projects separately)",
                   color='Number of content')

  fig.update_layout(autosize=False, width=950, height=600, xaxis_title="Country",
                  yaxis_title="Number of content")
  g1.plotly_chart(fig, use_container_width=True) 
  with g1:
        st.markdown("""
        <h3 class="f2 f1-m f-headline-l measure-narrow lh-title mv0">
         
         </h3>
         <p class="f5 f4-ns lh-copy measure mb4" style="text-align: justify;font-family: Sans Serif">
          Netflix has the most content from United States. Also, India ranks second in the amount of content added to Netflix 
         </p>
            """,unsafe_allow_html = True)

# II- Dynamics of content by years (no international projects)
  with k2:
        st.markdown("""
        <h3 class="f2 f1-m f-headline-l measure-narrow lh-title mv0">
         II- Dynamics of content by years (no international projects)
         </h3>
         <p class="f5 f4-ns lh-copy measure mb4" style="text-align: justify;font-family: Sans Serif">
          
         </p>
            """,unsafe_allow_html = True)
  y_с = df.groupby('year')['country'].value_counts().reset_index(name='counts')

  fig = px.choropleth(y_с, locations="country", color="counts", 
                    locationmode='country names',
                    animation_frame='year',
                    range_color=[0,100])

  fig.update_layout(title='Dynamics of content by years (no international projects)')
  k2.plotly_chart(fig, use_container_width=True) 
  with k2:
        st.markdown("""
        <h3 class="f2 f1-m f-headline-l measure-narrow lh-title mv0">
        
         </h3>
         <p class="f5 f4-ns lh-copy measure mb4" style="text-align: justify;font-family: Sans Serif">
          In the animation, we observe the amount of content added to Netflix by country for different years. There is a rapid increase in content in America as well as India
         </p>
            """,unsafe_allow_html = True)
# III- Dynamics of adding content for the top 5 countries by addition (excluding international projects)
  with s1:
        st.markdown("""
        <h3 class="f2 f1-m f-headline-l measure-narrow lh-title mv0">
         III- Dynamics of adding content for the top 5 countries by addition (excluding international projects)
         </h3>
         <p class="f5 f4-ns lh-copy measure mb4" style="text-align: justify;font-family: Sans Serif">
          
         </p>
            """,unsafe_allow_html = True)

  df.groupby('country').size().sort_values(ascending=False).nlargest(10).index
  top10_contry_of_cnt_content = df.groupby('country').size().sort_values(ascending=False).nlargest(5).index.tolist()
  df_6 = df.loc[df['country'].isin(top10_contry_of_cnt_content)]
  df_6_upd = df_6.groupby('year')['country'].value_counts().reset_index(name='counts')
  fig = px.line(df_6_upd, x="year", y="counts", color='country',
              title='Dynamics of adding content for the top 5 countries by addition (excluding international projects)', 
             markers=True)
  fig.update_layout(xaxis_title="Year",
                    yaxis_title="Number of content",
                    legend_title='Country')

  s1.plotly_chart(fig, use_container_width=True)

  with s1:
        st.markdown("""
        <h3 class="f2 f1-m f-headline-l measure-narrow lh-title mv0">
         
         </h3>
         <p class="f5 f4-ns lh-copy measure mb4" style="text-align: justify;font-family: Sans Serif">
          This graph shows that America has always led the way in adding content to Netflix
         </p>
            """,unsafe_allow_html = True)

# IV- Various genres on Netflix (TOP 20)
  with h1:
        st.markdown("""
        <h3 class="f2 f1-m f-headline-l measure-narrow lh-title mv0">
         IV- Various genres on Netflix (TOP 20)
         </h3>
         <p class="f5 f4-ns lh-copy measure mb4" style="text-align: justify;font-family: Sans Serif">
        
         </p>
            """,unsafe_allow_html = True)
  df['genre'] = df['listed_in'].apply(lambda x :  x.replace(' ,',',').replace(', ',',').split(','))
  key_value = {}  # key - genre, value - number of content 
  for g1 in df['genre']:
    for g2 in g1:
        if g2 not in key_value:
            key_value[g2] = 0
        key_value[g2] += 1

  df_upd = pd.DataFrame(data=list(zip(key_value.keys(), key_value.values())),
                      columns=['genre', 'Number of content']).sort_values('Number of content',
                                                                          ascending=False)[0:20]
  fig = px.bar(df_upd,
             x='genre',
             y="Number of content",
             title="Various genres on Netflix (TOP 20)",
             color='Number of content')

  fig.update_layout(
    autosize=False,
    width=950,
    height=600,
    xaxis_title="Genre",
    yaxis_title="Number of content",
    legend_title = 'Number of content',
    grid_pattern='independent')
  h1.plotly_chart(fig, use_container_width=True)

  with h1:
        st.markdown("""
        <h3 class="f2 f1-m f-headline-l measure-narrow lh-title mv0">
        
         </h3>
         <p class="f5 f4-ns lh-copy measure mb4" style="text-align: justify;font-family: Sans Serif">
          Netflix has the most international movies added, and Dramas comes second
         </p>
            """,unsafe_allow_html = True)
# V- Ratings for all content on Netflix
  with w1:
        st.markdown("""
        <h3 class="f2 f1-m f-headline-l measure-narrow lh-title mv0">
        V- Ratings for all content on Netflix
         </h3>
         <p class="f5 f4-ns lh-copy measure mb4" style="text-align: justify;font-family: Sans Serif">
         
         </p>
            """,unsafe_allow_html = True)
  df_5 = pd.DataFrame(data=df.groupby('rating').size()).reset_index()
  df_5 = df_5.loc[~df_5['rating'].isin(['66 min', '74 min', '84 min'])]
  df_5 = df_5.rename(columns={0: 'Number of content'})

  fig = px.pie(df_5, values='Number of content', names='rating',
             color_discrete_sequence=px.colors.sequential.RdBu, title='Ratings for all content on Netflix')

  fig.update_traces(textposition='inside', textinfo='percent+label')
  w1.plotly_chart(fig, use_container_width=True) 

  with w1:
        st.markdown("""
        <h3 class="f2 f1-m f-headline-l measure-narrow lh-title mv0">
        
         </h3>
         <p class="f5 f4-ns lh-copy measure mb4" style="text-align: justify;font-family: Sans Serif">
          Netflix has the most TV-MA-rated content (36.4 %)
         </p>
            """,unsafe_allow_html = True)
# VI- TV shows duration in Netflix

  with w1:
        st.markdown("""
        <h3 class="f2 f1-m f-headline-l measure-narrow lh-title mv0">
        VI- TV shows duration in Netflix
         </h3>
         <p class="f5 f4-ns lh-copy measure mb4" style="text-align: justify;font-family: Sans Serif">
         
         </p>
            """,unsafe_allow_html = True)

  df_tv_show = df.loc[df['type'] == 'TV Show']
  df_tv_show['duration'] = df_tv_show['duration'].str.replace(' Seasons', ' Season')
  df_tv_show['duration'] = df_tv_show['duration'].str.replace(' Season', ' Season(s)')


  df_7 = pd.DataFrame(data=df_tv_show.groupby('duration').size().reset_index())
  df_7.rename(columns={0: 'Number of TV Show'}, inplace=True)

  fig = px.pie(df_7, values='Number of TV Show', names='duration',
             color_discrete_sequence=px.colors.sequential.RdBu, title='TV shows duration in Netflix')

  fig.update_traces(textposition='inside', textinfo='percent+label')
  w2.plotly_chart(fig, use_container_width=True)

  with w1:
        st.markdown("""
        <h3 class="f2 f1-m f-headline-l measure-narrow lh-title mv0">
        
         </h3>
         <p class="f5 f4-ns lh-copy measure mb4" style="text-align: justify;font-family: Sans Serif">
          TV shows with a duration of 1 season the largest number
         </p>
            """,unsafe_allow_html = True)