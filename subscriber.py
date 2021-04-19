from random import randrange
from mqtt_client import MyMQTTClass

if __name__ == "__main__":
    
    # define variables
    rand_number = randrange(10000)
    CLIENT_NAME = f'Subscriber-{rand_number}'
    SUBSCRIBE_DURATION = 5

    try:
        mqttcs = MyMQTTClass(mqtt_client_name=CLIENT_NAME)
        mqttcs.subscribe_to_channel(SUBSCRIBE_DURATION)
        mqttcs.calculate_latency()
    except KeyboardInterrupt:
        pass

