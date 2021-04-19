from mqtt_client import MyMQTTClass
from random import randrange
import time

if __name__ == "__main__":
    
    # define variables
    rand_number = randrange(1000)
    CLIENT_NAME = f'Publisher-{rand_number}'
    CLIENT_TYPE = 'PUBLISHER'
    WAIT_TIME = 1   # wait time between messages
    MSG_COUNT = 500   # number of messages to send

    # publish messages on mqtt topic
    try:
        mqttc = MyMQTTClass(mqtt_client_name=CLIENT_NAME, logging=True)
        while MSG_COUNT > 0:
            message = f'{mqttc.client_hostname} {time.time()} {CLIENT_TYPE}'
            mqttc.publish(message)
            time.sleep(WAIT_TIME)
            MSG_COUNT -= 1
    except KeyboardInterrupt:
        pass
