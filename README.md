# Weather Data ETL Using Kafka

This project simulates real-time weather data transmission using Apache Kafka, emulating IoT sensors sending continuous updates. A multi-node Kafka setup streams data into country-wise topics, and consumers ingest and store the data into a PostgreSQL database for downstream analytics and reporting.

## 🚀 Project Overview

- **Producers** simulate weather sensors generating data like temperature, humidity, and pressure for different countries.
- **Multi-node Kafka cluster** ensures scalable and fault-tolerant message streaming.
- **Country-wise Kafka topics** allow organized and parallel data processing.
- **Consumers** listen to respective country topics and store parsed data into a **PostgreSQL data warehouse**.

---

## 🛠️ Technologies Used

- Python
- Apache Kafka (multi-node cluster)
- PostgreSQL
- Kafka-Python (Producer & Consumer APIs)
- Docker / Docker Compose (for setting up Kafka and Postgres)

---

## 📁 Project Structure

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

## 🧪 How It Works

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

## 🗃️ Database Schema

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

## 📸 Sample Output (Terminal)

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

## 📌 Use Case

This project mimics a real-world IoT + big data ETL setup for scenarios like:

- Weather monitoring systems
- Smart city dashboards
- Real-time analytics pipelines
- Data warehousing for climate data

---

## 📦 Installation

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

## 📞 Contact

For any questions, feel free to open an issue or reach out via the repository.

Venkat Nikhil Chimata

---

## 📌 Screenshots

_(Leave space to insert screenshots later if needed)_
