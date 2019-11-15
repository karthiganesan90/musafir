import Python_DHT
import time
import os
K = "echo ‘SLOW DOWN.      ROADS ARE SLIPPERY’ | festival --tts"
sensor = Python_DHT.DHT11
speedLimit = 40
currentSpeed = 60
while True:
    humidity, temperature = Python_DHT.read_retry(sensor, 17)
    print("Temperature = "+str(temperature)+ "C Humidity = "+str( humidity)+"%" "  Speed Limit  = " +str(speedLimit) +"mph" " Current Speed = " +str(currentSpeed) +"mph")
    time.sleep(5)
    if humidity > 40 and temperature < 30 and speedLimit >= 40 and currentSpeed >= 40:
        os.system(K)