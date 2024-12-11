import serial
import csv
import time
import os

# Name of serial port and baud rate to connect to Arduino IDE serial monitor
SERIAL_PORT = "/dev/cu.usbmodemEBBED8AD2"  # My personal serial port
BAUD_RATE = 115200  # baud rate in the Arduino sketch
CSV_FILE = os.path.expanduser("~/renamethis_data.csv")  # CSV file in the user's directory

# Attempt to open the serial connection to the Arduino
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)  # Timeout ensures non-blocking reads
    print(f"Connected to {SERIAL_PORT} at {BAUD_RATE} baud")
except Exception as e:
    print(f"Error: Could not open serial port {SERIAL_PORT}: {e}")
    exit()

# Open the CSV file for writing data
with open(CSV_FILE, mode='w', newline='') as file:
    csv_writer = csv.writer(file)  # Create a CSV writer object

    # The header row to the CSV file
    csv_writer.writerow(["Timestamp", "Data"])

    print(f"Logging data to {CSV_FILE}. Press Ctrl+C to stop.")

    try:
        while True:
            # Check if there is data available in the serial buffer
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()  # Read and decode a line of data

                # Get the current timestamp
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

                # Write the timestamp and data to the CSV file
                csv_writer.writerow([timestamp, line])

                # Ensures the data is written to disk immediately
                file.flush()

                # Print the logged data to the console for real-time monitoring
                print(f"{timestamp}, {line}")

    except KeyboardInterrupt:
        # Handle user interrupt (Ctrl+C) to stop logging
        print("\nLogging stopped.")
    except Exception as e:
        # Handle unexpected errors during execution
        print(f"An error occurred: {e}")
    finally:
        # Ensure the serial connection is properly closed
        ser.close()
        print(f"Closed serial connection to {SERIAL_PORT}.")
