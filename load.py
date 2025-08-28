import pandas as pd
import sqlite3
import logging

def load_data(df, csv_path="cryptos.csv", db_path="cryptos.db"):
    """
    Carrega os dados transformados em:
    - Arquivo CSV
    - Banco de dados SQLite
    """
    if df.empty:
        logging.warning("Nenhum dado para carregar.")
        return

    logging.info("Carregando dados...")

    # Salva em CSV
    df.to_csv(csv_path, index=False)
    logging.info(f"Dados salvos em {csv_path}")

    # Salva em SQLite
    conn = sqlite3.connect(db_path)
    df.to_sql("cryptos", conn, if_exists="replace", index=False)
    conn.close()
    logging.info(f"Dados salvos no banco SQLite: {db_path}")
