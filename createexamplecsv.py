import csv
import random

FOLDER_PATH = r"C:\Users\dmaca\Desktop\RoboCode\RoboDiag\MatchData\Match0001\CSVs\analyzedata.csv"

def create_csv():
    with open(FOLDER_PATH, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            'timestamp', 
            'BatteryVoltage', 
            'Amperage', 
            'Temperature',

            'elevatorDesiredPosition',
            'elePosition',
            'eleVelo',
            'eDesiredVelo',

            'shoulderPosition',
            'shoulderDesiredPosition',

            'batteryname'
        ])
        timestamp = 0
        voltage_range = range(0, 130)
        amperage_range = range(0, 800)
        speed_range = range(-6000, 6000)
        position_range = range(-900, 900)
        temperature_range = range(0, 1000)
        for idx in range(1, 10001):
            writer.writerow([
                timestamp + 0.1*idx, 
                random.choice(voltage_range)/10, 
                random.choice(amperage_range)/10, 
                random.choice(temperature_range)/10, 

                random.choice(position_range),
                random.choice(position_range),
                random.choice(speed_range),
                random.choice(speed_range),

                random.choice(position_range),
                random.choice(position_range),

                "category1"
            ])

create_csv()