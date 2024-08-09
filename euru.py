import streamlit as st
import pandas as pd
from plotly import graph_objects as go


df = pd.read_csv(R"D:DA_finalproject\result.csv")

st.title("bitcoin")

topic = st.selectbox("topic",["data frame", "describe", "candle stick"])

if st.button("do it"):
    if topic=="data frame":
        st.write(df)

    if topic=="describe":
        st.write(df.describe())
    
    if topic=="candle stick":
        candle_stick = go.Figure(go.Candlestick(x=df.index, open=df.Open, high=df.High, low=df.Low, close=df.Close))
        
        st.plotly_chart(candle_stick)