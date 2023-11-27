# Import library
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('main_data.csv', index=False)

min_date = df['date'].min()
max_date = df['date'].max()
 
with st.sidebar:
    # Menambahkan logo
    st.image('https://cdn.lyft.com/static/bikesharefe/logo/CapitalBikeshare-main.svg')

    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )