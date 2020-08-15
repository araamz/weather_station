import bme280
import smbus2
import datetime
from time import sleep

print("PROGRAM START -> PROGRAM LOOP")

class bme280_IC:

    def __init__(self, device_port, device_address):
        self.device_port = device_port
        self.device_address = device_address
        self.device_bus = smbus2.SMBus(device_port)
        bme280.load_calibration_params(self.device_bus, self.device_address)
        self.device_data_link = bme280.sample(self.device_bus, self.device_address)
    
    @property
    def temperature_value(self):
        return self.device_data_link.temperature

    @property
    def pressure_value(self):
        return self.device_data_link.pressure

main_sensor = bme280_IC(1, 0x76)

current_file = open('DATA/PROGRAM_START_INFORMATION.txt', "w", 1)
current_file.write("STARTED AT " + str(datetime.datetime.today()))
current_file.close()

while True: 

    print("START -> MAIN EVENT LOOP")

    current_date = datetime.datetime.today().strftime('%d_%m_%Y')

    if (current_date == datetime.datetime.today().strftime('%d_%m_%Y')):

        print("IF -> MAIN EVENT LOOP")

        current_file = open(datetime.datetime.today().strftime('DATA/%d_%m_%Y') + '.txt', "a+", 1)
        current_file.write(datetime.datetime.now().strftime('%H_%M') + ":" + str(main_sensor.temperature_value) + "_" + str(main_sensor.pressure_value) + "\n")
        sleep(1800)

    else: 

        print("ELSE -> MAIN EVENT LOOP")

        current_file.close()
        current_file = open(datetime.datetime.today().strftime('DATA/%d_%m_%Y'), "a+", 1)
        current_file.write(datetime.datetime.now().strftime('%H_%M') + ":" + str(main_sensor.temperature_value) + "_" + str(main_sensor.pressure_value) + "\n")
