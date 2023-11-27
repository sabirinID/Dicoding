# Import library
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('main_data.csv')

# Create a sidebar
option = st.sidebar.selectbox(
    'Select variable:',
    ('temperature', 'humidity', 'wind_speed'))

# Create a plot based on the selected option
st.title(f'Plot of {option}')
plt.figure(figsize=(16, 9))
plt.hist(df[option], bins=30)
plt.xlabel(option)
plt.ylabel('Count')
st.pyplot()