#include <ArduinoBLE.h>

const int maxDevices = 50;  // Maximum number of devices to track
struct DeviceInfo {
  String address;
  String name;
  int rssi;
};

DeviceInfo detectedDevices[maxDevices];  // Array to store device information
int deviceCount = 0;

const unsigned long scanInterval = 30000;  // Scan every 30 seconds
const unsigned long summaryInterval = 300000;  // Provide a summary every 5 minutes
const unsigned long totalRunTime = 3600000;  // Run for 1 hour

unsigned long lastScanTime = 0;
unsigned long lastSummaryTime = 0;
unsigned long startTime = 0;

// Add a new device or update an existing one
void addDevice(String address, String name, int rssi) {
  for (int i = 0; i < deviceCount; i++) {
    if (detectedDevices[i].address == address) {
      detectedDevices[i].name = name;
      detectedDevices[i].rssi = rssi;
      return;
    }
  }
  if (deviceCount < maxDevices) {
    detectedDevices[deviceCount++] = {address, name, rssi};
  }
}

void setup() {
  Serial.begin(115200);
  while (!Serial);

  if (!BLE.begin()) {
    Serial.println("BLE initialization failed!");
    while (1);
  }
  Serial.println("BLE initialized");
  BLE.scan(true);  // Enable active scanning
  startTime = millis();  // Track program start time
}

void loop() {
  // End program after the total runtime
  if (millis() - startTime >= totalRunTime) {
    Serial.println("\n=== Final Hourly Summary ===");
    Serial.print("{\"total_devices\":");
    Serial.print(deviceCount);
    Serial.print(",\"devices\":[");

    for (int i = 0; i < deviceCount; i++) {
      if (i > 0) Serial.print(",");
      Serial.print("{\"address\":\"");
      Serial.print(detectedDevices[i].address);
      Serial.print("\",\"name\":\"");
      Serial.print(detectedDevices[i].name);
      Serial.print("\",\"rssi\":");
      Serial.print(detectedDevices[i].rssi);
      Serial.print("}");
    }
    Serial.println("]}");
    BLE.stopScan();
    while (1);  // Stop the program
  }

  // Perform BLE scan at regular intervals
  if (millis() - lastScanTime >= scanInterval) {
    lastScanTime = millis();
    Serial.println("\n=== BLE Scan Results ===");
    BLEDevice peripheral;

    while (peripheral = BLE.available()) {
      String deviceName = peripheral.localName();
      if (deviceName.length() == 0) deviceName = "Unknown";  // Default for unnamed devices
      addDevice(peripheral.address(), deviceName, peripheral.rssi());

      // Log device details
      Serial.print("Address: "); Serial.print(peripheral.address());
      Serial.print(", Name: "); Serial.print(deviceName);
      Serial.print(", RSSI: "); Serial.println(peripheral.rssi());
    }
    Serial.println("Scan completed.\n");
  }

  // Provide a summary every 5 minutes
  if (millis() - lastSummaryTime >= summaryInterval) {
    lastSummaryTime = millis();
    Serial.println("\n=== 5-Minute Summary ===");
    Serial.print("{\"summary_interval\":\"5 minutes\",\"total_devices\":");
    Serial.print(deviceCount);
    Serial.print(",\"devices\":[");

    for (int i = 0; i < deviceCount; i++) {
      if (i > 0) Serial.print(",");
      Serial.print("{\"address\":\"");
      Serial.print(detectedDevices[i].address);
      Serial.print("\",\"name\":\"");
      Serial.print(detectedDevices[i].name);
      Serial.print("\",\"rssi\":");
      Serial.print(detectedDevices[i].rssi);
      Serial.print("}");
    }
    Serial.println("]}");
  }

  delay(100);  // Avoid overloading the CPU
}
