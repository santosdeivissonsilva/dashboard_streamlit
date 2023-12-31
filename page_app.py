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

grafico_data = px.bar(tabela_filtrada, x="Date", y="Total", 
                     color="City",title="Faturamento por dia")
col1.plotly_chart(grafico_data, use_container_width=True)

grafico_produto = px.bar(tabela_filtrada, x="Date", y="Product line",
                         color="City", title="Faturamento por tipo de produto",
                         orientation="h")
col2.plotly_chart(grafico_produto, use_container_width=True)

total_cidade = tabela_filtrada.groupby("City")[["Total"]].sum().reset_index()
grafico_cidade = px.bar(total_cidade, x="City", y="Total",
                        title="Faturamento por cidade")
col3.plotly_chart(grafico_cidade, use_container_width=True)

grafico_tipo = px.pie(tabela_filtrada, values="Total", names="Payment",
                    title="Faturamento por tipo de pagamento")
col4.plotly_chart(grafico_tipo, use_container_width=True)

avaliacao_cidade = tabela_filtrada.groupby("City")[["Rating"]].mean().reset_index()
grafico_avaliacao = px.bar(avaliacao_cidade, x="Rating", y="City", 
                    title="Avaliação")
col5.plotly_chart(grafico_avaliacao, use_container_width=True)
