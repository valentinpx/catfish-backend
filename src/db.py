import mysql.connector
from json import loads

def store_msg(client, userdata, msg):
  print(loads(msg.payload), msg.topic.split("/")[1])

class DB():
  def __init__(self, host, user, password, database):
    self.db = mysql.connector.connect(
      host=host,
      user=user,
      password=password,
      database=database
    )
    cursor = self.db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS reports (id INT AUTO_INCREMENT PRIMARY KEY, client_id VARCHAR(200), date VARCHAR(20), CDOM FLOAT, nitrate FLOAT, dissolved_oxygen FLOAT, PH FLOAT, induction FLOAT, fish_depth FLOAT, pressure FLOAT, depth FLOAT)")
    self.db.commit()
  
  def insert(self, client, userdata, msg):
    cursor = self.db.cursor()
    data = loads(msg.payload)

    cursor.execute(
      "INSERT INTO reports (client_id, date, CDOM, nitrate, dissolved_oxygen, PH, induction, fish_depth, pressure, depth) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
      (msg.topic.split("/")[1], data["TIME"], data["CDOM"], data["NITRATE"], data["DISSOLVED_OXYGEN"], data["PH"], data["INDUCTION"], data["FISH_DEPTH"], data["PRESSURE"], data["DEPTH"])
    )
    self.db.commit()
