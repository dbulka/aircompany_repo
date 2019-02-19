from flask import Flask
from core.controllers.flight.flights_controller import FlightsController


flight = FlightsController()
app = Flask(__name__)

@app.route('/api/flights/get/')
def read():
    return str(flight.read())

@app.route('/api/flights/create/')
def create():
    flight.create(3, "'MINSK'", "'NEW YORK'", "'20-02-12 19:00'", "'21-02-15 19:00'")
    return "created"

@app.route('/api/flights/delete/')
def delete():
    flight.delete(3)
    return "deleted"


if __name__ == "__main__":
    app.run()

