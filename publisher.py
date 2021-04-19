from mqtt_client import MyMQTTClass
from random import randrange
import time

if __name__ == "__main__":
    
    # define variables
    MSG_COUNT = 50   # number of messages to publish
    WAIT_TIME = 1   # wait time between messages
    CLIENT_TYPE = 'PUBLISHER'   # used as tag in mqtt messages to identofy publisher/subscriber messages
    RAND_NUMBER = randrange(1000)
    CLIENT_NAME = f'Publisher-{RAND_NUMBER}'
    
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
