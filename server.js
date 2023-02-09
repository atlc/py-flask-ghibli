const express = require("express");
const cors = require("cors");

const films = require("./data/films.json");
const people = require("./data/people.json");
const locations = require("./data/locations.json");
const species = require("./data/species.json");
const vehicles = require("./data/vehicles.json");

const app = express();
app.use(cors());

app.use(express.static("public"));

app.get("/films", (req, res) => {
    res.json(films);
});

app.get("/films/:id", (req, res) => {
    const { id } = req.params;

    const [film] = films.filter(f => f.id === id);

    if (!film) {
        res.json({});
    } else {
        res.json(film);
    }
});

app.get("/people", (req, res) => {
    res.json(people);
});

app.get("/people/:id", (req, res) => {
    const { id } = req.params;

    const [person] = people.filter(p => p.id === id);

    if (!person) {
        res.json({});
    } else {
        res.json(person);
    }
});

app.get("/locations", (req, res) => {
    res.json(locations);
});

app.get("/locations/:id", (req, res) => {
    const { id } = req.params;

    const [location] = locations.filter(l => l.id === id);

    if (!location) {
        res.json({});
    } else {
        res.json(location);
    }
});

app.get("/species", (req, res) => {
    res.json(species);
});

app.get("/species/:id", (req, res) => {
    const { id } = req.params;

    const [single] = species.filter(s => s.id === id);

    if (!single) {
        res.json({});
    } else {
        res.json(single);
    }
});

app.get("/vehicles", (req, res) => {
    res.json(vehicles);
});

app.get("/vehicles/:id", (req, res) => {
    const { id } = req.params;

    const [vehicle] = vehicles.filter(v => v.id === id);

    if (!vehicle) {
        res.json({});
    } else {
        res.json(vehicle);
    }
});

app.use((req, res) => {
    res.json({ message: "Only GET requests to the following routes are supported", routes: ["/films", "/people", "/locations", "/species", "/vehicles"] });
});

app.listen(process.env.PORT || 3000);
