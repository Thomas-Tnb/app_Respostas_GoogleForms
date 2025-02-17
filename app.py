import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração da página
st.set_page_config(page_title="Dashboard Shopfono", layout="wide")

# Acessando a planilha
url = "https://docs.google.com/spreadsheets/d/1JEsn8iuQw4bXJ4wC1QFsq74GBGQfFz5-Fj9dpIRj4lo/export?format=csv"
df = pd.read_csv(url)

# Tratamentos básicos 
df = df.drop(columns=["Coluna 19", "Coluna 20", "Coluna 21"], errors='ignore')

# Função para definir a faixa etária
def definir_faixa_etaria(idade):
    if 20 < idade <= 35:
        return "Entre 20 e 35 anos"
    elif 35 < idade <= 50:
        return "Entre 35 e 50 anos"
    else:
        return "Mais que 50 anos"

if "Idade" in df.columns:
    df["Faixa Etária"] = df["Idade"].apply(definir_faixa_etaria)

# Criando Dashboard no Streamlit
st.title("Dashboard Shopfono")
st.write("Dados extraídos do Google Sheets:")
st.dataframe(df.head())

# Gráfico de distribuição etária
st.subheader("Distribuição por Faixa Etária")
if "Faixa Etária" in df.columns:
    fig, ax = plt.subplots()
    sns.countplot(x="Faixa Etária", data=df, palette="viridis", ax=ax)
    st.pyplot(fig)
else:
    st.write("Coluna de idade não encontrada no conjunto de dados.")

# Pergunta específica do formulário
st.subheader("Respostas de uma Pergunta Específica")
pergunta = st.selectbox("Escolha uma pergunta para analisar:", df.columns[1:])
fig2, ax2 = plt.subplots()
sns.countplot(y=df[pergunta], order=df[pergunta].value_counts().index, palette="magma", ax=ax2)
st.pyplot(fig2)
