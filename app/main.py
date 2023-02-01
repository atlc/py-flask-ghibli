from flask import Flask, render_template
from flask.json import jsonify
from flask_cors import CORS
import json

film_file = open('data/films.json')
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
CORS(app)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    return render_template("public/index.html")


# @app.get('/films')
# def all_films():
#     return render_template("films/all.html", films=films)


# @app.get('/films/<film_id>')
# def single_film(film_id):
#     found_film = {}
#     for film in films:
#         if (film['id'] == film_id):
#             found_film = film
#     if (found_film.__len__() > 0):
#         hours = int(int(film['running_time']) / 60)
#         minutes = int(film['running_time']) % 60
#         film_with_time = {**found_film, "hours": hours, "minutes": minutes}
#         return render_template("films/single.html", film=film_with_time)
#     else:
#         return render_template("not_found.html", resource_name="films")


# @app.get('/people')
# def all_people():
#     return render_template('people/all.html', people=people)


# @app.get('/people/<person_id>')
# def single_person(person_id):
#     found_person = {}
#     for person in people:
#         if (person['id'] == person_id):
#             found_person = person
#             for spc in species:
#                 if (spc['id'] == person['species'].replace("https://api-ghibli.herokuapp.com/species/", "")):
#                     found_person['species'] = spc['name']

#     return render_template('people/single_person.html', person=found_person)


# @app.get('/api/')
# def api_root():
#     return jsonify({"valid_paths": ["/api/films", "/api/people", "/api/species", "/api/locations", "/api/vehicles"]})


@app.get('/films')
def api_all_films():
    return jsonify(films)


@app.get('/films/<film_id>')
def api_single_film(film_id):
    found_film = {}
    for film in films:
        if (film['id'] == film_id):
            found_film = film
    return found_film


@app.get('/people')
def api_all_people():
    return jsonify(people)


@app.get('/people/<person_id>')
def api_single_person(person_id):
    found_person = {}
    for person in people:
        if (person['id'] == person_id):
            found_person = person
    return found_person


@app.get('/locations')
def all_locations():
    return jsonify(locations)


@app.get('/locations/<location_id>')
def single_location(location_id):
    found_location = {}
    for location in locations:
        if (location['id'] == location_id):
            found_location = location
    return found_location


@app.get('/species')
def all_species():
    return jsonify(species)


@app.get('/species/<species_id>')
def single_species(species_id):
    found_species = {}
    for single in species:
        if (single['id'] == species_id):
            found_species = single
    return found_species


@app.get('/vehicles')
def all_vehicles():
    return jsonify(vehicles)


@app.get('/vehicles/<vehicle_id>')
def single_vehicle(vehicle_id):
    found_vehicle = {}
    for vehicle in vehicles:
        if (vehicle['id'] == vehicle_id):
            found_vehicle = vehicle
    return found_vehicle
