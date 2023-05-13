from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/reports", methods=['GET'])
def get_reports():
    db = app.config['DB']
    reports = db.get_reports(request.json["ids"], request.json["start"], request.json["end"])

    return reports
