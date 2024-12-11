#include "Arduino.h"
#include "Arduino_BHY2.h"

// Initialize the BSEC sensor object
SensorBSEC bsec(SENSOR_ID_BSEC);

const unsigned long INTERVAL = 30000; // 30-second interval
const int MAX_READINGS = 120;         // Stop after 120 readings

void setup()
{
  Serial.begin(115200);       // Initialize Serial communication
  while (!Serial);            // Wait for Serial monitor to be ready

  BHY2.begin();               // Initialize the BHY2 sensor hub
  bsec.begin();               // Initialize the BSEC sensor
}

void loop()
{
  static unsigned long lastPrintTime = 0; // Tracks the last time data was printed
  static int readingCount = 0;            // Number of readings taken so far

  // Stop the process after reaching the maximum number of readings
  if (readingCount >= MAX_READINGS) {
    Serial.println("Maximum readings reached. Stopping process.");
    while (true); // Halt execution
  }

  // Continuously update the sensor hub for fresh data
  BHY2.update();

  // Check if the specified interval (30 seconds) has passed since the last reading
  if (millis() - lastPrintTime >= INTERVAL) {
    lastPrintTime = millis(); // Update the last print time
    readingCount++;           // Increment the reading count

    // Output data in CSV format for easier processing later
    Serial.print(readingCount);
    Serial.print(",");
    Serial.println(bsec.toString());
  }
}
