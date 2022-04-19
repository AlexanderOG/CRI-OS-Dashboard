import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

@st.cache(suppress_st_warning=True) 
def loadData():
    st.write("Cache miss: Loading data")
    df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv')
    df["date"] = pd.to_datetime(df["date"])
    return df

df = loadData()

# Get the countries list
clist = df['location'].unique()

# Create the streamlit sidebar
country = st.sidebar.selectbox("Select a country:",clist)

# The header of the figure
st.header("COVID-19 cases per country")

cases = df[df['location'] == country]['new_cases']
dates = list(df[df['location'] == country]['date'])

# Create a figure
fig, ax = plt.subplots()
# plot data
ax.plot( dates, cases)
ax.tick_params(axis='x',rotation=90)


# Plots the chart
st.plotly_chart(fig)

# ---------------------------------------------------------
# # MultySelector goes here
# # Get the countries list
clist = df['location'].unique()

# Create the streamlit sidebar
# country = st.sidebar.selectbox("Select a country:",clist)
country = st.sidebar.multiselect("Select countries:",clist,'Afghanistan')
# The header of the figure
st.header("COVID-19 cases per country - Multy Countries")

cases = df[df['location'] == country]['new_cases']
dates = list(df[df['location'] == country]['date'])

# Create a figure
fig = plt.figure()
# plt.figure(figsize=(12,5))
plt.plot(dates, cases)

# Plots the chart
st.plotly_chart(fig)
# ---------------------------------------------------------
# data = df

# # Create a list of possible values and multiselect menu with them in it.
# COUNTRIES = df['location'].unique()
# COUNTRIES_SELECTED = st.sidebar.multiselect('Select countries', COUNTRIES)

# # Mask to filter dataframe
# mask_countries = df['COUNTRIES_SELECTED'].isin(COUNTRIES)

# # df = df[mask_countries]
# st.write('You selected:', mask_countries)
