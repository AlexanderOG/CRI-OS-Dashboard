import streamlit as st
import pandas as pd
import plotly.express as px

# Read the data
df = pd.DataFrame(px.data.gapminder())

# Get the countries list
clist = df['country'].unique()

# Create the streamlit sidebar
country = st.sidebar.selectbox("Select a country:",clist)

# The header of the figure
st.header("GDP per Capita over time")

# Create a figure
fig = px.line(df[df['country'] == country], x = "year", y = "gdpPercap", title = country)

# Plots the chart
st.plotly_chart(fig)