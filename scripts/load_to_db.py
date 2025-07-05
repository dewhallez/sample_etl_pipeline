import os
import logging
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Setup logging
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/load_to_postgres.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Load environment variables
load_dotenv()

DB_USER = os.getenv("DB_USER", "airflow")
DB_PASS = os.getenv("DB_PASS", "airflow")
DB_NAME = os.getenv("DB_NAME", "carsales")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_HOST = os.getenv("DB_HOST", "postgres")

INPUT_PATH = "/opt/airflow/data/processed/car_sales_cleaned.parquet"

def load_data():
    try:
        logging.info(f"Reading cleaned data from: {INPUT_PATH}")
        df = pd.read_parquet(INPUT_PATH)

        conn_str = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        engine = create_engine(conn_str)

        logging.info("Loading data into PostgresSQL table: car_sales")
        df.to_sql("car_sales", engine, if_exists="replace", index=False)

        logging.info("Data successfully loaded into PostgresSQL.")

    except Exception as e:
        logging.error(f"Error loading data into PostgresSQL: {e}")
        raise

if __name__ == "__main__":
    load_data()
