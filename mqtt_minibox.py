
import paho.mqtt.client as mqtt


mqtt_username = "dimaystinov"
mqtt_password = "00000000"
mqtt_topic = "temp"
mqtt_broker_ip = "192.168.43.215"

client = mqtt.Client()

client.username_pw_set(mqtt_username, mqtt_password)


def on_connect(client, userdata, flags, rc):

    print("Connected!" + str(rc))

    client.subscribe(mqtt_topic)


def on_message(client, userdata, msg):

    print("Topic: " + msg.topic + "\nMessage: " + str(msg.payload))


client.on_connect = on_connect
client.on_message = on_message


client.connect(mqtt_broker_ip, 1883)


client.loop_forever()
client.disconnect()
