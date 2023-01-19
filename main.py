import streamlit as st
import pandas as pd
import plotly.express as px

df = px.data.gapminder()

st.write(df)