import sys
import time
import random
from uart import *
from Adafruit_IO import MQTTClient


AIO_FEED_ID = ["device_fan", "device_light", "mode"]
AIO_USERNAME = "nguyennamkha"
AIO_KEY = "aio_ruiV8486TRzDh0QOrwsUdc6XRwGE"


def connected(client):
    for topic in AIO_FEED_ID:
        client.subscribe(topic)
    print("Ket noi thanh cong ...")


def subscribe(client, userdata, mid, granted_qos):
    print("Subscribe thanh cong ...")


def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit(1)


def message(client, feed_id, payload):
    print("Nhan du lieu: " + payload + ", feed id:" + feed_id)
    if feed_id == 'device_fan':
        writeData(payload)
    elif feed_id == 'device_light':
        writeData(payload)
    elif feed_id == 'mode':
        writeData(payload)


client = MQTTClient(AIO_USERNAME, AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

while True:
    readSerial(client)
    pass
