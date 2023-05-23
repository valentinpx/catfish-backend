# Catfish Backend
This project is a backend server for the Catfish project.
It receives organizes and stores the data sent by the Catfish in MQTT to a MySQL database and provides an API to access it.

# Usage
## Setup
Install docker and docker-compose.
Create a `.env` file in the root of the project based on the `.env.example` file.

## Run
Run `docker-compose up` to start the server.

# Development
The MQTT broker, database and python server run in docker containers that can be configured in the `docker-compose.yml` file.

## MQTT Broker
The MQTT broker configuration is stored in the `moquitto/config` folder.

## Database
The server interracts with a CouchDB database thanks to the [couchdb python](https://couchdb-python.readthedocs.io/en/latest/) library. The file `src/db.py` contains the DB class that handles the connection and queries.
The tables are created in the class constructor at the first run of the server.

## API
The server exposes an API to access the data stored in the database thanks to the [Flask](https://flask.palletsprojects.com/en/2.3.x/) library.
The API routes are defined in the `src/api.py` file.

### Routes
#### GET /reports
Returns a list of all the reports in the database between the `start` and `end` dates with matching `client_ids`.
##### Parameters
- `start`: UTC start date and time of your search in ISO 8601 format
- `end`: UTC end date and time of your search in ISO 8601 format
- `client_ids`: List of client ids to filter the results
##### Response
```json
[
  {
    "CDOM": 3.0,
    "PH": 26.0,
    "CLIENT_ID": "CATFISH_PROTOTYPE",
    "TIME": "2023-04-27T04:20:00Z",
    "DEPTH": 7.0,
    "DISSOLVED_OXYGEN": 59.0,
    "FISH_DEPTH": 8.0,
    "INDUCTION": 535.0,
    "NITRATE": 141.0,
    "PRESSURE": 9.0
  },
  {
    "CDOM": 3.0,
    "PH": 26.0,
    "CLIENT_ID": "CATFISH_PROTOTYPE",
    "TIME": "2023-04-27T04:20:00Z",
    "DEPTH": 7.0,
    "DISSOLVED_OXYGEN": 59.0,
    "FISH_DEPTH": 8.0,
    "INDUCTION": 535.0,
    "NITRATE": 141.0,
    "PRESSURE": 9.0
  },
]
```

# License
This work is licensed under a [CreativeCreative Commons Attribution-NonCommercial 4.0 International License](http://creativecommons.org/licenses/by-nc/4.0/).

Made with 💖 by Valentin Sene.

![Creative Commons License](https://i.creativecommons.org/l/by-nc/4.0/88x31.png "Creative Commons License")
