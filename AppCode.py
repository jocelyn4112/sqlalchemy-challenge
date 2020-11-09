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

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
Base.classes.keys()
# Save reference to the table
Measurement = Base.classes.Measurement
Station = Base.classes.Station

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
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/`/api/v1.0/tobs"
        f"/api/v1.0/<start>/<end>`"
    )

#Percipitation route
@app.route("/api/v1.0/precipitation")
def Precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

   ##"Convert the query results to a dictionary using `date` as the key and `prcp` as the value.
    ##Return the JSON representation of your dictionary.

     # Create a dictionary from the row data and append to a list of all_prcp
all_prcp = []
for date, prcp in all_prcp:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
        all_prcp.append(prcp_dict)

    # Query all prcp
results = session.query(Measurement.prcp).all()

session.close()

    # Convert list of tuples into normal list
all_prcp = list(np.ravel(results))

return jsonify(all_prcp)
     # Query all passengers

results = session.query(Measurement.id, Measurement.prcp).all()

session.close()

   
return jsonify(all_prcp)

#Stations Route 

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
   # * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  #* When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.
    def calc_temps(start_date):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    
return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

# function usage example
print(calc_temps('2012-02-28'))
#* When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.
def calc_temps(start_date, end_date):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    
    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

# function usage example
print(calc_temps('2012-02-28', '2012-03-05'))

def justice_league_character(real_name):
    """Fetch the Justice League character whose real_name matches
       the path variable supplied by the user, or a 404 if not."""
    canonicalized = real_name.replace(" ", "").lower()
    for character in justice_league_members:
        search_term = character["real_name"].replace(" ", "").lower()
        if search_term == canonicalized:
            return jsonify(character)
    return jsonify({"error": f"Character with real_name {real_name} not found."}), 404
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
results = session.query(Passenger.name).all()

session.close()

    # Convert list of tuples into normal list
all_names = list(np.ravel(results))

return jsonify(all_names)


if __name__ == '__main__':
    app.run(debug=True)
