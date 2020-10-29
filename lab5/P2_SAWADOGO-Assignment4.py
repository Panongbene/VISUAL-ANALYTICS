#First the things we need to import
import streamlit as st

st.title("The Ethics of Communicating Data with Visualization")

st.title(" Greenhouse Gas Emissions 1990–2018")

#Everything written between three single apostrophes will be interpreted as markdown and printed on the webpage streamlit creates. Everything outside will be treated as code to be run.

'''
[Greenhouse Gas Emissions 1990–2018](https://stats.oecd.org/Index.aspx?DataSetCode=AIR_GHG). The Organization for Economic Co-operation and Development (OECD) has compiled data for the emissions of all participating countries broken out by the pollutant (e.g., carbon monoxide, methane, etc.) and by different sources (e.g., energy, agriculture, etc.). The linked interface can be a little difficult to use, but you can access various slices of the data by either choosing alternate themes in the left-hand side menu, or by customizing the pollutants and variables in the dropdown menus in the main view.

'''

st.header("P2: \"dishonest/unethical/deceiving\"")
'''
For a perspective view 2 below, the following guidelines must be observed:

  - The visual representation is intentionally inappropriate, overly complex and/or too cluttered for the audience.
 
  - Labels, axes, and legends are misleading.
 
  - Titles are skewed to intentionally influence the viewer’s perception.

  - The data has been transformed, filtered, or processed in an intentionally misleading way

  -  The source and provenance of the data is not clear to the viewer.


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

*We import Greenhouse Gas Emissions 1990–2018 from ours google drive*

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
    Transport_data_fram = green_house_gas_1990_2018[green_house_gas_1990_2018["Variable"] == "1C - CO2 from Transport and Storage"]



st.header('Pollution from the transport sector and other elements decreases over time in Organization for Economic Co-operation and Development (OECD) countries')

# Build the chart and add description'

with st.echo():
    chart = alt.Chart(Transport_data_fram).mark_area().encode(
        x='Year',
        y='mean(Value)',
        color='Country:N'
    ).interactive().properties(
        width=780, 
        height=800
    )
    st.write(chart)

'''This graph, supposed to show the decrease over time in greenhouse gas emissions in the transport sector in OECD countries, meets the P2 criterion. 

This is because the data visualized is not the data of the transport sector itself, we took the data of the transport sector plus the data of the storage sector to construct the curve. We mentioned it in a nuanced way in our headline saying that this is the data of the transport sector with other elements.

Also, the countries represented are not all OECD countries. In fact, we have shown just 5 surface curves the first is Canada, the second is Norway, the third is Turkey and the 4 is the average of data on EURE countries and the fifth is the average of data on OECD countries. The choice was made so as to have a curve that will decrease at the end.

The visualization tool used has also been nuanced, in fact with the visualization by the nested surfaces, it is more difficult to have a real understanding and that requires to make efforts to understand what we are talking about.
'''