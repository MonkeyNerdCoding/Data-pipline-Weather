import psycopg2
from api_request import mock_fetch_data

print(mock_fetch_data())

def connect_to_db():
    print("Connecting to the Postgres database...")
    try: 
        conn = psycopg2.connect(
            host="localhost",
            port=5000,
            dbname ="db",
            user="db_user",
            password="db_password"
        )
        print(conn)
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        raise

def create_table(conn):
    print("Creating weather_data table if not exists...")
    try:
        cursor = conn.cursor()
        create_table_query = '''
        CREATE SCHEMA IF NOT EXISTS weather;
        CREATE TABLE IF NOT EXISTS weather.raw_weather_data (
            id SERIAL PRIMARY KEY,
            city TEXT,
            temperature FLOAT,
            weather_description TEXT,
            wind_speed FLOAT,
            time TIMESTAMP,
            inserted_at TIMESTAMP DEFAULT NOW(),
            utc_offset TEXT
        );
        '''
        cursor.execute(create_table_query)
        conn.commit()
        cursor.close()
        print("Table created successfully or already exists.")
    except psycopg2.Error as e:
        print(f"Error creating table: {e}")
        raise
    



def insert_record(conn, data):
    print("Inserting record into weather_data table...")
    try:
        cursor = conn.cursor()
        insert_query = '''
        INSERT INTO weather.raw_weather_data (city, temperature, weather_description, wind_speed, time, utc_offset)
        VALUES (%s, %s, %s, %s, %s, %s);
        '''
        cursor.execute(insert_query, (
            data['location']['name'],
            data['current']['temperature'],
            data['current']['weather_descriptions'][0],
            data['current']['wind_speed'],
            data['location']['localtime'],
            data['location']['utc_offset']
        ))
        conn.commit()
        cursor.close()
        print("Record inserted successfully.")
    except psycopg2.Error as e:
        print(f"Error inserting record: {e}")
        raise

def main(): 
    try:
        data = mock_fetch_data()
        conn = connect_to_db()
        create_table(conn)
        insert_record(conn, data)
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
            print("Database connection closed.")

main()