import csv
import datetime
import time

import board
from busio import I2C
import adafruit_bme680

# Create library object using our Bus I2C port
i2c = I2C(board.SCL, board.SDA)
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)

# change this to match the location's pressure (hPa) at sea level
bme680.sea_level_pressure = 1013.25


def main(csv_writer):
    while True:
        # print("\nTemperature: %0.1f C" % bme680.temperature)
        # print("Gas: %d ohm" % bme680.gas)
        # print("Humidity: %0.1f %%" % bme680.humidity)
        # print("Pressure: %0.3f hPa" % bme680.pressure)
        # print("Altitude = %0.2f meters" % bme680.altitude)

        data = datetime.datetime.now(tz=datetime.timezone.utc).isoformat(), \
               bme680.temperature, bme680.gas, bme680.humidity, bme680.pressure, bme680.altitude

        csv_writer.writerow(data)
        print(data)
        time.sleep(1)


if __name__ == '__main__':
    with open('bme680.csv', 'a') as csvfile:
        main(csv_writer=csv.writer(csvfile))
