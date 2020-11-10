import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")
#conn = engine.connect()
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
print(Base.classes.keys())
# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def Home():
    """List all available api routes."""
    return (
        f"Vacation Time!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/`/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start>/<end>`"
    )

#Percipitation route
@app.route("/api/v1.0/precipitation")
def Precipitation():
    # Create session (link) from Python to the DB
    session = Session(engine)

   ##"Convert the query results to a dictionary using `date` as the key and `prcp` as the value.
    ##Return the JSON representation of your dictionary.

     # Create a dictionary from the row data and append to a list of all_prcp
     
    results = session.query(Measurement.date, Measurement.prcp).all()
    session.close()
    all_prcp = []
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
        all_prcp.append(prcp_dict)

    return jsonify(all_prcp)
     # Query all 


#Stations Route 

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/api/v1.0/stations")
def stations():
# Return a JSON list of stations from the dataset
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    """Return a list of all Station names"""
    # Query all Stations
    results = session.query(stations.name).all()

    session.close()

    # Convert list of tuples into normal list
    all_stations = list(np.ravel(results))

    return jsonify(all_stations)



@app.route("/api/v1.0/tobs")
def Observations():
    # Return a JSON list of stations from the dataset
    # Create our session (link) from Python to the DB
    session = Session(engine)
  # Query the dates and temperature observations of the most active station for the last year of data.
  
  
    session.query(Measurement.tobs, func.sum(Measurement.Total)).\
        group_by(Measurement.tobs).\
        order_by(func.sum(Measurement.Total).desc()).all()

 # Return a JSON list of temperature observations (TOBS) for the previous year.
   
  
    # Query all 
    results = session.query(Measurement.tobs).all()

    session.close()

    # Convert list of tuples into normal list
    all_observaions = list(np.ravel(results))

    return jsonify(all_all_observations)

#API Start / #API End

@app.route("/api/v1.0/<start>/<end>")
def API():
    # Return a JSON list of stations from the dataset
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
    
#session.close()

if __name__ == '__main__':
    app.run(debug=True)
