# 🚀 Projeto ETL - Criptomoedas

## 📌 Objetivo

Este projeto demonstra um pipeline **ETL (Extract, Transform, Load)** em Python, com visualização de dados em **GUI Desktop** e **Dashboard Web**.
O tema escolhido foi o mercado de criptomoedas, usando a **API pública CoinGecko**.

### Etapas:

1. **Extract:** Consome dados de preços das top 5 criptomoedas.
2. **Transform:** Seleciona colunas relevantes e converte `market_cap` para milhões de dólares.
3. **Load:** Salva os dados em:

   * Arquivo `cryptos.csv`
   * Banco de dados SQLite `cryptos.db`
4. **Visualização:**

   * GUI Desktop com **PyQt6** mostrando tabela interativa
   * Dashboard Web com **Streamlit** mostrando tabela e gráficos

---

## 🛠️ Tecnologias Utilizadas

* Python
* Pandas
* Requests
* SQLite (biblioteca padrão do Python)
* **PyQt6** (GUI desktop)
* **Streamlit** (dashboard web)

---

## 📂 Estrutura do Projeto

```
etl-crypto/
│── main.py          # Orquestra a execução do ETL
│── extract.py       # Extração de dados da API
│── transform.py     # Transformação e limpeza dos dados
│── load.py          # Carregamento em CSV e SQLite
│── gui_pyqt.py      # Interface desktop PyQt6
│── app_streamlit.py # Dashboard web Streamlit
│── requirements.txt # Dependências do projeto
│── README.md        # Documentação do projeto
```

---

## ▶️ Como Executar

### 1️⃣ Preparar o ambiente

1. Clone o repositório
2. Crie um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
```

3. Ative o ambiente:

* Windows (PowerShell):

```powershell
.\venv\Scripts\Activate.ps1
```

* Windows (CMD):

```cmd
.\venv\Scripts\activate.bat
```

* Linux / Mac:

```bash
source venv/bin/activate
```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

---

### 2️⃣ Rodar o Pipeline ETL

```bash
python main.py
```

* Gera `cryptos.csv` e `cryptos.db` com os dados tratados
* Logging informa progresso das etapas

---

### 3️⃣ GUI Desktop PyQt6

```bash
python gui_pyqt.py
```

* Abre uma janela com tabela interativa carregando dados do SQLite

---

### 4️⃣ Dashboard Web Streamlit

```bash
python -m streamlit run app_streamlit.py
```

* Abre no navegador uma interface web com tabela e gráficos interativos

---

## 📊 Resultado Esperado

* Arquivo `cryptos.csv` com os dados tratados
* Banco SQLite `cryptos.db` com a tabela `cryptos`
* GUI Desktop PyQt6 mostrando a tabela
* Dashboard Streamlit com tabela e gráficos

Exemplo de saída CSV:

```
id,symbol,current_price,market_cap,total_volume,market_cap_millions
bitcoin,btc,26000,500000000000,10000000000,500000
ethereum,eth,1700,200000000000,5000000000,200000
```

---

## 💡 Diferenciais Técnicos

* Código modular (ETL separado em arquivos)
* Logging para monitorar a execução
* Uso de CSV + banco de dados SQLite
* Interfaces gráficas desktop e web
* Projeto simples, auto-contido e pronto para portfólio de estágio

---

## 📌 Observações

* Para Streamlit: se o comando `streamlit` não for reconhecido, rode:

```bash
python -m streamlit run app_streamlit.py
```

* Para PyQt6: garanta que está instalado via pip (`pip install PyQt6`)
* Projeto testado em Windows 10/11 e Python 3.12+
