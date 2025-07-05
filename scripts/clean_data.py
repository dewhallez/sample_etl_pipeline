from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import os
import logging

# Setup logging
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/clean_data.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

INPUT_PATH = "/opt/bitnami/spark/data/raw/car_sales.csv"
OUTPUT_PATH = "/opt/bitnami/spark/data/processed/car_sales_cleaned.parquet"

def clean_data():
    try:
        logging.info("Starting Spark session for data cleaning.")
        spark = SparkSession.builder.appName("CleanCarSalesData").getOrCreate()

        logging.info(f"Reading raw data from: {INPUT_PATH}")
        df = spark.read.option("header", True).csv(INPUT_PATH)

        logging.info("Cleaning data: dropping nulls and filtering invalid prices.")
        df_cleaned = (
            df.dropna()
              .filter(col("price").cast("double") > 0)
              .withColumn("year", col("year").cast("int"))
              .withColumn("price", col("price").cast("double"))
        )

        os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
        logging.info(f"Writing cleaned data to: {OUTPUT_PATH}")
        df_cleaned.write.mode("overwrite").parquet(OUTPUT_PATH)

        logging.info("Data cleaning completed successfully.")
        spark.stop()

    except Exception as e:
        logging.error(f"Error during data cleaning: {e}")
        raise

if __name__ == "__main__":
    clean_data()

