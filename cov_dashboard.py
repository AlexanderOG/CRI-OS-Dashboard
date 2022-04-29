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

peakDetect = st.sidebar.checkbox('Show peak detection example')
if peakDetect:
    cPeak = st.sidebar.selectbox('Country for peak detection', clist, index=clist.index('France'))
    thres = st.sidebar.select_slider('Threshold', [5,10,15,20,25,30,35,40,45,50])
    auxN = df[df['location']==cPeak][['new_cases_smoothed','date']].dropna()
    cum = list(auxN['new_cases_smoothed'])
    dates2 = list(auxN['date'])
    def mode(slice):
        pos = slice.count(1)
        neg = slice.count(-1)
        if pos > neg:
            return 1
        else:
            return -1

    lim = int(thres)
    derivada = []
    for i in range(len(cum)-1):
        derivada.append(cum[i+1]-cum[i])

    signs = [1 if i >= 0 else -1 for i in derivada ]
    resp = []
    for i in range(len(signs)-lim):
        resp.append(mode(signs[i:i+lim]))
    last = resp[-1]
    for i in range(lim):
        resp.append(last)
    peaks2 = []
    for i in range(len(resp)-1):
        if resp[i+1] < 0 and resp[i] > 0 or resp[i+1] > 0 and resp[i] < 0:
            peaks2.append(i)
    peaks3 = []
    for i in range(len(peaks2)//2):
        peaks3.append((peaks2[2*i]+peaks2[2*i+1])//2)
    fig2, ax = plt.subplots()
    ax.plot(cum)
    ax.set_title('Peak detection example for ' + cPeak)
    ax.set_ylabel('New smooth cases')
    ax.set_xlabel('Date index')
    for i in peaks3:
        ax.plot(i, cum[i], marker="x", markersize=5, markeredgecolor="red")
    st.pyplot(fig2)
    #Detect highest peak
    auxN = df[df['location']==cPeak][['total_cases','date']].dropna()
    cum = list(auxN['total_cases'])
    dates2 = list(auxN['date'])
    derivada = []
    for i in range(len(cum)-1):
        derivada.append(cum[i+1]-cum[i])
    maxi = max(derivada)
    maxInd = derivada.index(maxi)
    thresHP = lim/100*maxi
    peaks4 = []
    for i in range(len(derivada)):
        if derivada[i] > thresHP:
            peaks4.append(i)
    fig3, ax = plt.subplots()
    ax.plot(cum)
    ax.set_title('Peak detection example for ' + cPeak)
    ax.set_ylabel('Cumulative cases')
    ax.set_xlabel('Date index')
    ax.plot(maxInd, cum[maxInd], marker="x", markersize=5, markeredgecolor="red")
    st.pyplot(fig3)

