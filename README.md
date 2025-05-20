# Weather Data ETL Using Kafka

This project simulates a real-time weather data streaming pipeline using Apache Kafka, designed to emulate IoT sensors that continuously transmit weather metrics such as temperature, humidity, and pressure. The architecture is built for scalability, fault tolerance, and parallelism using a multi-node Kafka setup and country-wise topic segmentation. The streamed data is ingested and stored in a PostgreSQL database, forming the foundation for downstream analytics, visualization, or machine learning applications.

## Project Overview

- **Producers** simulate weather sensors generating data like temperature, humidity, and pressure for different countries.
- **Multi-node Kafka cluster** ensures scalable and fault-tolerant message streaming.
- **Country-wise Kafka topics** allow organized and parallel data processing.
- **Consumers** listen to respective country topics and store parsed data into a **PostgreSQL data warehouse**.

---
# Flowcharts

![WhatsApp Image 2025-05-20 at 14 17 22_65b61eb3](https://github.com/user-attachments/assets/1004a410-0798-4abd-97dc-c0da61b358ee)

---

## Technologies Used

- Python
- Apache Kafka (multi-node cluster)
- PostgreSQL
- Kafka-Python (Producer & Consumer APIs)
- Docker / Docker Compose (for setting up Kafka and Postgres)


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
weather-data-etl/
│
├── kafka_producer.py          # Simulates weather sensors, sends data to Kafka topics
├── kafka_consumer.py          # Consumes messages and writes them into PostgreSQL
├── weather.csv                # Sample source for simulated data
├── docker-compose.yml         # Spins up multi-node Kafka and Postgres
├── requirements.txt           # Python dependencies
└── README.md
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

```sql
CREATE TABLE weather_data (
    id SERIAL PRIMARY KEY,
    country VARCHAR(50),
    temperature FLOAT,
    humidity FLOAT,
    pressure FLOAT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## Sample Output (Terminal)

### Producer Output
```
Published to topic: weather-india => {"country": "India", "temperature": 32.5, "humidity": 70, "pressure": 1012}
Published to topic: weather-usa => {"country": "USA", "temperature": 24.3, "humidity": 60, "pressure": 1015}
```

### Consumer Output
```
Received: {'country': 'India', 'temperature': 32.5, 'humidity': 70, 'pressure': 1012}
Inserted into PostgreSQL: India | 32.5°C | 70% | 1012 hPa
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

