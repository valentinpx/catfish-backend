import mysql.connector
from json import loads

# Convert database query result to JSON
def jsonify(reports):
  dest = []

  for report in reports:
    dest.append({
      "client_id": report[1],
      "date": report[2],
      "CDOM": report[3],
      "nitrate": report[4],
      "dissolved_oxygen": report[5],
      "PH": report[6],
      "induction": report[7],
      "fish_depth": report[8],
      "pressure": report[9],
      "depth": report[10]
    })
  return dest
    

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
  
  # Insert MQTT message into database
  def insert(self, client, userdata, msg):
    cursor = self.db.cursor()
    data = loads(msg.payload)

    cursor.execute(
      "INSERT INTO reports (client_id, date, CDOM, nitrate, dissolved_oxygen, PH, induction, fish_depth, pressure, depth) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
      (msg.topic.split("/")[1], data["TIME"], data["CDOM"], data["NITRATE"], data["DISSOLVED_OXYGEN"], data["PH"], data["INDUCTION"], data["FISH_DEPTH"], data["PRESSURE"], data["DEPTH"])
    )
    self.db.commit()
  
  # Get reports from database between start and end dates for the specified client IDs
  def get_reports(self, ids, start, end):
    converter = mysql.connector.conversion.MySQLConverter()
    cursor = self.db.cursor()
    id_list_str = ", ".join([f"'{converter.escape(v)}'" for v in ids])
    start_str = converter.escape(start)
    end_str = converter.escape(end)

    cursor.execute(f"SELECT * FROM reports WHERE client_id IN ({id_list_str}) AND date BETWEEN '{start_str}' AND '{end_str}'")
    return jsonify(cursor.fetchall())
