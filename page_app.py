import streamlit as st
import pandas as pd

st.set_page_config(page_title="Streamlit Dados")

with st.container():
    st.title('Dashboard de Contratos')
    st.write('Informações sobre os contratos fechados ao longo de Maio/2023')

with st.container():
    st.write('---')
    dados = pd.read_csv("resultados.csv")
    st.area_chart(dados, x="Data", y="Contratos")
