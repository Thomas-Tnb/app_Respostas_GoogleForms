import streamlit as st  
import pandas as pd


# Acessando a planilha
url = "https://docs.google.com/spreadsheets/d/1JEsn8iuQw4bXJ4wC1QFsq74GBGQfFz5-Fj9dpIRj4lo/export?format=csv"


# Convertendo para dataframe
df = pd.read_csv(url)

# Criando Dashboard no Streamlit
st.title("Dashboard Shopfono")
st.write("Dados extraídos do google sheets :")
st.dataframe(df)

# Estatísticas básicas
st.subheader("Resumo Estatístico")
st.write(df.describe())
