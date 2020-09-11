import Adafruit_DHT
import json
import sys

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

humidity, temperatureCelcius = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

if humidity is not None and temperatureCelcius is not None:
  temperatureFarenheit = temperatureCelcius * (9 / 5) + 32

  output = {
    'temp-celcius': temperatureCelcius,
    'temp-farenheit': temperatureFarenheit,
    'humidity-percentage': humidity 
  }

  outputAsJson = json.dumps(output)

  print(outputAsJson)
  sys.exit(0)
else:
  error = {
    'reason': 'Unable to retrieve data from humidity sensor' 
  }

  errorAsJson = json.dumps(error)
  print(errorAsJson)

  sys.exit(1)
