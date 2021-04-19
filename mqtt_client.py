import paho.mqtt.client as mqtt
import time
import os
from random import randrange

class MyMQTTClass:

    """
    Used for establishing connection to mqtt broker and publishing a message on a topic.
    """

    def __init__(self, mqtt_client_name, mqtt_host=None, mqtt_port=None, mqtt_client_type=None, mqtt_channel=None, logging=None):
        self.mqtt_host = 'test.mosquitto.org' if mqtt_host is None else mqtt_host
        self.mqtt_port = 1883 if mqtt_port is None else mqtt_port
        self.mqtt_client_name = mqtt_client_name
        self.mqtt_client = mqtt.Client(mqtt_client_name)
        self._mqtt_connected = False
        self.mqtt_channel = 'DEFAULT_CHANNEL' if mqtt_channel is None else mqtt_channel
        # self.logging = False if logging is None else logging
        self._latencies = {}
        self._latency_float_digits = 4
        self._rand_number = randrange(10000)
        self.client_hostname = f'{os.uname()[1]}-{self._rand_number}'

    # def log(self, message):
    #     """Log message."""

    #     if self.logging:
    #         print(message)

    def _mqtt_connect(self, **kwargs):
        """
        Establish connection to mqtt broker.
        Returns True when connection si established.
        """

        if not self._mqtt_connected:
            try:
                self.mqtt_client.connect(self.mqtt_host, **kwargs)
            except Exception as e:
                raise
            else:
                print(f'Connection to {self.mqtt_host} was established!')
                self._mqtt_connected = True
                return True
        else:
            return True
            
    
    def publish(self, message):
        """
        Publish message on mqtt channel.
        """

        if self._mqtt_connect():
            self.mqtt_client.publish(self.mqtt_channel, message)
            print(message)
        else:
            print('Connection failed!')

    def on_message(self, mqttc, userdata, message):
        """
        When message is published on the channel, this call back function is called.
        """

        received_message = str(message.payload.decode("utf-8")) # convert published message to string
        current_timestamp = time.time() # register the timestamp when the message was received

        # sends a message to the channel with the timestamp when the message was received
        sender_type = received_message.split()[-1]
        if sender_type == 'PUBLISHER':
            sender_hostname = received_message.split()[0]
            sender_timestamp = float(received_message.split()[1])
            latency = current_timestamp - sender_timestamp
            latency = round(latency, self._latency_float_digits)

            # add latency to dict
            if sender_hostname in self._latencies:
                self._latencies[sender_hostname].append(latency)
            else:
                self._latencies[sender_hostname] = [latency]

            # publish message with latency details
            msg = f'{latency}s - A message sent by {sender_hostname} at {sender_timestamp} was received by {self.client_hostname} at {current_timestamp} SUBSCRIBER'
            self.publish(msg)


    def subscribe_to_channel(self, subscribe_duration):
        """
        This method subscribed to an mqtt channel.
        Send reply message to channel with host identifier and received timestamp.
        """

        if self._mqtt_connect():
            try:
                self.mqtt_client.subscribe(self.mqtt_channel)
            except:
                raise
            else:
                self.mqtt_client.loop_start()
                self.mqtt_client.on_message=self.on_message
                time.sleep(subscribe_duration)
                self.mqtt_client.loop_stop()
        else:
            print('Connection failed!')

    def calculate_latency(self):
        """
        Calculates the min, max and average latency for subscribers.
        """

        for subscriber,latencies in self._latencies.items():
            min_latency = min(latencies)
            max_latency = max(latencies)
            avg_latency = round(sum(latencies)/len(latencies), self._latency_float_digits)
            print(f'{subscriber} latency results - min:{min_latency}s max:{max_latency}s avg:{avg_latency}s')

    def __del__(self):
        """
        Closes mqtt connection.
        """

        self.mqtt_client.disconnect()
        print(f'Connection to {self.mqtt_host} was disconnected!')
