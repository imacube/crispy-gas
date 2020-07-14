# crispy-gas
Adafruit BME680 - temperature, humidity, pressure, and VOC Gas.

# Installing

```shell script
git clone https://github.com/imacube/crispy-gas.git
cd crispy-gas
python3 -m venv venv
source venv/bin/activate
# You should see (venv) prefix in CLI prompt
pip install -r requirements.txt
```

# bme680_record.py
Records data from the BME680 sensor to the file: `bme680.csv`.

# bme680_simpletest.py
Copied from [Adafruit_CircuitPython_BME680](https://github.com/adafruit/Adafruit_CircuitPython_BME680).

# References
- [Adafruit BME680 - Learning](https://learn.adafruit.com/adafruit-bme680-humidity-temperature-barometic-pressure-voc-gas/overview)
- [Adafruit BME680 - Product](https://www.adafruit.com/product/3660)
- [Circuit Python on Raspberry Pi Linux](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi)
