import streamlit as st 
import math
import pandas as pd
import os
import matplotlib.pyplot as plt


DATADIR = os.path.join(os.getcwd(),'pubs.csv')
st.title("Open Pubs Dataset")
st.write("This is a dataset of open pubs in the UK.")

data = pd.read_csv(DATADIR)
data = data.drop('Unnamed: 0',axis=1)
st.write("Number of pubs:", len(data))
st.write("Columns:", list(data.columns))
st.title('First 10 rows of the Dataset')
st.dataframe(data.head(10))

st.title('Description of Dataset')
st.dataframe(data.describe())

