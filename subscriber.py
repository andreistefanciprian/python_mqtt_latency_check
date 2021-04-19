"""
This sript connects to mqtt broker and subscribes to a topic/channel.

When a message from a different mqtt client (publisher) is received on the channel, 
the subscriber sends a response message that includes the information from the
original message, and the identifier of the receiving device and a timestamp for when the
message was received. Responses are sent immediately.

The subscriber only listens to the subscibed channel for a predetermined amount of time (SUBSCRIBE_DURATION).
When done listening, for each pair of publishers observed, the minimum, maximum,
and average (mean) latency is calculated and displayed.
"""

from random import randrange
from mqtt_client import MyMQTTClass

if __name__ == "__main__":
    
    # define variables
    RAND_NUMBER = randrange(10000)
    CLIENT_NAME = f'Subscriber-{RAND_NUMBER}'
    SUBSCRIBE_DURATION = 5  # amount of time in senconds to subscribe to a channel

    try:
        mqttcs = MyMQTTClass(mqtt_client_name=CLIENT_NAME)
        mqttcs.subscribe_to_channel(SUBSCRIBE_DURATION)
        mqttcs.calculate_latency()
    except KeyboardInterrupt:
        pass
    