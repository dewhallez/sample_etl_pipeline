import pandas as pd
from faker import Faker
import random, uuid, os, logging

# Setup logging
os.makedirs("logs", exist_ok=True)
logging.basicConfig(filename='logs/generate_data.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_data(n=100000):
    fake = Faker()
    car_makes = ['Toyota', 'Ford', 'Honda', 'Chevrolet', 'BMW', 'Mercedes-Benz', 'Audi', 'Volkswagen', 'Hyundai', 'Nissan', 'Kia', 'Subaru', 'Mazda', 'Lexus', 'Tesla']
    models = {
        'Toyota': ['Camry', 'Corolla', 'RAV4', 'Prius', 'Highlander', 'Tacoma', 'Tundra', 'Sienna', '4Runner', 'Avalon'],
        'Ford': ['F-150', 'Focus', 'Mustang', 'Explorer', 'Escape', 'Edge', 'Fusion', 'Ranger', 'Bronco', 'Transit'],
        'Honda': ['Civic', 'Accord', 'CR-V', 'Pilot', 'Fit', 'HR-V', 'Odyssey', 'Ridgeline', 'Insight', 'Passport'],
        'Chevrolet': ['Malibu', 'Impala', 'Equinox', 'Traverse', 'Silverado', 'Colorado', 'Camaro', 'Tahoe', 'Suburban', 'Bolt'],
        'BMW': ['X5', '3 Series', '5 Series', 'X3', 'X1', '7 Series', 'X6', 'Z4', 'M3', 'M5'],
        'Mercedes-Benz': ['C-Class', 'E-Class', 'S-Class', 'GLC', 'GLE', 'A-Class', 'B-Class', 'G-Class', 'CLA', 'GLA'],
        'Audi': ['A4', 'A6', 'Q5', 'Q7', 'A3', 'A8', 'Q3', 'TT', 'R8', 'S5'],
        'Volkswagen': ['Golf', 'Passat', 'Tiguan', 'Jetta', 'Atlas', 'Beetle', 'Polo', 'Arteon', 'ID.4', 'Touareg'],
        'Hyundai': ['Elantra', 'Sonata', 'Tucson', 'Santa Fe', 'Kona', 'Palisade', 'Accent', 'Veloster', 'Ioniq', 'Nexo'],
        'Nissan': ['Altima', 'Sentra', 'Rogue', 'Murano', 'Pathfinder', 'Frontier', 'Titan', 'Leaf', 'Maxima', 'Versa'],
        'Kia': ['Optima', 'Sorento', 'Sportage', 'Soul', 'Telluride', 'Forte', 'Stinger', 'Niro', 'Seltos', 'Cadenza'],
        'Subaru': ['Outback', 'Forester', 'Impreza', 'Crosstrek', 'Ascent', 'Legacy', 'WRX', 'BRZ', 'XV', 'Tribeca'],
        'Mazda': ['Mazda3', 'Mazda6', 'CX-5', 'CX-9', 'MX-5 Miata', 'CX-3', 'CX-30', 'RX-8', '6', '5'],
        'Lexus': ['RX', 'ES', 'IS', 'NX', 'GX', 'LS', 'UX', 'LC', 'RC', 'LX'],
        'Tesla': ['Model S', 'Model 3', 'Model X', 'Model Y', 'Cybertruck', 'Roadster', 'Semi', 'Powerwall', 'Solar Roof', 'Energy Storage']
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
