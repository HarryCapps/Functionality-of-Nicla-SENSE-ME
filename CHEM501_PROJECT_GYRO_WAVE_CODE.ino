#include "Arduino_BHY2.h"

SensorXYZ gyro(SENSOR_ID_GYRO);

void setup() {
  Serial.begin(115200);
  BHY2.begin();
  gyro.begin();
}

void loop() {
  BHY2.update();

  // Read the gyroscope values
  float gx = gyro.x();
  float gy = gyro.y();
  float gz = gyro.z();

  // Print the gyroscope data to Serial Monitor
  Serial.print("gyro_X: "); Serial.print(gx);
  Serial.print(", gyro_Y: "); Serial.print(gy);
  Serial.print(", gyro_Z: "); Serial.println(gz);

  // Delay to capture readings (every 100ms for example)
  delay(100);
}
