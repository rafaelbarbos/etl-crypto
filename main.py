import logging
from extract import extract_data
from transform import transform_data
from load import load_data

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    logging.info("Iniciando pipeline ETL...")

    # ETL pipeline
    raw_data = extract_data()
    transformed_data = transform_data(raw_data)
    load_data(transformed_data)

    logging.info("Pipeline ETL concluído com sucesso!")
