import pandas as pd
import logging

def transform_data(data):
    """
    Transforma os dados extraídos:
    - Seleciona colunas relevantes
    - Converte valores de mercado para milhões de dólares
    """
    logging.info("Iniciando transformação de dados...")

    if not data:
        logging.warning("Nenhum dado para transformar.")
        return pd.DataFrame()

    df = pd.DataFrame(data)

    # Seleciona apenas algumas colunas úteis
    df = df[["id", "symbol", "current_price", "market_cap", "total_volume"]]

    # Converte market_cap para milhões de dólares
    df["market_cap_millions"] = df["market_cap"] / 1_000_000

    logging.info(f"Transformação concluída. Registros processados: {len(df)}")
    return df
