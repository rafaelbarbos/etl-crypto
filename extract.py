import requests
import logging
import urllib3

def extract_data():
    """
    Extrai dados da API pública CoinGecko sobre preços de criptomoedas.
    """
    logging.info("Iniciando extração de dados...")

    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 5,
        "page": 1,
        "sparkline": "false"
    }
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    response = requests.get(url, params=params, verify=False)

    if response.status_code == 200:
        data = response.json()
        logging.info(f"Extração concluída. Registros obtidos: {len(data)}")
        return data
    else:
        logging.error(f"Erro na extração: {response.status_code}")
        return []
