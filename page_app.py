import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Streamlit Dados")

tabela = pd.read_csv('supermarket_sales.csv', sep=';', decimal=',')
