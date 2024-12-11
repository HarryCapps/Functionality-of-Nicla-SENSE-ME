import sqlite3

conn = sqlite3.connect('gyro_data.db')  # Connect to the database

cursor = conn.cursor()  # Create a cursor object to execute SQL queries

# Create gyroscope data table
cursor.execute('''
CREATE TABLE IF NOT EXISTS gyroscope_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    gyro_x REAL,
    gyro_y REAL,
    gyro_z REAL
)
''')

conn.commit()
conn.close()
