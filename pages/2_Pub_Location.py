import os
import pandas as pd
import streamlit as st

DATADIR = os.path.join(os.getcwd(),'pubs.csv')

data = pd.read_csv(DATADIR)
data = data.drop('Unnamed: 0',axis=1)

st.title("Pubs by Location")

# Get location input from user
location_type = st.radio("Select Location Type", ("Postal Code", "Local Authority"))
location = st.text_input(f"Enter {location_type}")

# Filter pubs by location
if location:
    if location_type == "Postal Code":
        pubs = data[data.postcode.str.startswith(location.upper())]
    else:
        pubs = data[data.local_authority== location.title()]

    st.write(f"Number of pubs in {location.title()}: {len(pubs)}")

    # Create map centered on location
    map_data = pubs[["latitude", "longitude"]]
    st.map(map_data,zoom=7)
    
    