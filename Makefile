# Project Makefile for Car Sales Data Pipeline

# Paths
COMPOSE=docker-compose -f docker/docker-compose.yml

# 🐳 Docker Commands
build:
    $(COMPOSE) build

up:
    $(COMPOSE) up --build

down:
    $(COMPOSE) down

reset:
    $(COMPOSE) down -v
    $(COMPOSE) up --build

logs:
    $(COMPOSE) logs -f

# 🧪 Run Pipeline Manually
run:
    python scripts/generate_data.py && \
    docker exec -it car-sales-data-pipeline_spark_1 spark-submit /app/scripts/clean_data.py && \
    python scripts/load_to_postgres.py

# ✅ Testing
test:
    pytest tests/

# 🧼 Clean Data and Logs
clean:
    rm -rf data/raw/*
    rm -rf data/processed/*
    rm -rf logs/*

# 🧭 Airflow Access Info
info:
    @echo "Airflow UI: http://localhost:8080"
    @echo "Username: admin"
    @echo "Password: admin"

# usage examples
# make build       # Build all services
# make up          # Start the stack
# make down        # Stop the stack
# make reset       # Rebuild and reset everything
# make run         # Run the pipeline manually
# make test        # Run unit tests
# make clean       # Clean data and logs
# make info        # Show Airflow login info
