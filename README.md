# 🚗 Car Sales Data Pipeline

[![CI/CD](https://github.com/dewhallez/sample_etl_pipeline/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/dewhallez/sample_etl_pipeline/actions/workflows/ci-cd.yml)
[![Dockerized](https://img.shields.io/badge/docker-ready-blue?logo=docker)](https://www.docker.com/)
[![Airflow](https://img.shields.io/badge/airflow-2.8.1-blue?logo=apache-airflow)](https://airflow.apache.org/)
[![Spark](https://img.shields.io/badge/spark-3.5-orange?logo=apache-spark)](https://spark.apache.org/)
[![PostgresSQL](https://img.shields.io/badge/postgres-14-blue?logo=postgresql)](https://www.postgresql.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.10-blue?logo=python)](https://www.python.org/)
[![Code Style](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)

> A modern data engineering pipeline that processes car sales data using industry-standard tools. Built with Apache Spark for robust data processing, PostgreSQL for reliable storage, and Apache Airflow for workflow orchestration. Features comprehensive testing, CI/CD automation, and containerized deployment.

## 📋 Table of Contents
- [Features](#-features)
- [Prerequisites](#️-getting-started)
- [Getting Started](#️-getting-started)
- [Project Structure](#️-project-structure)
- [Data Pipeline](#-data-pipeline-flow)
- [Development](#-development)
- [Testing](#-testing)
- [Deployment](#-deployment)
- [Contributing](#-contributing)

---

## 📦 Features

- 🧪 **Data Generation**
  - Generate realistic car sales data using Faker
  - Configurable data volume and characteristics
  - Automated data quality validation
  
- 🧼 **Data Processing**
  - PySpark-powered data cleaning and transformation
  - Efficient large-scale data processing
  - Schema validation and data type enforcement
  
- 🐘 **Data Storage**
  - PostgreSQL database with optimized schema
  - Efficient bulk loading capabilities
  - Data versioning and archival
  
- 🛰 **Workflow Orchestration**
  - Airflow DAGs with retry mechanisms
  - Dependency management and scheduling
  - Task monitoring and alerting
  
- 🐳 **Infrastructure**
  - Complete Docker containerization
  - Multi-service orchestration with Docker Compose
  - Consistent dev/prod environments
  
- ✅ **Quality Assurance**
  - Comprehensive unit and integration tests
  - Automated CI/CD with GitHub Actions
  - Code quality checks with black and flake8

---

## 🛠️ Getting Started

### Prerequisites

- Docker Desktop 4.x+ ([Install](https://docs.docker.com/get-docker/))
- Python 3.10+ ([Install](https://www.python.org/downloads/))
- Git ([Install](https://git-scm.com/downloads))
- 8GB RAM minimum
- 20GB free disk space

### Quick Start

1. **Clone Repository**
```bash
git clone https://github.com/dewhallez/sample_etl_pipeline
cd sample_etl_pipeline
```

2. **Configure Environment**

```bash
# Setup Python environment
python -m venv venv
.\venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac
python -m pip install --upgrade pip
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env     # Copy example config
```

3. **Start Services**

```bash
# Launch services
docker-compose up -d

# Verify deployment
docker-compose ps
docker-compose logs -f airflow-webserver
```

4. **Access Services**

- Airflow UI: http://localhost:8080 
  - Username: `airflow`
  - Password: `airflow`
- Spark UI: http://localhost:4040
- PostgreSQL: localhost:5432

## 💻 Development

### Local Testing
```bash
# Run all tests
pytest tests/

# Run with coverage
pytest --cov=scripts tests/

# Check code style
black .
flake8 .
```

### Running Pipeline Components
```bash
# Generate sample data
python scripts/generate_data.py --rows 1000

# Process with Spark
python scripts/clean_data.py --input data/raw/sales.csv

# Load to database
python scripts/load_to_db.py --file data/processed/sales_cleaned.csv
```

---

## 🏗️ Project Structure

```
sample_etl_pipeline/
├── dags/                  # Airflow DAG definitions
│   └── car_sales.py      # Main pipeline DAG
├── data/                  # Data storage and artifacts
│   ├── raw/              # Raw generated data
│   ├── processed/        # Cleaned data
│   └── archived/         # Historical data
├── scripts/              # Core ETL logic
│   ├── generate_data.py  # Data simulation
│   ├── clean_data.py     # PySpark transformations
│   ├── load_to_db.py     # Database operations
│   └── query_db.py       # Data validation
├── tests/                # Automated tests
│   ├── test_generate_data.py
│   ├── test_clean_data.py
│   ├── test_load_to_db.py
│   └── test_db_connection.py
├── utils/                # Shared utilities
│   └── db_utils.py       # Database helpers
├── docker/               # Container configurations
│   ├── Dockerfile.airflow
│   └── init.sql         # Database initialization
├── Dockerfile.spark      # Spark processing environment
├── docker-compose.yml    # Service definitions
├── requirements.txt      # Python dependencies
└── Makefile             # Build automation
```

---

## 📊 Data Pipeline Flow

1. **Data Generation**
   - Generate synthetic car sales data using Faker
   - Validate data quality and completeness
   - Save raw data to CSV format

2. **Data Processing**
   - Load raw data into Spark DataFrame
   - Clean and standardize data fields
   - Apply business rules and transformations
   - Validate processed data quality

3. **Data Storage**
   - Initialize PostgreSQL database
   - Load processed data in batches
   - Verify data integrity
   - Archive historical data

4. **Workflow Orchestration**
   - Schedule pipeline execution with Airflow
   - Monitor task status and dependencies
   - Handle failures and retries
   - Alert on pipeline completion/failure

## 🔍 Monitoring

### Health Checks
- Airflow: http://localhost:8080/health
- PostgreSQL: http://localhost:5432/health
- Spark: http://localhost:4040

### Logging
```bash
# View service logs
docker-compose logs -f airflow-webserver  # Airflow logs
docker-compose logs -f postgres           # Database logs
docker-compose logs -f spark             # Spark logs
```

## 👥 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Run tests (`pytest tests/`)
4. Commit changes (`git commit -m 'Add amazing feature'`)
5. Push to branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📫 Contact & Support

- Maintainer: [@dewhallez](https://github.com/dewhallez)
- Issues: [GitHub Issues](https://github.com/dewhallez/sample_etl_pipeline/issues)
- Discussions: [GitHub Discussions](https://github.com/dewhallez/sample_etl_pipeline/discussions)
3. **Loading**: Store results in PostgreSQL
4. **Orchestration**: Manage workflow with Airflow

---

## 🔧 Configuration

Environment variables can be set in `.env`:

```env
DB_USER=your_user
DB_PASS=your_password
DB_NAME=carsales
DB_PORT=5432
```

---

## 🚀 Airflow UI Access

- URL: `http://localhost:8080`
- Default credentials:
  - Username: `airflow`
  - Password: `airflow`

---

## 📈 Monitoring & Logging

- Airflow logs: `logs/airflow/`
- Application logs: `logs/app/`
- PostgreSQL logs: `logs/postgres/`

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📫 Contact

- Author: Your Name
- GitHub: [@dewhallez](https://github.com/dewhallez)