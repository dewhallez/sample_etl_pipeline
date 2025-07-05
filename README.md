# 🚗 Car Sales Data Pipeline

[![CI/CD](https://github.com/dewhallez/sample_etl_pipeline/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/dewhallez/sample_etl_pipeline/actions/workflows/ci-cd.yml)
[![Dockerized](https://img.shields.io/badge/docker-ready-blue?logo=docker)](https://www.docker.com/)
[![Airflow](https://img.shields.io/badge/airflow-2.8.1-blue?logo=apache-airflow)](https://airflow.apache.org/)
[![Spark](https://img.shields.io/badge/spark-3.5-orange?logo=apache-spark)](https://spark.apache.org/)
[![PostgresSQL](https://img.shields.io/badge/postgres-14-blue?logo=postgresql)](https://www.postgresql.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

> End-to-end data engineering pipeline that simulates car sales data, cleans it with PySpark, stores it in PostgresSQL, and orchestrates the workflow using Apache Airflow. Includes CI/CD with GitHub Actions and full Docker support.

---

## 📦 Features

- 🧪 **Data Generation**: Create realistic dummy car sales data with Faker
- 🧼 **Data Cleaning**: Use PySpark to clean and transform data
- 🐘 **PostgresSQL Storage**: Load cleaned data into a relational database
- 🛰 **Airflow DAG**: Orchestrate the pipeline with Apache Airflow
- 🐳 **Dockerized Stack**: Run everything locally with Docker Compose
- ✅ **Unit Testing**: Validate logic and edge cases with `pytest`
- 🚀 **CI/CD**: GitHub Actions pipeline for testing and deployment

---

## 🛠️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/dewhallez/sample_etl_pipeline
cd sample_etl_pipeline
