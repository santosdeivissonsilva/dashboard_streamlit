import streamlit as st
import pandas as pd

st.set_page_config(page_title="Streamlit Dados")

with st.container():
    st.title('Dashboard de Contratos')
    st.write('Informações sobre os contratos fechados ao longo de Maio/2023')


@st.cache_data
def carregar_dados():  # Função utilizada para carregar dados
    tabela = pd.read_csv('resultados.csv')
    return tabela


with st.container():
    st.write('---')
    quant_dias = st.selectbox('Selecione um período', [
                              "7D", "15D", "30D"])
    num_dias = int(quant_dias.replace("D", ""))
    dados = carregar_dados()
    dados = dados[-num_dias:]
    st.area_chart(dados, x="Data", y="Contratos")
