from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[1]").appName("Test").getOrCreate()

def test_clean_data_edge_cases():
    data = [
        ("1", "Toyota", "Camry", 2020, 0, "2023-01-01", "Alice", "New York"),
        ("2", "Ford", "Focus", 2019, -1000, "2022-01-01", "Bob", "Chicago"),
        ("3", None, "Civic", 2021, 15000, "2023-01-01", "Carol", "LA"),
        ("4", "BMW", "X5", 2022, 40000, "2023-01-01", "Dave", "Miami")
    ]
    columns = ["sale_id", "car_make", "car_model", "year", "price", "sale_date", "customer_name", "dealer_location"]
    df = spark.createDataFrame(data, columns)
    df_clean = df.dropna().filter(df.price > 0)
    assert df_clean.count() == 1
