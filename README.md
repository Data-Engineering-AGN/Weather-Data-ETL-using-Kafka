# Weather Data ETL Using Kafka

This project simulates a real-time weather data streaming pipeline using Apache Kafka, designed to emulate IoT sensors that continuously transmit weather metrics such as temperature, humidity, and pressure. The architecture is built for scalability, fault tolerance, and parallelism using a multi-node Kafka setup and country-wise topic segmentation. The streamed data is ingested and stored in a PostgreSQL database, forming the foundation for downstream analytics, visualization, or machine learning applications.

---

## Project Overview

- **Producers**: Python-based Kafka producers read from a CSV (simulating real-time sensor data) and send randomized weather updates to country-specific Kafka topics. Each record includes attributes such as temperature, humidity, pressure, timestamp, and country.

- **Kafka Cluster**: A multi-node Kafka setup (configured via Docker Compose) ensures scalable, high-throughput, and fault-tolerant message streaming. Kafka topics are logically divided by country, enabling parallel data pipelines for different regions.

- **Consumers**: Kafka consumers are implemented in Python to subscribe to individual country topics, parse weather data in real time, and persist the data into a PostgreSQL database. Each consumer handles only one country, allowing easy horizontal scaling.

- **PostgreSQL Data Store**: The consumers write structured weather data into country-specific tables in PostgreSQL. This schema is optimized for analytical querying and future integration with BI tools.

- **ETL Pipeline**: Effectively acts as an end-to-end ETL pipeline—from simulated sensor data (Extract), real-time parsing and filtering (Transform), to structured storage in PostgreSQL (Load).

---
## Flowcharts

![image](https://github.com/user-attachments/assets/e857eda1-a07e-491f-a034-0fea54ba62d4)

---

## Technologies Used

- **Apache Kafka**: Real-time distributed streaming platform

- **Docker & Docker Compose**: Containerized deployment of Kafka (multi-node), Zookeeper, and PostgreSQL

- **Python**: Kafka Producers and Consumers (using kafka-python)

- **PostgreSQL**: Relational database to store ingested weather data

- **SQL**: Table creation and query scripts for storage and analysis


---

## Key Features
- Simulated real-time ingestion from weather sensors
- Country-wise topic partitioning for organized streaming
- Multi-node Kafka deployment for reliability and scalability
- PostgreSQL-based persistent storage with country-level schema separation
- Modular ETL architecture suitable for real-time analytics or downstream ML pipelines

---

## Project Structure

```
Weather-Data-ETL-using-Kafka/
│
├── data/
│   └── weather.csv                # Simulated IoT sensor weather data
│
├── server1.yml                    # Docker Compose file for Kafka Node 1
├── server2.yml                    # Docker Compose file for Kafka Node 2
├── server3.yml                    # Docker Compose file for Kafka Node 3
│
├── weather_producer.py           # Python script to simulate weather data producer
├── weather_consumer1.py          # Kafka consumer for selected countries
├── weather_consumer2.py          # Additional Kafka consumer for scaling
│
├── create_postgres_schema.py     # Python script to create PostgreSQL tables
│
├── requirements.txt              # Python dependencies for producer and consumer
├── docker commands.txt           # Useful Docker CLI commands and references
│
├── .gitignore                    # Files/folders to exclude from version control
├── README.md                     # Project documentation
└── .DS_Store                     # (System file, safe to ignore or delete)
```

---

## How It Works

1. **Start Kafka & Postgres** using Docker Compose:
   ```bash
   docker-compose up -d
   ```

2. **Run the producer** to publish data to Kafka topics (based on country):
   ```bash
   python kafka_producer.py
   ```

3. **Run the consumer** to read from Kafka and store data into PostgreSQL:
   ```bash
   python kafka_consumer.py
   ```

---

## Database Schema

PostgreSQL table example:

```
{'MinTemp': 'FLOAT', 'MaxTemp': 'FLOAT', 'Rainfall': 'FLOAT', 'Evaporation': 'FLOAT', 'Sunshine': 'FLOAT', 'WindGustDir': 'TEXT', 'WindGustSpeed': 'FLOAT', 'WindDir9am': 'TEXT', 'WindDir3pm': 'TEXT', 'WindSpeed9am': 'FLOAT', 'WindSpeed3pm': 'INTEGER', 'Humidity9am': 'INTEGER', 'Humidity3pm': 'INTEGER', 'Pressure9am': 'FLOAT', 'Pressure3pm': 'FLOAT', 'Cloud9am': 'INTEGER', 'Cloud3pm': 'INTEGER', 'Temp9am': 'FLOAT', 'Temp3pm': 'FLOAT', 'RainToday': 'TEXT', 'RISK_MM': 'FLOAT', 'RainTomorrow': 'TEXT', 'City': 'TEXT', 'Country': 'TEXT', 'Coordinates': 'TEXT'}
```

---

## Use Case

This project mimics a real-world IoT + big data ETL setup for scenarios like:

- **Agriculture advisory system:** Farmers get alerts based on humidity and rainfall.
- **Smart city traffic/weather routing:** Integrate with traffic simulation data for route planning.
- **Disaster response simulation:** Create a reactive system for storm or flood warnings.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Data-Projects-AGN/Weather-Data-ETL-using-Kafka.git
   cd Weather-Data-ETL-using-Kafka
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Contact

For any questions, feel free to open an issue or reach out via the repository.

**Abhishek Prasanna Walavalkar** (abhishek.walavalkar13@gmail.com)  [**(Linkedin)**](https://www.linkedin.com/in/abhishek-walavalkar-777130147/)

**Gandhar Ravindra Pansare** (gandharpansare@gmail.com)  [**(Linkedin)**](https://www.linkedin.com/in/gandharpansare/)

**Venkat Nikhil Chimata** () [**(Linkedin)**](

---

