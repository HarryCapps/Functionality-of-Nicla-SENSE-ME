# How-does-population-density-influence-localised-air-quality-within-the-University-of-Liverpool-
A Chem501 Project Done by Harry Capps and Ben Rogers



# Indoor Air Quality Monitoring at the University of Liverpool  

Hi! We’re Harry and Ben, and this is our CHEM501 project exploring how population density affects indoor air quality (IAQ) at the University of Liverpool. Our goal is to investigate differences in IAQ during peak and off-peak hours across various university locations. By measuring factors like VOC levels, CO2 concentrations, temperature, and humidity, we aim to identify patterns and trends that shed light on how human activity impacts the air we breathe.  

To make this happen, we’re using two awesome pieces of hardware. First, the Nicla Sense ME, which collects detailed IAQ data. Second, the MKR WiFi 1010, which transmits that data to an MQTT broker in real-time. From there, we convert the data into a CSV file and use SQL to organize it into database tables for deeper analysis. The final step? Creating visualizations to bring the data to life and presenting our findings in a way that’s clear and impactful.  

Here’s how it all works: The Nicla Sense ME measures IAQ parameters and sends them to the MKR WiFi 1010, which acts as the bridge to the MQTT broker. The broker receives the data, and we use Python scripts to turn it into a CSV file. After that, SQL takes over, allowing us to organize the information into clean, structured tables. Finally, we use tools like Python (Matplotlib), Tableau, or Power BI to create graphs and charts that highlight key insights—like how IAQ changes depending on the time of day or the number of people around.  

Setting up the system is straightforward. The Nicla Sense ME connects to the MKR WiFi 1010 via the ESLOV connector, and both devices are powered using USB. We programmed the MKR WiFi 1010 using the Arduino IDE with libraries like `ArduinoMqttClient`, `WiFiNINA`, and `Arduino_BHY2Host`. Once it’s up and running, the system automatically collects and sends data continuously to the MQTT broker, making the whole process seamless.  

The aim of this project is to paint a clear picture of air quality trends across the university. By analyzing the data, we can pinpoint how environmental conditions change with human activity and share actionable insights for improving air quality in shared spaces. Our findings will be presented in an accessible and engaging format, making them useful for everyone from students to university administrators.  

If you’d like to know more about our project, collaborate, or just share ideas, feel free to reach out to us here on GitHub. We’re Harry and Ben, and we’re excited to dive into the air we breathe and uncover its secrets. Together, let’s figure out how we can all breathe a little easier!   
