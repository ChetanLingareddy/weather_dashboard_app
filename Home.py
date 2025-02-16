import streamlit as st
import plotly.express as px

from backend import get_data

st.title("Weather Forecast for the Next 5 Days")

# Frontend , take values from user
place=st.text_input("Place: ")
days=st.slider(label="Forcast Days:", min_value=1,max_value=5, help="Select number of forecasted days")
option = st.selectbox( "Select data to view", ("Temperature", 'Sky') )

# try error block for error handling
try:
    if place:
        st.subheader ( f"{option} for next {days} days in {place}" )

        #Getting data from backend
        filtered_data = get_data ( place, days )

        if option == "Temperature":

            #getting  temperature and dates from filtered_data
            temperature = [value["main"]["temp"]/10 for value in filtered_data]
            dates = [value["dt_txt"] for value in filtered_data]

            # Printing a graph with the data using plotly
            figure= px.line(x=dates, y=temperature, labels={"x": "date", "y": "temperature (c)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "rain":"images/rain.png", "Snow":"images/snow.png"}

            #getting  sky_condition  from filtered_data
            sky_conditions = [value["weather"][0]["main"] for value in filtered_data]

            #image_path = [images[condition] for condition in sky_conditions]
            #st.image(image_path, width=115)
            max_cols = 6
            day_count = 1  # Start day count

            # Loop through sky_conditions with step-size of 8
            for i in range ( 0, len ( sky_conditions ), 8 ) :
                st.subheader ( f"Day {day_count}" )  # Print day count

                # Create columns for up to 6 images in a row
                cols = st.columns ( max_cols )

                # Get the next 8 images, but only display 6 per row
                for j, condition in enumerate ( sky_conditions[i :i + 8] ) :
                    with cols[j % max_cols] :  # Use modulo to ensure 6 images per row
                        st.image ( images[condition], width=115, caption=condition )

                day_count += 1
except KeyError: st.error("Error: City Doesn't Exist,  Try with a correct name.")
