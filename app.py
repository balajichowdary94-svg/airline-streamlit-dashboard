import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Airline Flight Delay Dashboard")

@st.cache_data
def load_data():
    cols = [
        'YEAR','MONTH','AIRLINE',
        'DEPARTURE_DELAY','ARRIVAL_DELAY',
        'CANCELLED','DISTANCE'
    ]
    df = pd.read_csv("flights_sample.csv", usecols=cols)
    df = df.sample(200000, random_state=42)
    df = df[df["CANCELLED"] == 0]
    df = df.dropna()
    return df

df = load_data()
