import paho.mqtt.client as mqtt #import the client1
import time
import os

def on_message(client, userdata, message):
    print("recebido " ,str(message.payload.decode("utf-8")))

    if str(message.payload.decode("utf-8"))=="1":
        print "Chegou aqui"
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

os.system("start mosquito.bat")
os.system("python mqtt_get_message.py")
broker_address="127.0.0.1"
#broker_address="iot.eclipse.org"
while (True):
    
    contexto = raw_input("Digite o valor do conexto")
    valor = raw_input ("Digite o valor que será escrito no conexto")
    print("creating new instance")
    client = mqtt.Client("P1") #create new instance
    client.on_message=on_message #attach function to callback
    print("connecting to broker")
    client.connect(broker_address) #connect to broker
    client.loop_start() #start the loop
    print("Subscribing to topic","house/bulbs/bulb1")
    client.subscribe(contexto)
    print("Publishing message to topic","house/bulbs/bulb1")
    client.publish(contexto,valor)
    time.sleep(4) # wait
    client.loop_stop() #stop the loop
