from flask import Flask
from core.controllers.flights.flights_controller import FlightsController


flights = FlightsController()
app = Flask(__name__)

@app.route('/api/flights/', method = 'GET')
def get_all_flights():
    read_all_flights = flights.read()
    return str(read_flight)

@app.route('api/flights/<id int>', method = 'GET')
def get_flight_by_id(id):
    read_the_flight = flights.read_id(id)
    return print(read_the_flight)

@app.route('api/flights/',  method = 'DELETE')
def delete_flights():
    flights.delete_all()
    return 'all flights were deleted'

@app.route('api/flights/<id int>', method = 'DELETE')
def delete_the_flight(id):
    flights.delete_by_id(id)
    return 'flights with {0} was deleted'.format(id)

@app.route('api/flights/', method = 'create')
def create(id_plane, _from, _to, date_departure, date_arrival):
    flights.create(id_plane, _from, _to, date_departure, date_arrival)
    return 'flight was created'

@app.route('api/flights/<id int>', method = 'EDIT')
def edit(id):
    flights.update(_to, id_plane)
    return 'flight was edited'



