import streamlit as st
import pandas as pd
import plotly.express as px

df = px.data.gapminder()

st.write(df)

year_options = df['year'].unique().tolist()
year = st.selectbox('Which year would you like  to see?', year_options,0)
df = df[df['year']==year]
