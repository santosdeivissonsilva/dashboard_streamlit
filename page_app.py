import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide", page_title="Streamlit Dados")

tabela = pd.read_csv('supermarket_sales.csv', sep=';', decimal=',')

# Ordenando a tabela por data
tabela["Date"] = pd.to_datetime(tabela["Date"])
tabela = tabela.sort_values("Date")


tabela["Month"] = tabela["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Mês", tabela["Month"].unique())


tabela_filtrada = tabela[tabela["Month"] == month]
tabela_filtrada

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

grafico_data = px.bar(tabela_filtrada, x="Date", y="Total", title="Faturamento por dia")
col1.plotly_chart(grafico_data)
