import os
import logging
from utils.db_utils import query_to_df

# Setup logging
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/query_car_sales.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    try:
        logging.info("Starting query_car_sales script...")

        # Example query: get top 10 most expensive car sales
        query = """
        SELECT car_make, car_model, year, price, sale_date
        FROM car_sales
        ORDER BY price DESC
        LIMIT 10;
        """

        df = query_to_df(query)
        logging.info(f"Retrieved {len(df)} rows.")
        print(df)

        # Optionally export to CSV
        output_path = "data/query_results/top_10_expensive_sales.csv"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, index=False)
        logging.info(f"Results saved to {output_path}")

    except Exception as e:
        logging.error(f"Error in query_car_sales: {e}")
        print("❌ Failed to query car sales data. Check logs for details.")

if __name__ == "__main__":
    main()
