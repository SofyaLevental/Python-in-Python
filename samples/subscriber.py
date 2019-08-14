import paho.mqtt.client


class Subscriber:
    @staticmethod
    def subscribe_for_commands(on_message):
        client = paho.mqtt.client.Client("commandsSub")
        client.on_message = on_message
        client.connect("Marocchino")
        client.loop_start()
        client.subscribe("commands")
