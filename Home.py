import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")

place=st.text_input("Place: ")
days=st.slider(label="Forcast Days:", min_value=1,max_value=5, help="Select number of forecasted days")
option = st.selectbox( "Select data to view", ("Temperature", 'Sky') )
st.subheader(f"{option} for next {days} days in {place}")

get_data( place , days , option)
figure= px.line(x=d, y=t, labels={"x": "date", "y": "temperature (c)"})
st.plotly_chart(figure)
