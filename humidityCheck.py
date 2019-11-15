import Python_DHT
import time
import os
import random
K = "echo ‘SLOW DOWN.      ROADS ARE SLIPPERY’ | festival --tts"
sensor = Python_DHT.DHT11
speedLimit = 60
currentSpeed = random.randint(55,60)
while True:
    humidity, temperature = Python_DHT.read_retry(sensor, 17)

    print("Temperature = "+str(temperature)+ "C Humidity = "+str( humidity)+"%" "  Speed Limit  = " +str(speedLimit) +"mph" " Current Speed = " +str(currentSpeed) +"mph")
    time.sleep(5)
    if humidity > 20 and temperature < 30 and speedLimit >= 40 and currentSpeed >= 55:
        os.system(K)
