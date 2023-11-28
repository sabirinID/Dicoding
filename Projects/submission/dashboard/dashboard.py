# Mengimpor pustaka
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="dark")

# Membaca data
main_data = pd.read_csv(
    "https://raw.githubusercontent.com/sabirinID/IDCamp/main/Projects/submission/dashboard/main_data.csv"
)

# Mengubah kolom 'date' menjadi datetime
main_data["date"] = pd.to_datetime(main_data["date"])

# Menghitung total rentals harian
daily_total_rentals = main_data.groupby(pd.Grouper(key="date", freq="D"))[
    ["non_registered_user_rentals", "registered_user_rentals"]
].sum()
daily_total_rentals["total_rentals"] = (
    daily_total_rentals["non_registered_user_rentals"]
    + daily_total_rentals["registered_user_rentals"]
)
daily_total_rentals.reset_index(inplace=True)

# Menghitung total rentals bulanan
monthly_total_rentals = daily_total_rentals.resample("M", on="date").sum()

st.title("Bike Share Dashboard")

st.text("Created by Syahril Dimas Sabirin, @sabirinID")

st.header("Jumlah Rental Sepeda")

st.subheader("Daily Rentals")

col1, col2, col3 = st.columns(3)

with col1:
    min_rentals = daily_total_rentals["total_rentals"].min()
    st.metric("Min Rentals", value=min_rentals)
with col2:
    max_rentals = daily_total_rentals["total_rentals"].max()
    st.metric("Max Rentals", value=max_rentals)
with col3:
    total_rentals = daily_total_rentals["total_rentals"].sum()
    st.metric("Total Rentals", value=total_rentals)
fig, ax = plt.subplots(figsize=(16, 9))
ax.plot(
    daily_total_rentals["date"],
    daily_total_rentals["total_rentals"],
    marker="o",
    linewidth=2,
    color="tab:blue",
)
ax.tick_params(axis="y", labelsize=20)
ax.tick_params(axis="x", labelsize=15)

st.pyplot(fig)

st.subheader("Monthly Rentals")

col1, col2, col3 = st.columns(3)

with col1:
    min_rentals = monthly_total_rentals["total_rentals"].min()
    st.metric("Min Rentals", value=min_rentals)
with col2:
    max_rentals = monthly_total_rentals["total_rentals"].max()
    st.metric("Max Rentals", value=max_rentals)
with col3:
    total_rentals = monthly_total_rentals["total_rentals"].sum()
    st.metric("Total Rentals", value=total_rentals)
fig, ax = plt.subplots(figsize=(16, 9))
ax.plot(
    monthly_total_rentals.index,
    monthly_total_rentals["total_rentals"],
    marker="o",
    linewidth=2,
    color="tab:blue",
)
ax.tick_params(axis="y", labelsize=20)
ax.tick_params(axis="x", labelsize=15, rotation=90)

st.pyplot(fig)

st.caption("Copyright (c) @sabirinID 2023")