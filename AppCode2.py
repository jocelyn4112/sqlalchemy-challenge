import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import datetime as dt

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")
#conn = engine.connect()
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
Base.classes.keys()
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

@app.route("/api/v1.0/stations")
def stations():
# Return a JSON list of stations from the dataset
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    """Return a list of all Station names"""
    # Query all Stations
    results = session.query(Station.station).all()

    session.close()

    # Convert list of tuples into normal list
    all_stations = list(np.ravel(results))

    return jsonify(all_stations)

#Observations Route

@app.route("/api/v1.0/tobs")
def Observations():
    # Return a JSON list of stations from the dataset
    # Create our session (link) from Python to the DB
    session = Session(engine)
  # Query the dates and temperature observations of the most active station for the last year of data.
  
    one_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)


    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
            filter(Measurement.date >= one_year).all()
       

 # Return a JSON list of temperature observations (TOBS) for the previous year.
   

    session.close()

    # Convert list of tuples into normal list
    all_observations = list(np.ravel(results))

    return jsonify(all_observations)

#API Start / #API End
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def API(start=None , end=None):
    # Return a JSON list of stations from the dataset
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    stat = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs) ]

    if not end:
        results = session.query(*stat).\
        filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()
        temps = list(np.ravel(results))
        session.close()
        return jsonify(temps)

    results = session.query(*stat).\
        filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    session.close()
    return jsonify(temps)
    
#session.close()

if __name__ == '__main__':
    app.run(debug=True)
