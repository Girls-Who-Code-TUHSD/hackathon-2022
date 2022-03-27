# Importing needed libraries
import flask
from flask import request, jsonify, render_template
import csv

# Configuring the Flask server set up. Currently we are in DEBUG mode for development.
app = flask.Flask(
        __name__,
        template_folder='templates',
        static_folder='static'
    )
app.config["DEBUG"] = True

# Our first method that returns at default homepage. This is HTML code for the landing.
@app.route('/', methods=['GET'])
def base_page():
    return render_template('base.html')

# Standard error handler. 
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

# Data ingestion from our stored CSV or data source.
# TODO: Change from this I/O of CSV to an SQLite DB.
def feed():
    pokemon = []
    with open('test.csv') as csv_file:
        reader = csv.DictReader(csv_file)
        for line in reader:
            pokemon.append(line)

    return {"pokemon": pokemon}

# Our default API call to return our our pokemon universe.
@app.route('/api/v1/resources/pokemon/all', methods=['GET'])
def api_all():
    return feed()

# An API function that can filter by name, type, max_height and max_weight.
@app.route('/api/v1/resources/pokemon', methods=['GET'])
def api_filter():
    # Flask provides us with a standard way of reading API arguments as below.
    query_parameters = request.args

    name = query_parameters.get('name')
    type = query_parameters.get('type')
    height = query_parameters.get("max_height")
    weight = query_parameters.get("max_weight")

    # Pull the entire Pokemon universe, then filter. 
    data = feed()
    pokemon_universe = data['pokemon']
    
    # Filtering by our query arguments. Below is an example of list comprehension.
    # TODO: Replace with SQL queries and add additional filteirng funcitonality.
    if name:
        # Checks to make sure the start of the Pokemon name and name arg match.
        pokemon_universe = [x for x in pokemon_universe if x['name'].startswith(name)]
    if type:
        pokemon_universe = [x for x in pokemon_universe if x['type'] == type]
    if height:
        pokemon_universe = [x for x in pokemon_universe if int(x['height']) <= int(height)]
    if weight:
        pokemon_universe = [x for x in pokemon_universe if int(x['weight']) <= int(weight)]
    if not (name or type or height or weight):
        # Returning an error if API was hit but valid arguments we not passed.
        return page_not_found(404)

    return {"pokemon": pokemon_universe}

# Running our App in a local enviornment.
app.run()
