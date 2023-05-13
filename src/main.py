import os
from dotenv import load_dotenv
from threading import Thread
from mqtt_client import MQTTClient
from db import DB
from api import app

load_dotenv("../.env")

# Create database connection
db = DB(os.getenv("DB_HOST"), os.getenv("DB_USER"), os.getenv("DB_PASS"), "reports")

# Start MQTT client in a separate thread
cli = MQTTClient(os.getenv("BROKER_USER"), os.getenv("BROKER_PASS"))
cli.connect(os.getenv("BROKER_HOST"), int(os.getenv("BROKER_PORT")))
Thread(target=lambda: cli.run(db.insert)).start()

# Run the API
app.config["DB"] = db
app.run()
