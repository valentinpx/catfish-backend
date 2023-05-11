import os
from dotenv import load_dotenv
from mqtt_client import MQTTClient
from db import DB

load_dotenv("../.env")

db = DB(os.getenv("DB_HOST"), os.getenv("DB_USER"), os.getenv("DB_PASS"), "reports")

cli = MQTTClient(os.getenv("BROKER_USER"), os.getenv("BROKER_PASS"))
cli.connect(os.getenv("BROKER_HOST"), int(os.getenv("BROKER_PORT")))
cli.run(db.insert)
