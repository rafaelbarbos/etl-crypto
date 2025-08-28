# 🚀 Projeto ETL - Criptomoedas

## 📌 Objetivo
Este projeto demonstra um pipeline **ETL (Extract, Transform, Load)** em Python.  
O tema escolhido foi o mercado de criptomoedas, usando a **API pública CoinGecko**.

- **Extract:** Consome dados de preços das top 5 criptomoedas.
- **Transform:** Seleciona colunas relevantes e converte `market_cap` para milhões de dólares.
- **Load:** Salva os dados em:
  - Arquivo `cryptos.csv`
  - Banco de dados SQLite `cryptos.db`

---

## 🛠️ Tecnologias Utilizadas
- Python
- Pandas
- Requests
- SQLite (biblioteca padrão do Python)

---

## 📂 Estrutura do Projeto
```
etl-crypto/
│── main.py          # Orquestra a execução do ETL
│── extract.py       # Extração de dados da API
│── transform.py     # Transformação e limpeza dos dados
│── load.py          # Carregamento em CSV e SQLite
│── requirements.txt # Dependências do projeto
│── README.md        # Documentação do projeto
```

---

## ▶️ Como Executar
1. Clone este repositório
2. Crie um ambiente virtual (opcional, mas recomendado)
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute o pipeline:
   ```bash
   python main.py
   ```

---

## 📊 Resultado Esperado
Após a execução:
- Um arquivo `cryptos.csv` será criado com os dados tratados
- Um banco SQLite `cryptos.db` conterá a tabela `cryptos`

Exemplo de saída no CSV:
```
id,symbol,current_price,market_cap,total_volume,market_cap_millions
bitcoin,btc,26000,500000000000,10000000000,500000
ethereum,eth,1700,200000000000,5000000000,200000
```

---

## 💡 Diferenciais Técnicos
- Código modular (separação clara entre ETL)
- Logging para monitorar a execução
- Uso de banco de dados + CSV
- Projeto simples e auto-contido, ideal para portfólio de estágio
