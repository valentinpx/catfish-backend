import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
  client.subscribe("reports/#", qos=1)

def on_message(client, userdata, msg):
  print("Received message %s on topic %s with QoS %s" % (msg.payload, msg.topic, msg.qos))

class MQTTClient():
  def __init__(self, user, password):
    self.client = mqtt.Client()
    self.client.username_pw_set(user, password)

  def connect(self, host, port):
    self.client.connect(host, port)

  def run(self):
    self.client.on_connect = on_connect
    self.client.on_message = on_message
    self.client.loop_forever()
