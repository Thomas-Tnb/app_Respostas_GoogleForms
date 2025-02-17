import streamlit as st  
import pandas as pd

# Acessando a planilha
url = "https://docs.google.com/spreadsheets/d/1JEsn8iuQw4bXJ4wC1QFsq74GBGQfFz5-Fj9dpIRj4lo/export?format=csv"


# Convertendo para dataframe
df = pd.read_csv(url)

# Função para definir a faixa etária
def definir_faixa_etaria(idade):
    if 20 < idade <= 35:
        return "Entre 20 e 35 anos"
    elif 35 < idade <= 50:
        return "Entre 35 e 50 anos"
    else:
        return "Mais que 50 anos"

df["Faixa Etária"] = df["Idade"].apply(definir_faixa_etaria)

# Criando Dashboard no Streamlit
st.title("Dashboard Shopfono")
st.write("Dados extraídos do google sheets :")
st.dataframe(df)


st.bar_chart(df["Faixa Etária"])