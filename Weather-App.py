import streamlit as st
import json
import requests

def weather_info(city):
    api_key = '3e1e57b36b71498089f92200242809'
    base_url = f"http://api.weatherapi.com/v1/current.json?key=3e1e57b36b71498089f92200242809&q={city}&aqi=no"
    response = requests.get(base_url)

    if(response.status_code==200):
        data=response.json()
        st.write(f"The name of the city is: {data['location']['name']}")
        st.write(f"The name of the region is: {data['location']['region']}")
        st.write(f"The local time is: {data['location']['localtime']}")
        st.write(f"The Temperature of the city is: {data['current']['temp_c']} C")
        st.write(f"The weather feels like: {data["current"]["condition"]["text"]}")

        img_url=data["current"]["condition"]["icon"]
        img_url="https:"+img_url
        st.image(img_url)

    else:
        st.error("The weather info for the city could not be fetched...please try again.")


st.title("Weather application 🌤️")
st.subheader("This applications displays weather information")
city=st.text_input("Enter city name here:")

if st.button("Display Weather Information"):
    weather_info(city)
