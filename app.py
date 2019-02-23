from flask import Flask
from core.controllers.flight.flights_controller import FlightsController


flights = FlightsController()
app = Flask(__name__)

@app.route('/api/flights/', method = 'GET')
def get_all_flights():
    read_all_flights = flights.read()
    return str(read_flight)

@app.route('api/flights/<id int>')
def get_flight_by_id(id):
    read_the_flight = flights.read_id(id)
    return print(read_the_flight)

@app.route('api/flights/)
def delete_flights():
    flights.delete_all()
    return 'all flights were deleted'

@app.route('api/flights/<id int>')
def delete_the_flight(id):
    flights.delete_by_id(id)
    return 'flights with {0} was deleted'.format(id)

@app.route('api/flights/')
    def create(
        flights.create(id_plane, _from, _to, date_departure, date_arrival)



# @app.route('/api/flights/create/')
# def create():
#     flight.create(3, "'MINSK'", "'NEW YORK'", "'20-02-12 19:00'", "'21-02-15 19:00'")
#     return "created"
#
# @app.route('/api/flights/delete/')
# def delete():
#     flight.delete(3)
#     return "deleted"
#
# if __name__ == "__main__":
#     app.run()

