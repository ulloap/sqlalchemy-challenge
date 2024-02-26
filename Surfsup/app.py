# Import the dependencies.
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import numpy as np 
from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

#################################################
# Database Setup
#################################################


# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with = engine)

# Save references to each table
base_measurement = Base.classes.measurement
base_station = Base.classes.station

# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")

def welcome():

    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs"
        f"/api/v1.0/Y-M-D/starts/end/<starts>/<end>"
        )

# Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) 
# to a dictionary using date as the key and prcp as the value.
@app.route("/api/v1.0/precipitation")

def precipitation():
    session = Session(engine)
    results = session.query(base_measurement.prcp).all()
    session.close()
    rain_data = list(np.ravel(results))
# Return the JSON representation of your dictionary.
    return jsonify(rain_data)

# Return a JSON list of stations from the dataset

f = open("hawaii.sqlite","w",encoding='utf-8')
@app.route("/api/v1.0/stations")