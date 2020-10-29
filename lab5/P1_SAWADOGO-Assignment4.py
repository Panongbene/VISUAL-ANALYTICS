#First the things we need to import
import streamlit as st

st.title("The Ethics of Communicating Data with Visualization")

st.title(" Greenhouse Gas Emissions 1990–2018")

#Everything written between three single apostrophes will be interpreted as markdown and printed on the webpage streamlit creates. Everything outside will be treated as code to be run.

'''
[Greenhouse Gas Emissions 1990–2018](https://stats.oecd.org/Index.aspx?DataSetCode=AIR_GHG). The Organization for Economic Co-operation and Development (OECD) has compiled data for the emissions of all participating countries broken out by the pollutant (e.g., carbon monoxide, methane, etc.) and by different sources (e.g., energy, agriculture, etc.). The linked interface can be a little difficult to use, but you can access various slices of the data by either choosing alternate themes in the left-hand side menu, or by customizing the pollutants and variables in the dropdown menus in the main view.

'''

st.header("P1: \"honest/ethical/truthful\"")
'''
For a perspective view 1 below, the following guidelines must be observed:

  - The visualization is clear and easy to interpret for the intended audience (often parts of the general population).
 
  - Any data transformations (e.g., filters, additional computations, etc.) are clearly and transparently communicated.
 
  - The sources of the data, including potential bias, is communicated

'''



#Import all library we need


st.header("Visualization")

'''

*We import the necessary library*

'''
with st.echo():
    import requests
    import pandas as pd
    import altair as alt
    import streamlit as st
    from io import StringIO

# load the data
'''

*We import Greenhouse Gas Emissions 1990–2018*

'''
with st.echo():
    orig_url= "https://drive.google.com/file/d/1S3mE7-CWL1Hve0GVpGmpBPSTdMkOYNRL/view?usp=sharing"
    file_id = orig_url.split('/')[-2]
    dwn_url='https://drive.google.com/uc?export=download&id=' + file_id
    url = requests.get(dwn_url).text
    csv_raw = StringIO(url)
    green_house_gas_1990_2018 = pd.read_csv(csv_raw)
    green_house_gas_1990_2018.rename(columns={'ï»¿"COU"': 'COU'}, inplace=True)

# Plot some data
'''

*We visualize the head of data*

'''
with st.echo():
    st.write(green_house_gas_1990_2018.head())


# Extract data only related to 3 - Agriculture'
'''

*We extract data only related to "3 - Agriculture"*

'''
with st.echo():
    country_data_fram = green_house_gas_1990_2018[green_house_gas_1990_2018["Variable"] == '3 - Agriculture']



st.header('Annual evolution of greenhouse gas emissions from 1990 to 2018 in the agricultural sector in the various countries of the Organization for Economic Cooperation and Development (OECD)')

# Build the chart and add description'

with st.echo():
    chart = alt.Chart(country_data_fram).mark_bar().encode(
        alt.X('Country'),
        alt.Y('mean(Value)'),
        color='Year:N',
        tooltip='Value:N',
    ).interactive().properties(
        width=780, 
        height=800
    )
    st.write(chart)

'''This graph shows the annual change between the dates 1990 to 2018 of greenhouse gas emissions in the agricultural sector in the various OECD member countries. 

The data used to produce this graph have been downloaded from the official statistics website of the OECD do these data are reliable.

To represent the graph, we have chosen a bar representation so that the countries are in the abscissa axis and the emission values ​​in the ordinate axis. This way of doing things gives us the values ​​of the emissions according to the countries.

The different values of gas emissions as a function of the dates were obtained by coloring the height of each bar as a function of the year and by highlighting the correspondence between the dates and the colors on the right. Thus, it is easy to check the value of the emission of each country for a well determined date. 
'''
