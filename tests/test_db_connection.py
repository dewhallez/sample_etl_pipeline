import os
import logging
from utils.db_utils import query_to_df, execute_sql

# Setup logging for test output
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/test_db_connection.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def test_connection_and_query():
    try:
        logging.info("Starting database connection test...")

        # Test read query
        df = query_to_df("SELECT * FROM car_sales LIMIT 3;")
        assert not df.empty, "Query returned no results."
        logging.info(f"Query returned {len(df)} rows:\n{df}")

        # Test write query (non-destructive)
        execute_sql("SELECT 1;")
        logging.info("Successfully executed a test SQL command.")

        print("✅ Database connection and query test passed.")

    except Exception as e:
        logging.error(f"Test failed: {e}")
        print("❌ Database test failed. Check logs for details.")

if __name__ == "__main__":
    test_connection_and_query()
