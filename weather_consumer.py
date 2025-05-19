from kafka import KafkaConsumer
import json
import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="weatherDataDB",
    user="admin",
    password="admin",
    host="10.20.144.28",
    port="5432"
)
cursor = conn.cursor()

topics_list = ["australia_weather", "turkey_weather", "south_africa_weather"]
consumer = KafkaConsumer(
    *topics_list,
    bootstrap_servers='10.20.31.246:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Subscribe to all topics that start with 'weather-'
#consumer.subscribe(pattern='^.*_weather$')

# Define mapping between country and table name
country_table_map = {
    'Australia': 'weather_australia',
    'Turkey': 'weather_turkey',
    'South Africa': 'weather_south_africa',
   'USA': 'weather_usa',
    'Spain': 'weather_spain'
}

# Columns in the schema (same for all tables)
columns = [
    'MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine',
    'WindGustDir', 'WindGustSpeed', 'WindDir9am', 'WindDir3pm',
    'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm',
    'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm', 'Temp9am', 'Temp3pm',
    'RainToday', 'RISK_MM', 'RainTomorrow', 'City', 'Country', 'Coordinates'
]

for message in consumer:
    topic = message.topic                 
    data = message.value                   
    country = data.get("Country")  
    table_name = country_table_map[country]

    # Ensure all columns exist, even if missing in data
    values = [data.get(col) for col in columns]

    placeholders = ','.join(['%s'] * len(columns))
    col_str = ','.join(columns)

    insert_query = f"""
        INSERT INTO {table_name} ({col_str})
        VALUES ({placeholders})
    """

    try:
        cursor.execute(insert_query, values)
        conn.commit()
        print(f"Inserted into [{table_name}]:",data)
    except Exception as e:
        conn.rollback()
        print(f"Error inserting into [{table_name}]:", e, "\nData:",data)