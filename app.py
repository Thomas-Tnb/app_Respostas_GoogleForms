import streamlit as st  
import pandas as pd

# Acessando a planilha
url = "https://docs.google.com/spreadsheets/d/1JEsn8iuQw4bXJ4wC1QFsq74GBGQfFz5-Fj9dpIRj4lo/export?format=csv"


# Convertendo para dataframe
df = pd.read_csv(url)

# Faixa etária 
if 20 < df["Idade"] <= 35:
    df["Faixa Etária"] = "Entre 20 e 35 anos"
elif 35 < df["Idade"] <= 50:
    df["Faixa Etária"] = "Entre 35 e 50 anos"
else:
    df["Faixa Etária"] = "Mais que 50 anos"

# Criando Dashboard no Streamlit
st.title("Dashboard Shopfono")
st.write("Dados extraídos do google sheets :")
st.dataframe(df)


st.bar_chart(df["Faixa Etária"])