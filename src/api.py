from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/reports", methods=['GET'])
def get_reports():
    db = app.config['DB']
    reports = db.get_reports(request.args["ids"], request.args["start"], request.args["end"])

    return reports
