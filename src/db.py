import couchdb
from json import loads, dumps

class DB():
  def __init__(self, host, user, password, database):
    srv = couchdb.Server(f"http://{user}:{password}@{host}:5984/")

    try:
      self.db = srv[database]
    except couchdb.http.ResourceNotFound:
      self.db = srv.create(database)
  
  # Insert MQTT message into database
  def insert(self, client, userdata, msg):
    data = loads(msg.payload)
    client_id = msg.topic.split("/")[1]

    if "TIME" not in data:
      return ("Missing date", 400)
    self.db.save({
      "CLIENT_ID": client_id,
      **data
    })
  
  # Get reports from database between start and end dates for the specified client IDs
  def get_reports(self, ids, start, end):
    return(
      dumps(list(self.db.find({
        "selector": {
          "CLIENT_ID": {
            "$in": ids
          },
          "TIME": {
            "$gte": start,
            "$lte": end
          }
        }
      })))
    )
