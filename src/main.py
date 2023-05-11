import os
from dotenv import load_dotenv
from mqtt_client import MQTTClient

load_dotenv("../.env")

cli = MQTTClient(os.getenv("BROKER_USER"), os.getenv("BROKER_PASS"))
cli.connect(os.getenv("BROKER_HOST"), int(os.getenv("BROKER_PORT")))
cli.run()
