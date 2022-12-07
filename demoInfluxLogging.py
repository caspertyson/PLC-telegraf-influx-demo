from pylogix import PLC
import paho.mqtt.client as mqtt
import time
import json
from queue import Queue

client = mqtt.Client("Casper")
client.connect('127.0.0.1')

with PLC() as comm:
    comm.IPAddress = '10.140.36.4'
    
    while True:
        plcTime = comm.GetPLCTime()
        
        timens = time.time_ns()
        date = str(plcTime.Value).replace(".","-").replace(":","-").split("-")
        
        # works 
        # client.publish("test", "weather,location=us-midwest temperature=" + date[5] + " " + str(timens))
        
        # also works, but lets influxdb add the timestamp (server timestamp might be more accurate?) (date is random value just for testing)
        client.publish("test", "weather,location=us-midwest temperature=" + date[5])
        
        #print("weather,location=us-midwest temperature=" + date[3] + " " + str(timens))
        time.sleep(1)