import streamlit as st
import pandas as pd
import plotly.express as px

df = px.data.gapminder()

st.write(df)

year_options = df['year'].unique().tolist()
year = st.selectbox('Which year would you like  to see?', year_options,0)
df = df[df['year']==year]

fig = px.scatter(df,x="gdpPercap",y="lifeExp",size="pop", color="continent",hover_name="continent",log_x=True, size_max=55, range_x=[100,100000],range_y=[25,90])

fig.update_layout(width=800)

st.write(fig)


covid = pd.read_csv('https://raw.githubusercontent.com/shinokada/covid-19-stats/master/data/daily-new-confirmed-cases-of-covid-19-tests-per-case.csv')

covid.columns = ['Country','Code','Date','Confirmed','Days since confirmed']
covid['Date'] = pd.to_datetime(covid['Date']).dt.strftime('%y-%m-%d')
country_options= covid['Country'].unique().tolist()

st.write(covid)

date_options = covid['Date'].unique().tolist()
date = st.selectbox('Which date would you like to see?',date_options,100)
country = st.multiselect('Which country would you like to see?',country_options,['Brazil'])

