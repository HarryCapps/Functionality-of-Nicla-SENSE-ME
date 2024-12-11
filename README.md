# CHEM501_Project

This GitHub repository contains the code for the CHEM501 Project - Digital Alchemy: Synthesising Code and Chemistry at the University of Liverpool.


# Description 

Hi! We’re Harry and Ben, and this is our CHEM501 project exploring the overall functionality of the NICLA Sense ME. The investigation will take place across two seperate buildings within the university of liverpool (Central Teaching Hub and Sydney Jones library). For us to investigate the potential of the Nicla Sense ME, we decided to look into the BSEC sensor - a digital indoor air quality sensor with the ability to detect pressure, humidity, temperature, CO2 concentrations, VOC concentrations all within an accuracy index measurement. We will use this sensor to detect how good the BSEC is at detecting the IAQ with a related accuracy reading and how valid this index is. The Bluetooth low energy (BLE) sensor was also used as a measurement of detection for devices in a certain area to give an indication to 'busyness'. Finally the last sensor we were intrigued by was the Gyroscope, this was measured and detected via hand movements.

# Files

This repository contains the following 13 files:

CHEM501_PROJECT_BLE_CODE.ino

C++ code used to operate the BLE Sensor.

CHEM501_PROJECT_BLE_DATA_VISUALISATION.py

Python code created to create graphs for BLE.

CHEM501_PROJECT_BSEC_CODE.ino

C++ code used to operate the BSEC Sensor.

CHEM501_PROJECT_BSEC_DATA_VISUALISATION.py

Python code created to create graphs for BLE.

CHEM501_PROJECT_GYRO_WAVE_CODE.ino

C++ code used for the Gyroscope Sensor.

CHEM501_GYRO_DATABASE.py

Python code used to create a database for the gyroscope using SQLite.

CHEM501_GYRO_DATA_VISUALISATION.ipynb

A jupyter notebook file with multistep code to visualise gyroscopic data and set thresholds to distinguish noise and stationary states from a wave gesture.

CHEM501_DATA_CONVERTER.py

Python code used to convert the data given by BSEC and BLE sensor into a csv file.

CHEM501_METADATA_BSEC_BLE.zip

Series of CSV files containing Metadata for BSEC and BLE Sensor.

CHEM501_PLAINDATA_BSEC_BLE.zip

Series of CSV files containing exmaples of basic data readings from BSEC and BLE sensor.

CHEM501_GYRO_METADATA.csv

A CSV file containing metadata for the gyro sensor measurements.

README.md

requirements.txt

# Requirements

The following software is needed in order to code and recieve the appropriate data:

Virtual Studio Code (or any other code editor) - https://code.visualstudio.com

Arduino IDE - https://www.arduino.cc/en/software

Python (Anaconda is recommended use. For installation, click free download via the following URL) - https://www.anaconda.com/

The hardware requirements for this project are as follows:

Arduino Nicla Sense ME - https://store.arduino.cc/products/nicla-sense-me

# Installation

If using Anaconda, the pyserial module must be installed.

If using Windows:

1. Open Anaconda Prompt.

2. Type conda install pyserial.

3. Press Enter.

If using macOS:

1. Open Terminal.

2. Type conda install pyserial.

3. Press Enter.

Next, open Arduino IDE and navigate to Tools --> Board --> Board Manager, then install the following:

Arduino Mbed OS Nicla Boards

In the Arduino IDE, navigate to Tools --> Manage Libraries, and install the following:

Arduino_BHY2

Arduino_BHY2Host

ArduinoBLE

# Usage

In order to collect the wanted data using the software and hardware listed above, a set of instructions is given below:

1. The Arduino Nicla Sense ME must be plugged into your computer via a USB-A to micro USB.
2. The Arduino IDE software application is opened.
3. Choose a sensor to test.
4. i.e Run CHEM501_PROJECT_BSEC_CODE.ino in Arduino IDE ensuring to keep the serial monitor closed.
5. Virtual Studio Code should be open and ready.
6. Run CHEM501_DATA_CONVERTER.py (or CHEM501_GYRO_DATABASE.py for Gyro) in VSCode alongside the Arduino IDE to allow the data to be stored in a csv file for BSEC and BLE (or Database for Gyroscope).
8. Use the Respectable Visualisation Codes to gain graphical representations of each Sensor.

# Authors

If there are any questions or additional information, please get in touch:

Harry Capps (sghcapps@liverpool.ac.uk)

Ben Rogers (sgbroger@liverpool.ac.uk)

# License

This project is not currently licensed

# Acknowledgements

We are deeply grateful to Dr. Joe Forth, Professor Anna Slater, and Harvey West for their invaluable support throughout this project. Our sincere thanks also go to Dr. Anthony Bradley and Dr. Gemma Holliday for generously sharing their expertise in SQL (Structured Query Language) and FAIR principles (Findable, Accessible, Interoperable, and Reusable), which greatly enriched our work.
