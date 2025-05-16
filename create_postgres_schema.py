import pandas as pd
import psycopg2

# Load weather.csv
df = pd.read_csv("./data/weather.csv")

# Preview schema
print("Columns:", df.columns)

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="10.20.144.28",
    port=5432,
    dbname="weatherDataDB",
    user="admin",
    password="admin"
)
cursor = conn.cursor()

# Choose 5 countries
if 'Country' not in df.columns:
    raise ValueError("The CSV must contain a 'country' column.")

countries = df['Country'].dropna().unique()[:5]

# Convert Pandas dtypes to PostgreSQL types
def map_dtype(dtype):
    if pd.api.types.is_integer_dtype(dtype):
        return "INTEGER"
    elif pd.api.types.is_float_dtype(dtype):
        return "FLOAT"
    elif pd.api.types.is_datetime64_any_dtype(dtype):
        return "TIMESTAMP"
    else:
        return "TEXT"

schema = {col: map_dtype(dtype) for col, dtype in df.dtypes.items()}

# Create tables
for country in countries:
    table_name = f"weather_{country.lower().replace(' ', '_')}"
    columns_sql = ", ".join([f"{col} {dtype}" for col, dtype in schema.items()])
    create_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_sql});"
    
    cursor.execute(create_sql)
    print(f"Created table: {table_name}")

# Commit and close
conn.commit()
cursor.close()
conn.close()
