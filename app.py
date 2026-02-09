import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="Airline Flight Delay Dashboard",
    layout="wide"
)

st.title("✈️ Airline Flight Delay Dashboard")


@st.cache_data
def load_data():
    cols = [
        "YEAR",
        "MONTH",
        "DAY",
        "AIRLINE",
        "ORIGIN_AIRPORT",
        "DESTINATION_AIRPORT",
        "DEPARTURE_DELAY",
        "ARRIVAL_DELAY"
    ]
    df = pd.read_csv("flights_sample.csv", usecols=cols)
    return df

df = load_data()


st.sidebar.header("Filters")

airline_options = sorted(df["AIRLINE"].dropna().unique())
selected_airline = st.sidebar.selectbox(
    "Select Airline",
    ["All"] + airline_options
)

if selected_airline != "All":
    df = df[df["AIRLINE"] == selected_airline]


col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Flights",
    f"{len(df):,}"
)

col2.metric(
    "Avg Departure Delay (min)",
    f"{df['DEPARTURE_DELAY'].mean():.2f}"
)

col3.metric(
    "Avg Arrival Delay (min)",
    f"{df['ARRIVAL_DELAY'].mean():.2f}"
)

st.divider()


st.subheader("Average Arrival Delay by Airline")

avg_delay = (
    df.groupby("AIRLINE")["ARRIVAL_DELAY"]
    .mean()
    .sort_values()
)

fig1, ax1 = plt.subplots()
avg_delay.plot(kind="barh", ax=ax1)
ax1.set_xlabel("Minutes")
ax1.set_ylabel("Airline")

st.pyplot(fig1)


st.subheader("Flights Per Month")

monthly_flights = df.groupby("MONTH").size()

fig2, ax2 = plt.subplots()
monthly_flights.plot(marker="o", ax=ax2)
ax2.set_xlabel("Month")
ax2.set_ylabel("Number of Flights")

st.pyplot(fig2)


st.subheader("Arrival Delay Distribution")

fig3, ax3 = plt.subplots()
ax3.hist(df["ARRIVAL_DELAY"].dropna(), bins=40)
ax3.set_xlabel("Arrival Delay (minutes)")
ax3.set_ylabel("Number of Flights")

st.pyplot(fig3)

with st.expander("Show Raw Data"):
    st.dataframe(df.head(100))

