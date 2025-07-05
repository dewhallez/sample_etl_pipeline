import os
import logging
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Setup logging
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/db_utils.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_engine():
    """Create a SQLAlchemy engine using environment variables."""
    try:
        DB_USER = os.getenv("DB_USER", "user")
        DB_PASS = os.getenv("DB_PASS", "password")
        DB_NAME = os.getenv("DB_NAME", "carsales")
        DB_HOST = os.getenv("DB_HOST", "localhost")
        DB_PORT = os.getenv("DB_PORT", "5432")

        conn_str = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        engine = create_engine(conn_str)
        logging.info("Successfully created database engine.")
        return engine
    except Exception as e:
        logging.error(f"Error creating database engine: {e}")
        raise

def query_to_df(query: str) -> pd.DataFrame:
    """Execute a SQL query and return the result as a DataFrame."""
    try:
        engine = get_engine()
        with engine.connect() as conn:
            df = pd.read_sql(text(query), conn)
            logging.info(f"Successfully executed query: {query}")
            return df
    except Exception as e:
        logging.error(f"Error executing query: {e}")
        raise

def execute_sql(query: str):
    """Execute a SQL command (INSERT, UPDATE, DELETE, etc.)."""
    try:
        engine = get_engine()
        with engine.begin() as conn:
            conn.execute(text(query))
            logging.info(f"Successfully executed SQL command: {query}")
    except Exception as e:
        logging.error(f"Error executing SQL command: {e}")
        raise
