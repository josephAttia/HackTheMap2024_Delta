from flask import Flask, request
from flask import url_for
# from flask_cors import CORS
from flask import jsonify

app = Flask(__name__)

# LOLLLLL this is joe

# joe did this


italy = {
    "name": "Italy",
    "population": 60_000_000,
    "capital": "Rome",
    "language": "Italian",
    "currency": "Euro",
}

# api endpoint that add flight cost the databse for each country dynamically
 


@app.route('/')
def hello():
    return 'Hello, World!'


@app.get("/api/places")
def get_places():
    return {"places": ["place1", "place2"]}

# /reg/user/<id>


# this is a comment by joe

@app.get("/api/places/<place_id>")
def get_place(place_id):
    # for:
    #     if place_id == "italy":
            # call a request to google flights api passing italy as the destination and the user location as the origin and save the cost in the database
    
    if place_id == "italy":
        return italy
    return {"place": place_id}

if __name__ == '__main__':
    app.run(debug=True)