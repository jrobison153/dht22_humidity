import adafruit_dht
import board
import json
import sys

dhtDevice = adafruit_dht.DHT22(board.D4)


temperature_c = dhtDevice.temperature
humidity = dhtDevice.humidity

if humidity is not None and temperature_c is not None:
  temperature_f = temperature_c * (9 / 5) + 32

  output = {
    'temp-celcius': temperature_c,
    'temp-farenheit': temperature_f,
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
