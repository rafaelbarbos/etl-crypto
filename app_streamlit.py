import streamlit as st
import pandas as pd
import sqlite3

st.title("Dashboard de Criptomoedas")

# Conectar ao banco SQLite e carregar dados
conn = sqlite3.connect("cryptos.db")
df = pd.read_sql("SELECT * FROM cryptos", conn)
conn.close()

# Mostrar tabela interativa
st.dataframe(df)

# Filtro de criptomoeda por market cap
min_cap = st.slider("Market Cap mínimo (milhões USD)", 0, int(df["market_cap_millions"].max()), 0)
st.dataframe(df[df["market_cap_millions"] >= min_cap])
