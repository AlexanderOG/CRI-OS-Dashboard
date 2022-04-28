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

@st.cache(suppress_st_warning=True) 
def getCountriesList(df):
    st.write("Cache miss: Getting countries list")
    # Get the countries list
    clist = df['location'].unique()

    # Define things that are not countries and remove them from the countries list
    notCountries = ['Africa', 'Asia', 'Central African Republic', 'Europe', 'European Union', 'High income', 'International', 'Low income', 'Lower middle income', 'North America', 'Oceania', 'South Africa', 'South America', 'Upper middle income', 'World']
    clist = list(clist)
    for i in notCountries:
        clist.remove(i)
    return clist

#A bit of styling
# Remove whitespace from the top of the page and sidebar
st.markdown("""
        <style>
               .css-12oz5g7 {
                    padding-top: 2rem;
                }
                .css-1adrfps{
                    padding-top: 1rem;
                }
                .css-1kyxreq {
                    display: flex;
                    flex-flow: row wrap;
                    row-gap: 1rem;
                    align-items: center;
                    justify-content: center;
                }
        </style>
        """, unsafe_allow_html=True)

df = loadData()
clist = getCountriesList(df)

typeList = {'New cases':'new_cases', 'New cases smoothed (7-day rolling average)':'new_cases_smoothed', 'Cummulative cases': 'total_cases', 'New deaths':'new_deaths', 'New deaths smoothed (7-day rolling average)':'new_deaths_smoothed', 'Cummulative deaths': 'total_deaths'}

# Create the streamlit sidebar
# Add LPI logo 
st.sidebar.image('https://www.learningplanetinstitute.org/user/themes/cri/images/LPI-sm.png', width=130)

select1 = st.sidebar.multiselect('Select Countries', clist, default=["France"])
dataType = st.sidebar.selectbox("Select the type of data you want to see:",typeList.keys())
dataTypeSelection = typeList[dataType]

normalized = st.sidebar.checkbox('Normalized data (per million habitants of the country)', True)
if normalized:
    dataType += " per million habitants"
    dataTypeSelection += "_per_million"

st.markdown("<h3 style='text-align: left; color: #ff4b4b;'>COVID-19 " + dataType + "</h2>", unsafe_allow_html=True)

### DATE SLIDER GOES HERE ###
dates = list(df[df['location'].isin(select1)]['date'])

if len(dates) > 0:
    start_date, end_date = st.sidebar.select_slider(
        'Select a time range: ',
        options=dates,
        value=(dates[0], dates[-1]), 
        format_func=lambda x: x.strftime("%d/%m/%Y"))
    df_1 = df[df['date'].between(start_date, end_date)]
    fig = px.line(df_1[df_1['location'].isin(select1)], x="date", y=dataTypeSelection, color="location", width=750, height=550).update_layout(xaxis_title="Date", yaxis_title=dataType)
    st.plotly_chart(fig)
else:
    st.write("Please select at least one country :)")
