import pandas as pd
from faker import Faker
import random, uuid, os, logging

# Setup logging
os.makedirs("logs", exist_ok=True)
logging.basicConfig(filename='logs/generate_data.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_data(n=100000):
    fake = Faker()
    car_makes = ['Toyota', 'Ford', 'Honda', 'Chevrolet', 'BMW']
    models = {
        'Toyota': ['Camry', 'Corolla'],
        'Ford': ['F-150', 'Focus'],
        'Honda': ['Civic', 'Accord'],
        'Chevrolet': ['Malibu', 'Impala'],
        'BMW': ['X5', '3 Series']
    }

    data = []
    for _ in range(n):
        make = random.choice(car_makes)
        model = random.choice(models[make])
        data.append({
            'sale_id': str(uuid.uuid4()),
            'agent_id': random.randint(1, 250),
            'car_make': make,
            'car_model': model,
            'year': random.randint(2000, 2025),
            'price': round(random.uniform(5000, 50000), 2),
            'sale_date': fake.date_between(start_date='-2y', end_date='today'),
            'customer_name': fake.name(),
            'dealer_location': fake.city()
        })
    return pd.DataFrame(data)

if __name__ == "__main__":
    try:
        output_path = "/opt/airflow/data/raw/car_sales.csv"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        #os.makedirs("data/raw", exist_ok=True)
        df = generate_data()
        df.to_csv(output_path, index=False)
        #df.to_csv("data/raw/car_sales.csv", index=False)
        logging.info(f"Successfully saved data to {output_path}")
        #logging.info("Successfully generated and saved dummy car sales data.")
    except Exception as e:
        logging.error(f"Error generating data: {e}")
