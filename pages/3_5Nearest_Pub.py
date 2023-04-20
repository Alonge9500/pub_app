import numpy as np
import streamlit as st
import pandas as pd
from math import sqrt
import os

DATADIR = os.path.join(os.getcwd(),'pubs.csv')

data = pd.read_csv(DATADIR)
data = data.drop('Unnamed: 0',axis=1)




def euclidean_distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


st.title("Find the 5 Nearest Pub")

# Get user's location
lat = st.number_input("Latitude")
lng = st.number_input("Longitude")

if st.button("Find"):
    if pd.isna(lat) or pd.isna(lng):
        st.warning("Please enter a valid location.")
    else:
        # Calculate distances from user's location to each pub
        data["distance"] = data.apply(
            lambda row: euclidean_distance(lat, lng, row["latitude"], row["longitude"]),
            axis=1,
        )

        # Sort pubs by distance and display the nearest 5 on a map
        nearest_pubs = data.sort_values("distance").head(5)
        st.write(f"Nearest Pubs to ({lat}, {lng}):")
        st.write(nearest_pubs[["name", "address", "distance"]])

        # Create map centered on user's location
        map_data = nearest_pubs[["latitude", "longitude"]]
        st.map(map_data)
        for i, row in nearest_pubs.iterrows():
            name = row["name"]
            address = row["address"]
            distance = row["distance"]
            st.write(f"{i+1}. {name} ({address}) - {distance:.2f} km")
            st.markdown(f'<a href="https://www.google.com/maps/search/?api=1&query={row["latitude"]},{row["longitude"]}" target="_blank">View on Google Maps</a>', unsafe_allow_html=True)

