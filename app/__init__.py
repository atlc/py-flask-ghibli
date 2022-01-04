from flask import Flask, render_template
from flask.json import jsonify
import json


film_file = open('data/films.json', "r")
films = json.loads(film_file.read())
film_file.close()

people_file = open('data/people.json')
people = json.loads(people_file.read())
people_file.close()

locations_file = open('data/locations.json')
locations = json.loads(locations_file.read())
locations_file.close()

species_file = open('data/species.json')
species = json.loads(species_file.read())
species_file.close()

vehicles_file = open('data/vehicles.json')
vehicles = json.loads(vehicles_file.read())
vehicles_file.close()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("public/index.html")


@app.get('/films')
def all_films():
    return render_template("films/all.html", films=films)


@app.get('/films/<film_id>')
def single_film(film_id):
    found_film = {}
    for film in films:
        if (film['id'] == film_id):
            found_film = film
    if (found_film.__len__() > 0):
        hours = int(int(film['running_time']) / 60)
        minutes = int(film['running_time']) % 60
        film_with_time = {**found_film, "hours": hours, "minutes": minutes}
        print(film_with_time)
        return render_template("films/single.html", film=film_with_time)
    else:
        return render_template("not_found.html", resource_name="films")


@app.get('/people')
def all_people():
    return jsonify(people)


@app.get('/people/<person_id>')
def single_person(person_id):
    found_person = {}
    for person in people:
        if (person['id'] == person_id):
            found_person = person
    if (found_person.__len__() > 0):
        return found_person
    else:
        return {"message": "No person with that ID was located"}, 404


@app.get('/locations')
def all_locations():
    return jsonify(locations)


@app.get('/locations/<location_id>')
def single_location(location_id):
    found_location = {}
    for location in locations:
        if (location['id'] == location_id):
            found_location = location
    if (found_location.__len__() > 0):
        return found_location
    else:
        return {"message": "No location with that ID was located"}, 404


@app.get('/species')
def all_species():
    return jsonify(species)


@app.get('/species/<species_id>')
def single_species(species_id):
    found_species = {}
    for single in species:
        if (single['id'] == species_id):
            found_species = single
    if (found_species.__len__() > 0):
        return found_species
    else:
        return {"message": "No species with that ID was located"}, 404


@app.get('/vehicles')
def all_vehicles():
    return jsonify(vehicles)


@app.get('/vehicles/<vehicle_id>')
def single_vehicle(vehicle_id):
    found_vehicle = {}
    for vehicle in vehicles:
        if (vehicle['id'] == vehicle_id):
            found_vehicle = vehicle
    if (found_vehicle.__len__() > 0):
        return found_vehicle
    else:
        return {"message": "No vehicle with that ID was located"}, 404
